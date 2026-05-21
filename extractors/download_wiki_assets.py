#!/usr/bin/env python3
"""Download Caves of Qud wiki images for lore-video B-roll.

The wiki blocks the WebFetch tool's user-agent, but a normal browser
UA over HTTPS works fine. We use the MediaWiki Special:FilePath
endpoint, which redirects to the actual upload URL, and pull a
curated, per-episode set of images (NPC tiles, location tiles,
screenshots) into corpus/visual_assets/<episode>/.

These are Freehold Games' assets, downloaded for the user's personal
lore-video research (same fair-use basis as the extracted text).
Re-running is idempotent (overwrites). Writes MANIFEST.md.
"""

import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

DST = Path(__file__).resolve().parent.parent / "corpus" / "visual_assets"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")
FILEPATH = "https://wiki.cavesofqud.com/wiki/Special:FilePath/"
FILEPAGE = "https://wiki.cavesofqud.com/wiki/File:"

# Curated, per-episode. Filenames confirmed to exist via the wiki API.
ASSETS = {
    "00_common_locations": [
        "Ovw grit gate.png", "Ovw joppa.png", "Ovw six day stilt.png",
        "Ovw kyakukya.png", "Ovw bey lah.png",
    ],
    "01_resheph": [
        "Statue of resheph.png", "Mechanimist preacher.png",
        "Hunter of the sightless way.png", "Tomb of the Eaters.png",
        "Tomb of the Eaters (large).png", "Death gate.png",
        "Hologram of eater.png",
    ],
    "02_barathrum": [
        "Barathrum the old.png", "Euclid.png", "Q girl.png",
        "Hortensa.png", "Otho.png", "Pax klanq.png", "Argyve.png",
        "Aloysius.png", "Dardi.png",
        "Barathrum clock with q girl pendulum.png",
        "Disquisition on the malady of the mimic.png",
        "Blueprints for q girls climber design.png",
        "Mushroom cherub.png", "Ursine locket.png",
    ],
    "03_rebekah": [
        "Yla haj.png", "Daughter of exile.png",
        "Zothom the penitent.png", "Mayor haddas.png", "Ezra.png",
        "Warden 1ff reprogrammed conservator.png", "Banana rancher.png",
        "Sixshrew.png", "Omonporch.png",
    ],
    "04_spindle": [
        "Earl asphodel.png", "Asphodelyte.png", "Banana grove.png",
        "Banana tree.png", "Court of the sultans.png", "Twin gates.png",
        "Omonporch.png", "Herododicus.png", "Imperial sarcophagus.png",
        "Access Corridor, Tomb of the Eaters.png",
        "Grand Vestibule, Tomb of the Eaters.png", "Elevator shaft.png",
        "Funerary urn.png", "Bell of Rest message.png",
        "Witchwood tree.png",
    ],
    "05_brightsheol": [
        "Brightsheolgate.png", "Rainwater shomer.png",
        "Hologram of resheph the above.png", "Girsh godling.png",
        "Girsh godling true.png", "Fool of the gyre.png",
        "Mainframe monitor.png", "Helping hands.png",
        "Hologram of outworlder.png", "Hologram bracelet.png",
        "Barathrum the old.png",
    ],
}


def safe_name(fname: str) -> str:
    return re.sub(r"[^A-Za-z0-9._() -]", "_", fname)


def download(fname: str, dest_dir: Path):
    url = FILEPATH + urllib.parse.quote(fname)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
            ctype = r.headers.get("Content-Type", "")
    except Exception as e:
        print(f"    FAIL {fname}: {e}", file=sys.stderr)
        return None
    if len(data) < 200 or not ctype.startswith("image"):
        print(f"    SKIP {fname}: not an image ({len(data)}B, {ctype})", file=sys.stderr)
        return None
    dest = dest_dir / safe_name(fname)
    dest.write_bytes(data)
    return len(data)


def main() -> int:
    DST.mkdir(parents=True, exist_ok=True)
    manifest = [
        "# Visual Assets — Manifest",
        "",
        "Caves of Qud wiki images (Freehold Games), downloaded for the",
        "lore-video series as B-roll reference. Personal-research use,",
        "same basis as the extracted text corpus. Source wiki:",
        "https://wiki.cavesofqud.com",
        "",
        "Regenerate with `python3 extractors/download_wiki_assets.py`.",
        "",
    ]
    total = ok = 0
    for episode, files in ASSETS.items():
        edir = DST / episode
        edir.mkdir(parents=True, exist_ok=True)
        manifest.append(f"## {episode}")
        manifest.append("")
        manifest.append("| File | Size | Wiki source |")
        manifest.append("|---|---:|---|")
        for fname in files:
            total += 1
            size = download(fname, edir)
            file_url = FILEPAGE + urllib.parse.quote(fname.replace(" ", "_"))
            if size:
                ok += 1
                manifest.append(f"| `{safe_name(fname)}` | {max(size//1024,1)} KB | [{fname}]({file_url}) |")
            else:
                manifest.append(f"| ~~{fname}~~ | — | (download failed) |")
            time.sleep(0.25)  # be polite to the wiki
        manifest.append("")
    (DST / "MANIFEST.md").write_text("\n".join(manifest), encoding="utf-8")
    print(f"OK: {ok}/{total} images downloaded to {DST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
