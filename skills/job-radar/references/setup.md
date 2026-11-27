# Mode configuration

But : en une conversation courte, passer de « je cherche des offres de X » à un tableau de bord rempli et une veille quotidienne programmée. L'utilisateur ne devrait jamais avoir à écrire de JSON.

## 1. Poser les questions (une seule fois, groupées)

Avec l'outil de questions s'il existe, sinon en un seul message. Ce qui est déjà dit dans la conversation n'est pas redemandé.

1. **Métier visé**, intitulés proches compris (ex. « Design System Manager », « Lead design system », « Design Ops »).
2. **Types de contrat** : freelance, CDI, CDD, alternance, stage (plusieurs choix possibles).
3. **Lieu et télétravail** : ville de résidence ; full remote obligatoire, hybride (combien de jours sur site au maximum, dans quelles villes) ou sur site accepté.
4. **Rémunération** : plancher et cible. TJM en €/jour pour le freelance, salaire brut annuel pour les autres contrats.
5. **Séniorité et points forts** : niveau (junior, confirmé, senior, lead) et 4 à 8 compétences ou sujets qui le distinguent. Secteurs aimés ou à éviter (facultatif).
6. **Rythme** (facultatif) : temps plein, 4 jours, 2 à 3 jours par semaine…

Ne demande ni nom, ni e-mail, ni téléphone, ni CV : Job Radar n'en a pas besoin.

## 2. Construire la config

Pars de `assets/config.example.json` et remplace chaque valeur par celles de l'utilisateur :

- `jobs` : 3 à 6 intitulés de poste équivalents. `searchKeywords` : les termes à chercher.
- `exclude` : ce qui ressemble au métier sans l'être (ex. pour un product designer : graphisme pur, motion, 3D, développement).
- `vocab` : 15 à 20 compétences en minuscules propres au métier. C'est le vocabulaire du champ `skills` des offres et des statistiques du tableau de bord.
- `sources` et `searchQueries` : choisis 4 à 8 sources dans `references/sources.md` selon le métier et les contrats, plus 4 à 6 recherches web. Avant de les enregistrer, vérifie que chaque page de source s'ouvre et liste bien des offres du métier (une lecture rapide par page). Retire celles qui refusent la lecture.
- `channels` : 2 à 4 canaux à suggérer sans les lire (voir la fin de `references/sources.md`), uniquement en `https://`.
- `notifyThreshold` : 70 par défaut. `maxAgeDays` : 60.

Montre à l'utilisateur un résumé lisible de la config (pas le JSON), en quelques lignes, et ajuste s'il le demande.

## 3. Créer le tableau de bord

### Mode artifact (app Claude)

1. Copie `assets/dashboard.html` dans le répertoire de travail (les fichiers du skill sont en lecture seule).
2. Publie-le avec l'outil `Artifact` : icône `radar`, titre de page conservé, et ces capabilities :
   ```json
   {"db": {"rules": [
     {"path": "config",   "read": "view", "write": "owner"},
     {"path": "missions", "read": "view", "write": "owner"},
     {"path": "runs",     "read": "view", "write": "owner"},
     {"path": "statuses", "read": "view", "write": "owner"}
   ]}, "user": {}}
   ```
3. Écris la config avec `ArtifactData` : `set` sur la collection `config`, document `profile`, avec l'objet JSON complet.
4. Note l'URL de l'artifact : c'est elle que la tâche planifiée utilisera.

### Mode local

1. Crée `job-radar-data/config.json` avec la config, puis `job-radar-data/missions.json` (`[]`) et `job-radar-data/runs.json` (`[]`).
2. Génère la page : `python3 <dossier du skill>/scripts/build_local.py job-radar-data`. Elle sort dans `job-radar-data/job-radar.html`.

## 4. Premier passage

Lance tout de suite un passage complet en suivant `references/scan.md`, pour que l'utilisateur voie un tableau de bord rempli et puisse corriger le tir (sources trop larges, score trop sévère…).

## 5. Programmer la veille quotidienne

Cherche l'outil de tâches planifiées de la session (par exemple `create_trigger`, ou via la recherche d'outils). Crée une tâche **quotidienne** le matin, à l'heure demandée par l'utilisateur ou vers 7 h–8 h dans son fuseau. Le texte de la tâche doit se suffire à lui-même :

> Passage quotidien de Job Radar. Utilise le skill `job-radar` en mode « passage quotidien » pour le tableau de bord <URL de l'artifact, ou chemin du dossier job-radar-data>. Si le skill `job-radar` n'est pas disponible dans cette session, envoie une notification qui le dit et arrête-toi. Ne postule à rien, ne contacte personne, ne publie rien ailleurs.

Active les notifications push si l'outil le permet. S'il n'existe aucun outil de tâches planifiées, dis-le simplement. En mode local, propose une commande à mettre dans le planificateur du système, par exemple `claude -p "Passage quotidien de Job Radar pour le dossier job-radar-data"`.

## 6. Conclure

En trois ou quatre lignes : ce qui est en place, combien d'offres le premier passage a trouvées, l'heure du passage quotidien, et le fait que l'utilisateur peut à tout moment dire « modifie mon profil Job Radar » pour relancer cette configuration.
