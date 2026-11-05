# Awesome-list PR

Find lists with `gh api -X GET search/repositories -f q='awesome claude code'` or search GitHub for "awesome-claude-code", "awesome-claude-skills", "awesome-agent-skills". Follow each list's CONTRIBUTING.md (most want alphabetical order and a one-line description).

## Entry line

```markdown
- [ai-philosophers](https://github.com/BhackerJ/ai-philosophers) - 48 philosopher personas (Socrates to Arendt, Confucius to Dōgen) as skills, each with verified quotations and anachronism guards, plus `/symposium` for staged debates between them.
```

## PR title

```
Add ai-philosophers (48 philosopher persona skills + debates)
```

## PR body

```markdown
Adds [ai-philosophers](https://github.com/BhackerJ/ai-philosophers): 48 philosopher personas for Claude Code (plugin marketplace + plain skills) and OpenClaw.

What makes it different from a prompt collection:
- Each persona has a verified-quotations list with sources and a list of famous misattributions it will correct
- Personas don't fake knowledge of modern things; they ask and reason by analogy
- `/symposium kant mill Is it ever right to lie?` stages a real two-sided debate
- Ships an eval suite for `claude plugin eval`

MIT licensed.
```
