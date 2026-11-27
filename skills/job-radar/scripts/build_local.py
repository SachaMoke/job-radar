#!/usr/bin/env python3
"""Job Radar, mode local : génère job-radar.html à partir des fichiers JSON d'un dossier.

Usage : python3 build_local.py <dossier-job-radar-data>

Le dossier doit contenir config.json, missions.json (liste d'offres avec un champ "id")
et runs.json (liste de passages). Le script lit ces trois fichiers, les intègre au modèle
assets/dashboard.html et écrit <dossier>/job-radar.html. Il n'utilise que la bibliothèque
standard, ne fait aucun appel réseau et n'écrit rien ailleurs que dans ce dossier.
"""
import json
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "dashboard.html"
MARKER = '<script type="application/json" id="job-radar-data">null</script>'


def load(path: Path, default):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    folder = Path(sys.argv[1]).resolve()
    if not folder.is_dir():
        print(f"Dossier introuvable : {folder}")
        return 1

    data = {
        "config": load(folder / "config.json", {}),
        "missions": load(folder / "missions.json", []),
        "runs": load(folder / "runs.json", []),
    }
    template = TEMPLATE.read_text(encoding="utf-8")
    if MARKER not in template:
        print("Modèle inattendu : bloc job-radar-data introuvable.")
        return 1

    # JSON intégré dans <script> : chaque "<" est échappé pour qu'aucun contenu
    # d'offre ne puisse fermer la balise ni injecter du HTML.
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    html = template.replace(MARKER, f'<script type="application/json" id="job-radar-data">{payload}</script>')

    out = folder / "job-radar.html"
    out.write_text(html, encoding="utf-8")
    print(f"Tableau de bord généré : {out} ({len(data['missions'])} offres)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
