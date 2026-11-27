# Catalogue de sources

Point de départ pour composer la liste `sources` et `searchQueries` d'un profil. Les adresses marquées ✅ ont été vérifiées en novembre 2026. Pour les autres, trouve la bonne page de catégorie ou de recherche en ouvrant le site (ou avec une recherche `site:`), puis enregistre-la dans la config. Les sites changent : si une page ne répond plus, cherche sa nouvelle adresse au passage suivant et signale-le dans la note du passage (`runs`).

**Règle commune** : on lit seulement ce qui est public, sans connexion. Si un site refuse la lecture automatique, on passe au suivant.

## Plateformes généralistes France

| Source | Contrats | Préfixe | Notes |
|---|---|---|---|
| Free-Work | freelance, CDI | `fw` | Très fourni en tech, product, design, data. ✅ `https://www.free-work.com/fr/tech-it/jobs/design`, ✅ `https://www.free-work.com/fr/tech-it/jobs/product-design` (`?page=N` pour paginer). Autres métiers : catégorie voisine sous `/fr/tech-it/jobs/`. TJM souvent affiché. |
| FreelanceRadar | freelance | `fr` | Agrège des missions de plusieurs plateformes. ✅ `https://www.freelanceradar.co/missions/ux-ui-designer/remote` ; adapter le métier et le lieu dans l'adresse. |
| Freelance-Informatique | freelance | `fi` | Beaucoup d'ESN et de grands comptes. ✅ `https://www.freelance-informatique.fr/freelance-ux-design-2469`, ✅ `https://www.freelance-informatique.fr/freelance-ui-design-2899`. TJM rarement affiché ; ouvrir chaque mission pour le lieu et le télétravail. |
| Welcome to the Jungle | CDI, CDD, freelance, stage | `wttj` | Recherche par métier et contrat. Les offres expirées affichent « n'est plus disponible ». |
| HelloWork | CDI, CDD, intérim | `hw` | Généraliste, bon pour les métiers hors tech. |
| APEC | CDI, CDD (cadres) | `apec` | Peut demander une recherche interactive. Si la liste n'est pas lisible, passe. |
| France Travail | tous | `ft` | Très large, beaucoup de doublons d'autres sites. |
| LeHibou | freelance | `lh` | Missions IT et digital, parfois en Belgique : vérifier le pays. |
| Collective.work | freelance | `cw` | Missions product, design, tech. Certaines annonces sont relayées sur arc.dev. |
| Crème de la Crème | freelance | `cdc` | Pages mission parfois publiques (`site:cremedelacreme.io`). |
| Wizbii | CDI, alternance, stage, freelance | `wz` | Relaie aussi des missions d'autres plateformes. |

## International en remote (garder seulement ce qui est ouvert à la France ou à l'Europe)

| Source | Contrats | Préfixe | Notes |
|---|---|---|---|
| Dribbble Jobs | freelance, CDI | `dr` | Design. ✅ `https://dribbble.com/jobs?anywhere=true&job_type=freelance` ; ouvrir l'offre pour vérifier le type de contrat. |
| Himalayas | contrat, CDI | `hm` | ✅ `https://himalayas.app/jobs/contractor-product-designer`. Beaucoup d'offres limitées à un pays : lire la restriction de lieu et la date « Apply before ». |
| We Work Remotely | contrat, CDI | `wwr` | ✅ `https://weworkremotely.com/categories/remote-design-jobs` ; autres catégories pour dev, produit, marketing… |
| IxDF Jobs | freelance, CDI | `ixdf` | Design et UX. Remontent bien par recherche web. |
| Remotive, RemoteOK, Arc.dev | contrat, CDI | `rmt`, `rok`, `arc` | Tech et produit. Vérifier l'éligibilité géographique. |

## Pistes par famille de métiers

- **Design (product, UX/UI, design system, UX research, UX writing)** : Free-Work (design, product-design), FreelanceRadar, Freelance-Informatique, Dribbble, Himalayas, WWR, IxDF, Collective.work, Welcome to the Jungle. Recherches : « mission freelance <métier> remote », « <métier> freelance télétravail », « site:cremedelacreme.io <métier> ».
- **Développement et data** : Free-Work (catégorie du langage ou du métier), Freelance-Informatique, LeHibou, WWR et Remotive (programming, data), Welcome to the Jungle.
- **Product management** : Free-Work (product-owner, product-manager), Collective.work, Welcome to the Jungle, Himalayas.
- **Marketing, growth, contenu** : Welcome to the Jungle, HelloWork, Collective.work, WWR (marketing), FreelanceRadar.
- **Métiers hors tech** : HelloWork, APEC, France Travail, Welcome to the Jungle, sites spécialisés du secteur.

## Canaux à suggérer sans les lire (section « Où chercher aussi »)

Malt (profil et disponibilité à jour), LinkedIn (réseau et alertes), communautés Slack ou Discord du métier, anciens collègues et managers. Job Radar ne s'y connecte pas : ce sont des rappels affichés dans le tableau de bord (`channels` de la config).
