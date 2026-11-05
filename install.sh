#!/bin/bash
# Install philosopher skills to ~/.claude/skills/
#   bash install.sh                  # all philosophers + the /philosophers switchboard
#   bash install.sh socrates kant    # only the ones you name
set -euo pipefail

SKILLS_DIR="$HOME/.claude/skills"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$SKILLS_DIR"

if [ "$#" -gt 0 ]; then
  names=("$@")
else
  names=()
  for dir in "$SCRIPT_DIR"/*/; do
    [ -f "$dir/SKILL.md" ] && names+=("$(basename "$dir")")
  done
fi

count=0
for name in "${names[@]}"; do
  src="$SCRIPT_DIR/$name"
  if [ ! -f "$src/SKILL.md" ]; then
    echo "  skipped: $name (no such skill)"
    continue
  fi
  rm -rf "${SKILLS_DIR:?}/$name"
  cp -r "$src" "$SKILLS_DIR/"
  echo "  installed: $name"
  [ "$name" != "philosopher-pack" ] && count=$((count + 1))
done

echo ""
echo "$count philosophers installed to $SKILLS_DIR"
echo "Restart Claude Code, then try: /socrates"
