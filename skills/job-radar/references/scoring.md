# Barème de score

Le score (0 à 100) dit à quel point une offre correspond au profil enregistré dans la config. Il sert à trier et à déclencher la notification (`notifyThreshold`, 70 par défaut). Applique le barème tel quel, puis borne le résultat entre 0 et 100. Si l'utilisateur a ajouté un bloc `scoring` à sa config, ses valeurs remplacent celles-ci.

| Critère | Points |
|---|---|
| Base | **40** |
| **Télétravail** (comparer à `remote.wanted`) | |
| Full remote | +25 |
| Télétravail partiel compatible (jours sur site ≤ `maxOnsiteDaysPerWeek`, et lieu dans `acceptOnsiteIn` ou proche de `location.city`) | +10 |
| Sur site dans la ville ou la région de l'utilisateur, quand il accepte le sur site | +5 |
| Présence régulière exigée loin de la ville de l'utilisateur | −15 |
| **Rémunération** (TJM en €/jour pour le freelance, salaire brut annuel pour les autres contrats ; haut de fourchette) | |
| ≥ cible (`target`) | +15 |
| entre plancher et cible | +10 |
| jusqu'à 10 % sous le plancher | +3 |
| plus de 20 % sous le plancher | −10 |
| non affichée | 0 |
| **Sujet** : métier visé (`jobs`), points forts (`strengths`) ou secteurs aimés (`sectorsLiked`) au cœur de l'offre | +10 |
| **Séniorité** égale ou proche de celle du profil | +5 |
| **Décalage** : autre métier, l'un des `exclude`, séniorité nettement plus basse, ou secteur dans `sectorsAvoided` | −15 |
| **Fraîcheur** : publiée il y a plus de 45 jours | −10 |
| **Contrat** non souhaité (absent de `contracts`) | ne pas ajouter l'offre |

## Le champ `why`

Une ou deux phrases honnêtes, adressées à l'utilisateur en le tutoyant, qui disent ce qui colle et ce qui coince. Pas de flatterie et pas de remplissage. Exemples :

- « Design system au cœur de la mission et TJM au-dessus de ta cible, mais 3 jours sur site à Lille. »
- « Bon sujet, mais l'offre cherche surtout un profil UI junior : décalage de séniorité. »

## Champs d'une offre (`missions/<id>`)

| Champ | Valeur |
|---|---|
| `title`, `company`, `source`, `url`, `location` | texte (`company` vide si non nommée) |
| `contract` | `freelance` \| `cdi` \| `cdd` \| `alternance` \| `stage` \| `interim` \| `unknown` |
| `remote` | `full` \| `partial` \| `onsite` \| `unknown` |
| `tjmMin`, `tjmMax` | nombres en €/jour, freelance seulement, omis si inconnus |
| `salaryMin`, `salaryMax` | nombres en € brut par an, omis si inconnus |
| `duration` | texte (« 6 mois renouvelables », « CDI »…) |
| `published` | `AAAA-MM-JJ`, date de publication, omise si inconnue |
| `firstSeen` | `AAAA-MM-JJ`, date du jour du passage |
| `tags` | 2 à 3 mots-clés courts |
| `skills` | compétences demandées, en minuscules, prises dans `vocab` de la config |
| `seniority` | `junior` \| `confirmé` \| `senior` \| `lead` \| `unknown` |
| `score`, `why`, `active` | nombre, texte, `true` |

L'identifiant `<id>` est court, en minuscules, avec des lettres, des chiffres et des tirets. Il commence par le `prefix` de la source (ex. `fw-acme-lead-ds`) et doit être unique dans la base.
