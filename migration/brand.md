# Charte graphique et médias repris de Squarespace

Relevé fait le 6 novembre 2026 sur le site public guillaumelarquemain.com (HTML, feuilles de style `site.css` et `static.css`, plan de site).

## Typographies

| Usage Squarespace | Police | Graisse / style | Réglages |
|---|---|---|---|
| Titres (heading) | Helvetica Neue, repli Arial, sans-serif | 400 normal | interlettrage 0,02 em, interligne 1,5 em, pas de capitales forcées |
| Corps de texte (body) et navigation | Helvetica Neue, repli Arial, sans-serif | 400 normal | interlettrage 0,1 em, interligne 0,9 em |
| Méta (prix, légendes) | Helvetica Neue, repli Arial, sans-serif | 400 normal | interlettrage 0,04 em, interligne 1,1 em |
| Boutons (primaire, secondaire, en-tête) | roc-grotesk (Adobe Fonts) | 400 normal | |

Taille de base : 13 px.

Conséquences pour Shopify :
- Helvetica Neue est une police système : aucun fichier à récupérer, Squarespace ne l'héberge pas. Dans l'éditeur de thème Shopify, choisir « Helvetica » (bibliothèque Shopify) ou charger Helvetica Neue en police personnalisée si vous possédez la licence.
- roc-grotesk est servie par Adobe Fonts via la licence Squarespace ; les fichiers ne sont pas récupérables et la licence ne se transfère pas. Sur Shopify, soit souscrire Adobe Fonts et l'intégrer dans le thème, soit choisir une grotesque proche de la bibliothèque Shopify (par exemple Work Sans, Archivo ou Inter).

## Couleurs

Palette Squarespace volontairement réduite au noir et blanc (toutes les variables d'accent sont à 0, 0 %, 100 % ou 0, 0 %, 0 %).

| Rôle | Valeur |
|---|---|
| Fond de site, en-tête | #FFFFFF |
| Titres, paragraphes, liens de navigation | #000000 |
| Bouton primaire | fond noir, texte blanc (thèmes de section « white » et « bright ») |
| Sections inversées | fond noir, texte blanc |

Thèmes de section utilisés : `white`, `bright`, `white-bold`.

## Logo

- Fichier d'origine : `01-Guillaume Larquemain-LOGO.png`, PNG 792 × 136 px, fond transparent. C'est la seule version hébergée sur Squarespace (pas de SVG). Pour un affichage net sur écrans haute densité, demander le fichier vectoriel au graphiste.
- Utilisé en logo d'en-tête et en image de partage (Open Graph).
- Favicon : Squarespace servait son favicon par défaut, aucun favicon de marque à reprendre.
- Importé dans Shopify → Contenu → Fichiers sous le nom `Guillaume-Larquemain-LOGO.png`.

## Médias

Inventaire des visuels hors fiches produits (les 100 images produits sont déjà sur les fiches Shopify) :

| Groupe | Nombre | Contenu |
|---|---|---|
| Visuels de pages (accueil, portrait, presse, questions) | 78 images (46 Mo, JPEG et PNG originaux) | photos de campagne, défilés (NYFW, VFW), atelier, retombées presse, logos de titres de presse (ELLE, L'Officiel, Harper's Bazaar, In Style, Les Inrocks, Nylon, Schön, Vogue China, WWD, Fashion Network) |
| Vidéos | 2 fichiers MP4 H.264 | « Guillaume Larquemain-Sac BLOOM » (8 s, 2048 × 1080, avec son) sur l'accueil ; « NCZF3401 » (6 s, 1920 × 1080) sur la page presse. Squarespace ne sert que du HLS : fichiers reconstitués sans réencodage, dans la meilleure qualité disponible. Une vignette JPEG accompagne chaque vidéo. |
| Logo | 1 PNG | voir plus haut |

Le kit complet (logo, médias, vidéos) a été fourni en archive `larquemain-brand-kit.zip` à part du dépôt.

Tout est aussi importé dans Shopify → Contenu → Fichiers, prêt à être utilisé dans l'éditeur de thème : le logo (PNG natif), les 78 visuels de pages (JPEG et PNG d'origine, pleine résolution, texte alternatif repris du nom de fichier) et les 2 vidéos MP4. Les images produits restent sur leurs fiches respectives.

## Pages à recréer sur Shopify

Contenu éditorial Squarespace à reporter dans les pages Shopify (handles attendus par les redirections) :

| Page Squarespace | Page Shopify |
|---|---|
| Accueil (`/home-1`) | page d'accueil du thème |
| Portrait (`/portrait`) | `pages/portrait` |
| Presse (`/presse`) | `pages/presse` |
| Questions (`/vosquestions`) | `pages/faq` |
| Livraisons et retours (`/shipping-returns`) | politique de livraison (Paramètres → Politiques) |

Contact affiché sur le site : contact@guillaumelarquemain.com.
