# Mode passage quotidien

Le passage tourne souvent sans personne devant l'écran. Il doit finir seul et ne déranger l'utilisateur que s'il y a quelque chose qui mérite son attention.

## 1. Charger l'état

- **Mode artifact** : charge `ArtifactData` (ou `read_db`/`write_db`). Lis `config/profile` (`get`), puis toute la collection `missions` (`list`, limite 1000, avec `out_dir` si la base est grosse). Retiens pour chaque offre son id, son URL, son `published`, son `active` et sa `version`.
- **Mode local** : lis `job-radar-data/config.json`, `missions.json` et `runs.json`.
- S'il n'y a pas de config, arrête-toi et dis qu'il faut d'abord configurer Job Radar (`references/setup.md`).

## 2. Chercher

1. Pour chaque entrée de `sources`, ouvre la page (et ses `pages` suivantes, si indiquées) avec l'outil de lecture web disponible : WebFetch, ou un sous-agent de lecture web. Pour aller plus vite, tu peux répartir les sources entre plusieurs sous-agents, en donnant à chacun la liste des URL déjà connues pour qu'il les saute.
2. Lance chaque requête de `searchQueries` avec la recherche web.
3. Ouvre la page de détail de chaque offre candidate pour lire : type de contrat, lieu, télétravail, rémunération, durée, date de publication, séniorité et compétences.
4. Ne garde que les offres qui :
   - correspondent à l'un des `jobs` (ou à un intitulé clairement équivalent) et à aucun des `exclude` ;
   - ont un contrat présent dans `contracts` ;
   - sont accessibles depuis la ville ou le pays de l'utilisateur (remote ouvert à son pays, ou lieu compatible avec ses préférences) ;
   - ne sont ni expirées ni publiées il y a plus de `maxAgeDays` jours ;
   - ont une URL absente de la base. Une offre identique republiée sous une autre URL (même entreprise, même titre, même contenu) compte comme un doublon : ne l'ajoute pas, mais signale-le dans la note du passage.
5. Convertis si besoin : un taux horaire vaut × 7 à 8 h pour obtenir un TJM ; une autre devise se convertit en euros au cours approximatif. Signale l'approximation dans `why`.

## 3. Écrire les nouvelles offres

Pour chaque offre retenue, calcule le score et rédige `why` selon `references/scoring.md`, puis crée `missions/<id>` avec l'opération `set` et `active: true`, `firstSeen` = date du jour.

- **Mode artifact** : opération groupée (`batch`), 50 écritures au plus par appel, avec une pause d'environ 2 s entre deux appels.
- **Mode local** : ajoute l'offre à `missions.json` avec un champ `id`.

## 4. Mettre à jour les offres existantes

- Offre dont tu as constaté, en ouvrant sa page, qu'elle est fermée, expirée ou supprimée : `update` avec `if_version` et uniquement `{ "active": false }`.
- Offre active publiée il y a plus de `maxAgeDays` jours : même chose.
- Ne modifie aucun autre champ et ne touche jamais à `statuses`.

## 5. Enregistrer le passage

Crée `runs/<AAAA-MM-JJ>` (`set`) avec :

```json
{ "at": "<horodatage ISO avec le fuseau de la config>", "added": 0, "checked": 0, "note": "<une phrase>" }
```

`checked` est le nombre de sources effectivement lues. La note mentionne ce qui mérite d'être su : source en panne ou qui refuse la lecture, doublons ignorés, offres désactivées. En mode local, ajoute ce même objet à `runs.json`, puis régénère la page avec `python3 <dossier du skill>/scripts/build_local.py job-radar-data`.

## 6. Prévenir (ou pas)

- Si au moins une offre **ajoutée** a un score ≥ `notifyThreshold` : envoie une notification (PushNotification s'il existe, sinon un message à l'utilisateur, sinon la réponse finale). Liste ces offres avec titre, contrat, rémunération, télétravail et lien. La première phrase doit se suffire à elle-même : c'est elle qui s'affiche sur le téléphone.
- Si une source essentielle est tombée (plusieurs refus, ou la config est cassée), notifie-le aussi.
- Sinon, pas de notification. Termine par une ligne : « Job Radar à jour : N nouvelles offres, aucune au-dessus de <seuil>. »
