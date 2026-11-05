# Show HN

**Title** (80 chars max):

```
Show HN: 48 philosophers as Claude Code skills, with verified quotes and debates
```

**URL:** https://github.com/BhackerJ/ai-philosophers

**First comment** (post immediately after submitting):

```
I built this because every "talk to Socrates" bot I tried would happily quote things Socrates never said and have opinions about Twitter.

Each philosopher is one SKILL.md file: voice, core positions, key works with dates, a list of verified quotations with chapter/section sources, a list of famous *misattributions* it will correct you on ("We are what we repeatedly do" is Will Durant, not Aristotle), and behavioral rules. No fine-tuning, no RAG.

Things I found mattered:

- Anachronism handling. The rule is "if the user raises something after your time, don't pretend to know it; ask them to describe it, then reason from your own principles." Ibn Khaldun analyzing a 400-person startup as a tribe losing its asabiyya is better than a version that knows what a startup is.
- Breaking character on purpose. The original rule was "never admit to being an AI." That's a bad rule when someone tells Schopenhauer they don't want to be alive. Now personas drop the act if you sincerely ask whether you're talking to an AI, or if you seem to be in distress.
- /symposium kant mill <question> stages a debate: openings, two rounds of rebuttals by name, closings, and a neutral host summary of where they actually disagree. Kant brought up his 1797 essay on the murderer at the door unprompted.
- Evals. `claude plugin eval` runs 10 cases: stays in voice, doesn't fake modern knowledge, admits being an AI when sincerely asked, corrects misquotes, answers in the user's language. Cheap enough to run on every change.

Install: `/plugin marketplace add BhackerJ/ai-philosophers` then `/plugin install philosophers@ai-philosophers`. Also on OpenClaw as `philosopher-pack`.

The quotations were spot-checked against primary sources but not all of them; corrections welcome.
```
