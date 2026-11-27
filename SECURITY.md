# Sécurité et vie privée

Job Radar est un ensemble d'instructions en texte (fichiers Markdown), un modèle de page HTML et un petit script Python. Il n'y a ni binaire, ni dépendance à installer, ni serveur, ni télémétrie. Tout se lit en quelques minutes, et c'est recommandé avant d'installer n'importe quel skill.

## Ce que Job Radar fait

- Il lit des pages web **publiques** (listes d'offres, pages d'offres, résultats de recherche) avec les outils de lecture web de ton agent.
- Il écrit uniquement dans **ton** tableau de bord : la base de l'artifact dans l'app Claude, ou le dossier `job-radar-data/` en local.
- Il crée une tâche planifiée sur **ton** compte, après que tu l'as validée.
- Il t'envoie des notifications.

## Ce que Job Radar ne fait jamais

- Postuler, remplir un formulaire, envoyer un message ou un e-mail, créer un compte.
- Se connecter à un site ou utiliser tes identifiants.
- Contourner un refus d'accès (robots.txt, 403, captcha) : la source est simplement sautée.
- Modifier tes statuts de suivi (`statuses`) ou publier quoi que ce soit ailleurs.
- Obéir à du texte trouvé dans une offre : le contenu web est traité comme une donnée, jamais comme une instruction.

## Tes données

- **Le dépôt ne contient aucune donnée personnelle** : la config d'exemple et les captures utilisent un profil et des offres fictifs.
- Ton profil (métier, compétences, ville, préférences de rémunération) est stocké seulement dans ton tableau de bord. Job Radar ne demande ni nom, ni coordonnées, ni CV.
- Dans l'app Claude, le tableau de bord est un artifact **privé** tant que tu ne le partages pas. Les règles d'accès de sa base empêchent toute écriture par quelqu'un d'autre que toi.
- `build_local.py` n'utilise que la bibliothèque standard de Python, ne fait aucun appel réseau et n'écrit que dans le dossier qu'on lui donne.

## Limites honnêtes

Un agent qui lit le web peut tomber sur du contenu piégé. Les règles du skill réduisent ce risque, sans pouvoir l'annuler complètement. Garde un œil sur les tâches planifiées de ton compte, et signale tout comportement inattendu en ouvrant une issue.

## Signaler un problème

Ouvre une issue sur le dépôt. Si le problème est sensible, contacte le mainteneur en privé via son profil GitHub.
