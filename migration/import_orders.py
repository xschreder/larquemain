#!/usr/bin/env python3
"""Importe les commandes historiques Squarespace dans Shopify via orderCreate.

Pourquoi ce script : la mutation orderCreate n'est accessible qu'avec un jeton
d'application « hors ligne » (custom app), pas avec le connecteur Shopify de
Claude. Tout le reste de la migration (produits, collection, clients) a été
fait directement via le connecteur.

Prérequis :
  1. Dans l'admin Shopify : Paramètres > Applications et canaux de vente >
     Développer des applications > Créer une application.
     Portées Admin API à cocher : write_orders, read_orders, write_customers,
     read_customers, read_products.
     Installer l'application, puis copier le « jeton d'accès Admin API »
     (il commence par shpat_...).
  2. Exporter deux variables d'environnement :
       export SHOPIFY_STORE="larquemain-e2ctsky3.myshopify.com"
       export SHOPIFY_ADMIN_TOKEN="shpat_..."
  3. Lancer :
       python3 migration/import_orders.py chemin/vers/orders_shopify.json
     Option --dry-run pour afficher ce qui serait envoyé sans rien créer.

Le fichier d'entrée est une liste d'objets OrderCreateOrderInput déjà prêts
(générés depuis l'export Squarespace). Le script est idempotent : il saute
toute commande dont le sourceIdentifier existe déjà dans Shopify.

Limite Shopify : 5 commandes créées par minute sur une boutique de
développement ou en essai. Le script attend 15 s entre deux créations.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

API_VERSION = "2026-10"
PAUSE_SECONDS = 15  # 4 commandes par minute, sous la limite de 5

ORDER_CREATE = """
mutation($order: OrderCreateOrderInput!, $opts: OrderCreateOptionsInput) {
  orderCreate(order: $order, options: $opts) {
    order { id name processedAt displayFinancialStatus displayFulfillmentStatus
            totalPriceSet { shopMoney { amount currencyCode } } customer { id } }
    userErrors { field message }
  }
}
"""

FIND_ORDER = """
query($q: String!) {
  orders(first: 1, query: $q) { nodes { id name sourceIdentifier } }
}
"""

OPTIONS = {
    "inventoryBehaviour": "BYPASS",
    "sendReceipt": False,
    "sendFulfillmentReceipt": False,
}


def graphql(store, token, query, variables):
    url = f"https://{store}/admin/api/{API_VERSION}/graphql.json"
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": token,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code} depuis Shopify : {detail}") from exc
    if payload.get("errors"):
        raise SystemExit(f"Erreur GraphQL : {json.dumps(payload['errors'], ensure_ascii=False)}")
    return payload["data"]


def already_imported(store, token, source_identifier):
    data = graphql(store, token, FIND_ORDER, {"q": f"source_identifier:{source_identifier}"})
    nodes = data["orders"]["nodes"]
    return nodes[0] if nodes else None


def main(argv):
    dry_run = "--dry-run" in argv
    args = [a for a in argv if a != "--dry-run"]
    if len(args) != 1:
        print(__doc__)
        return 2
    store = os.environ.get("SHOPIFY_STORE")
    token = os.environ.get("SHOPIFY_ADMIN_TOKEN")
    if not store or not token:
        print("Définir SHOPIFY_STORE et SHOPIFY_ADMIN_TOKEN dans l'environnement.")
        return 2

    with open(args[0], encoding="utf-8") as fh:
        orders = json.load(fh)

    created, skipped, failed = 0, 0, 0
    for index, order in enumerate(orders):
        label = f"{order.get('name', '?')} ({order.get('email', '?')})"
        existing = already_imported(store, token, order["sourceIdentifier"])
        if existing:
            print(f"- {label} : déjà importée sous {existing['name']}, ignorée")
            skipped += 1
            continue
        if dry_run:
            print(f"- {label} : serait créée ({len(order['lineItems'])} ligne(s))")
            continue
        data = graphql(store, token, ORDER_CREATE, {"order": order, "opts": OPTIONS})
        result = data["orderCreate"]
        if result["userErrors"]:
            print(f"- {label} : ÉCHEC {json.dumps(result['userErrors'], ensure_ascii=False)}")
            failed += 1
        else:
            o = result["order"]
            total = o["totalPriceSet"]["shopMoney"]
            print(
                f"- {label} : créée {o['name']} le {o['processedAt']}, "
                f"{total['amount']} {total['currencyCode']}, "
                f"{o['displayFinancialStatus']} / {o['displayFulfillmentStatus']}"
            )
            created += 1
        if index < len(orders) - 1:
            time.sleep(PAUSE_SECONDS)

    print(f"\nCréées : {created}, ignorées : {skipped}, échecs : {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
