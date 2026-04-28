#!/bin/bash
# Install all philosopher skills to ~/.claude/skills/
set -e

SKILLS_DIR="$HOME/.claude/skills"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$SKILLS_DIR"

count=0
for dir in "$SCRIPT_DIR"/*/; do
  if [ -f "$dir/SKILL.md" ]; then
    name=$(basename "$dir")
    cp -r "$dir" "$SKILLS_DIR/"
    echo "  installed: $name"
    ((count++))
  fi
done

echo ""
echo "$count philosophers installed to $SKILLS_DIR"
echo "Restart Claude Code, then try: /socrates"
