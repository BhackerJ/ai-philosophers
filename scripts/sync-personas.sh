#!/bin/bash
# Regenerate philosopher-pack/personas/*.md from each <name>/SKILL.md body
# (everything after the YAML frontmatter). SKILL.md files are the source of truth.
#   bash scripts/sync-personas.sh          # rewrite personas
#   bash scripts/sync-personas.sh --check  # exit 1 if any persona is out of sync
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/philosopher-pack/personas"
check=0
[ "${1:-}" = "--check" ] && check=1

stale=0
for skill in "$ROOT"/*/SKILL.md; do
  name=$(basename "$(dirname "$skill")")
  case "$name" in philosopher-pack|symposium) continue ;; esac
  body=$(awk 'c>=2 {print; next} /^---$/ {c++}' "$skill")
  target="$OUT/$name.md"
  if [ "$check" = 1 ]; then
    if [ ! -f "$target" ] || [ "$body" != "$(cat "$target")" ]; then
      echo "out of sync: $name"
      stale=1
    fi
  else
    printf '%s\n' "$body" > "$target"
  fi
done

if [ "$check" = 1 ] && [ "$stale" = 1 ]; then
  echo "Run: bash scripts/sync-personas.sh"
  exit 1
fi
exit 0
