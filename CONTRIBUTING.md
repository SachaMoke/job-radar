# Contribuer à Job Radar

Merci ! Les contributions les plus utiles sont souvent les plus simples.

## Ajouter ou corriger une source

1. Vérifie que la page est publique (lisible sans connexion) et qu'elle liste bien des offres.
2. Ajoute une ligne dans [`skills/job-radar/references/sources.md`](skills/job-radar/references/sources.md) avec le nom, les contrats couverts, un préfixe court et unique pour les identifiants, et une note sur ce qu'on y trouve. Indique la date de vérification si tu donnes une adresse précise.
3. Ne propose jamais de technique de contournement : un site qui refuse la lecture automatique est simplement sauté.

## Ajouter un métier

Complète la section « Pistes par famille de métiers » de `sources.md` avec les sources et les recherches web qui marchent pour ce métier. Si le métier a besoin d'un vocabulaire de compétences particulier, donne un exemple de liste `vocab`.

## Améliorer le tableau de bord

`skills/job-radar/assets/dashboard.html` est un fichier unique, sans build. Pour le tester en local :

```
mkdir demo && cp skills/job-radar/assets/config.example.json demo/config.json
echo "[]" > demo/missions.json && echo "[]" > demo/runs.json
python3 skills/job-radar/scripts/build_local.py demo
```

Ouvre ensuite `demo/job-radar.html`. Garde la page lisible sur mobile (390 px de large), en clair comme en sombre, et échappe toute donnée issue d'une offre avant de l'insérer dans le HTML.

## Après une modification du skill

Régénère l'archive pour l'app Claude depuis la racine du dépôt :

```
cd skills && zip -r ../dist/job-radar.zip job-radar -x "*.DS_Store" && cd ..
```

## Règles du projet

- Aucune donnée personnelle dans le dépôt. Exemples et captures restent fictifs.
- Les règles de sécurité de `SKILL.md` ne s'assouplissent pas.
- Les textes restent sobres et honnêtes : pas de promesse d'exhaustivité.
