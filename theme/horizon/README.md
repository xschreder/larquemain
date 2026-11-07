# Réglages du thème Horizon (boutique larquemain)

Fichiers de configuration appliqués le 6 novembre 2026 sur la copie non publiée du thème Horizon (« Copie de Horizon ») pour reproduire l'esprit du site Squarespace : fond blanc, texte noir, Helvetica, grille produits 4 colonnes sans cadre, titres produits en majuscules, héros vidéo plein écran.

| Fichier du thème | Copie ici | Contenu |
|---|---|---|
| `config/settings_data.json` | `config-settings_data.json` | logo, largeur de page « wide », Helvetica partout, coins carrés, aucun effet au survol, palette noir et blanc |
| `sections/header-group.json` | `sections-header-group.json` | en-tête sans barre d'annonce, logo à gauche, menu centré, sans sélecteurs pays et langue |
| `sections/footer-group.json` | `sections-footer-group.json` | pied de page Horizon avec, en premier bloc, l'ancien logo Squarespace (`Guillaume-Larquemain-LOGO.png`, lien vers l'accueil) ; le logo d'en-tête reste celui choisi dans les réglages du thème |
| `templates/index.json` | `templates-index.json` | héros vidéo (sac BLOOM) plein écran sans texte, grille de la collection « Collection » en 4 colonnes, puis les sections reprises de l'accueil Squarespace : logos « Guillaume Larquemain : dans la Presse internationale. » (2 rangées de 5), « Rendez-vous au Studio ! », et les 4 derniers articles du blog « Presse » |
| `templates/collection.json` | `templates-collection.json` | titre discret, filtres horizontaux sans tri, grille 4 colonnes, images au format portrait |
| `templates/product.json` | `templates-product.json` | titre en majuscules, accordéon « La marque » sous la description (Pourquoi la marque, Le design, La toile de pomme, Savoir-faire et engagements, Entretien et studio : contenu de la page Questions de Squarespace), section « Le savoir-faire » avec la photo de l'atelier, recommandations « Vous aimerez aussi » |

Le menu principal Shopify pointe vers Collection, Sacs, Accessoires et Contact.

Organisation des thèmes au 7 novembre 2026 : « Horizon - Larquemain (home presse) - LIVE » est publié ; « Horizon - Larquemain - STAGING » est la copie de travail, identique au thème publié plus les dernières modifications (logo Squarespace en pied de page). Le connecteur ne pouvant pas écrire sur le thème publié, les changements sont appliqués sur STAGING : les vérifier dans l'éditeur, puis soit publier STAGING, soit recopier le fichier concerné dans le thème publié.

Pour réappliquer un fichier : Boutique en ligne → Thèmes → Copie de Horizon → Modifier le code, puis coller le contenu dans le fichier correspondant. Pour publier : bouton « Publier » sur la copie une fois validée dans l'éditeur.
