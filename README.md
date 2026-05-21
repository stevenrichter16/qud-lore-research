# qud-lore-research

Workspace for extracting and indexing Caves of Qud lore for the purpose
of writing long-form YouTube video essays (Elder Scrolls–style).

See [PLAN.md](PLAN.md) for the living planning + implementation log.

## Layout

```
extractors/   Python scripts that turn Qud XML data into per-topic .md files
corpus/       The extracted, human-readable lore
  books/         one .md per in-game book
  conversations/ one .md per NPC conversation tree
  npc_index/     creature → conversation crosswalk
scripts/      eventual video-script drafts
```

## Source data

Canonical XML lives in the Steam install at:

```
~/Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base/
```

Behavior code (the procedural history generator, secrets system, Markov
text builders) lives in the full decompile at:

```
/Users/steven/qud-decompiled-project/
```

## Running

```sh
cd /Users/steven/qud-lore-research
python3 extractors/extract_books.py
python3 extractors/extract_conversations.py
python3 extractors/extract_npc_crosswalk.py
```

Re-running is idempotent — outputs overwrite. Commit the corpus to
git only after sanity-checking a few representative files.
