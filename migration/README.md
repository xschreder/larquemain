# Migration Squarespace → Shopify (Guillaume Larquemain)

Date : 6 novembre 2026.
Source : site Squarespace « Guillaume Larquemain » (guillaumelarquemain.com).
Cible : boutique Shopify `larquemain` (larquemain-e2ctsky3.myshopify.com, EUR, plan Development).

## Ce qui a été migré (fait via le connecteur Shopify)

| Donnée | Squarespace | Shopify | Statut |
|---|---|---|---|
| Produits | 14 | 14 (actifs) | fait |
| Images produits | 100 | 100 (importées depuis le CDN Squarespace) | fait |
| Collection | page boutique « Collection » | collection manuelle « Collection » (14 produits) | fait |
| Contacts | 192 | 192 clients | fait |
| Commandes | 8 | 0 | **à importer** avec `import_orders.py` (voir plus bas) |

### Produits

- Titre, description HTML, SEO (titre + meta description), SKU Squarespace, prix, vendeur « Guillaume Larquemain ».
- Type de produit et tags ajoutés pour faciliter les collections automatiques : `Sac`, `Accessoire`, `Petite maroquinerie`, `Prêt-à-porter`, `Soie`, `Toile de pomme`, etc.
- Tag `import-squarespace` sur chaque produit, et métachamp `squarespace.product_id` avec l'identifiant d'origine.
- Stock : les produits en « stock illimité » sur Squarespace sont **non suivis** dans Shopify (politique « continuer à vendre »). Les produits à stock fini sont suivis avec la quantité d'origine sur l'emplacement « Shop location ».

| Produit | Prix | Stock Shopify |
|---|---|---|
| SEED | 795 € | non suivi |
| LEEF | 695 € | 1 |
| BLOOM | 495 € | 2 |
| ROOT | 1 295 € | 3 |
| BIG APPLE BAG | 650 € | non suivi |
| Veste BUDDY | 495 € | 4 |
| CASQUETTE | 125 € | 3 |
| CARRÉ soie noire | 125 € | non suivi |
| CARRÉ soie rouge | 125 € | non suivi |
| BANDEAU soie noire | 95 € | non suivi |
| BANDEAU soie rouge | 95 € | non suivi |
| PORTE-CARTES | 95 € | non suivi |
| PORTE-PASSEPORT | 125 € | non suivi |
| CARNET A6 | 95 € | 2 |

Points à vérifier à la main dans l'admin Shopify :
- Les handles (URL) ont été repris de Squarespace quand c'était propre (`seed`, `bloom`, `casquette`…). Prévoir des redirections 301 depuis les anciennes URL `/collection/p/...` au moment de la bascule du domaine.
- Poids et dimensions d'expédition : vides sur Squarespace, donc vides sur Shopify. À renseigner si les tarifs de livraison en dépendent.
- Les prix ont été repris tels quels ; la boutique Shopify est configurée « taxes incluses dans les prix ».
- Quelques photos de produits Squarespace étaient des visuels de défilé ou d'autres produits (ex. une photo BIG APPLE BAG dans la galerie du carré rouge). Elles ont été reprises à l'identique ; à trier si besoin.

### Clients

- Email, prénom, nom, consentement marketing.
- Consentement e-mail : contacts « acceptsMarketing » sur Squarespace → **abonnés** (simple opt-in, date de consentement = date de création du contact). Les autres → non abonnés.
- Tag `import-squarespace` sur tous, note et métachamp `squarespace.contact_id` avec l'identifiant d'origine.
- 34 contacts portent en plus le tag `a-verifier` : des inscriptions d'août à octobre 2025 qui ressemblent à du spam (série « Jake Loango », adresses rogers.com, etc.). Ils ne sont **pas** abonnés aux e-mails. À supprimer dans Shopify après vérification : filtre clients `tag:a-verifier`.
- Les adresses postales ne sont pas exposées par l'API contacts de Squarespace ; elles n'ont donc pas été importées sur les fiches clients. Les adresses des 8 commandes sont dans les commandes.

### Commandes (reste à faire)

La mutation Shopify `orderCreate` n'est accessible qu'avec un jeton d'application « hors ligne » (custom app), pas avec le connecteur Shopify utilisé pour le reste. Les 8 commandes Squarespace ont été préparées au format Shopify (dates d'origine, lignes, adresses, transaction payée, statut livré) et s'importent avec `import_orders.py`.

Étapes :
1. Admin Shopify → Paramètres → Applications et canaux de vente → Développer des applications → Créer une application (ex. « Import Squarespace »).
2. Configurer les portées Admin API : `write_orders`, `read_orders`, `write_customers`, `read_customers`, `read_products`. Installer l'application et copier le jeton d'accès Admin API (`shpat_…`).
3. Lancer :

```bash
export SHOPIFY_STORE="larquemain-e2ctsky3.myshopify.com"
export SHOPIFY_ADMIN_TOKEN="shpat_..."
python3 migration/import_orders.py orders_shopify.json --dry-run
python3 migration/import_orders.py orders_shopify.json
```

Le fichier `orders_shopify.json` (8 commandes prêtes) a été fourni à part : il contient des données personnelles (adresses, téléphones) et n'est volontairement pas versionné dans ce dépôt.

Détails des commandes préparées :
- Numéros Shopify `SQ-1` à `SQ-8`, tag `import-squarespace`, métachamps `squarespace.order_id` et `squarespace.order_number`, note avec le moyen de paiement et la référence Stripe ou PayPal.
- Statut financier « payé » avec une transaction de vente datée du jour de la commande ; commandes 1 à 7 marquées livrées (date de clôture = date d'expédition Squarespace), commande 8 non expédiée.
- Pas de décrément de stock, pas d'e-mail envoyé au client.
- Commande 3 : le produit « MINI IMPERFECTO - Rouge » n'existe plus au catalogue ; la ligne est importée comme ligne libre (sans lien produit).
- Les commandes sont rattachées aux fiches clients par e-mail.

### Redirections (fait)

Les 25 URL du plan de site Squarespace (`sitemap.xml`) sont redirigées dans Shopify (Boutique en ligne → Navigation → Redirections d'URL). Le fichier `redirects.csv` est au format d'import Shopify (colonnes `Redirect from,Redirect to`) et sert de sauvegarde ou de réimport.

| Ancienne URL Squarespace | Cible Shopify |
|---|---|
| `/collection/p/<produit>` (14 fiches) | `/products/<handle>` |
| `/collection` | `/collections/collection` |
| `/collection/bags` | `/collections/sacs` (collection automatique, type « Sac ») |
| `/collection/accessoires`, `/collection/accessoires/earrings` | `/collections/accessoires` (collection automatique, types « Accessoire » et « Petite maroquinerie ») |
| `/collection/accessoires/chapeaux`, `/collection/seed` | fiche produit correspondante |
| `/home-1` | `/` |
| `/portrait`, `/presse`, `/vosquestions` | `/pages/portrait`, `/pages/presse`, `/pages/faq` |
| `/shipping-returns` | `/policies/shipping-policy` |

À faire pour que ces redirections aboutissent :
- Créer les pages Shopify `portrait`, `presse` et `faq` (handles exacts) avec le contenu des pages Squarespace, et renseigner la politique de livraison dans Paramètres → Politiques.
- Les redirections ne s'activent que sur le domaine final : pointer `guillaumelarquemain.com` vers Shopify au moment de la bascule.
- Les chemins Squarespace se terminant par un tiret (porte-cartes, porte-passeport) sont repris tels quels ; Shopify ignore la casse et la barre oblique finale.

## Fichiers

- `import_orders.py` : script d'import des commandes (Python 3, sans dépendance).
- `redirects.csv` : les 25 redirections au format d'import Shopify.
- `orders_shopify.json` (hors dépôt) : les 8 commandes au format `OrderCreateOrderInput`.

## Après la migration

- Supprimer les clients `tag:a-verifier` après contrôle.
- Vérifier la collection « Home page » (créée par Shopify) et construire la navigation du thème avec les collections Collection, Sacs et Accessoires.
- Créer les pages portrait, presse et faq, puis configurer livraison, taxes, moyens de paiement et domaine sur Shopify avant de couper Squarespace.
