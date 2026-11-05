# AI Philosophers

**AI Philosophers is a free, open-source set of 42 philosopher personas, plus a `/symposium` command that makes them debate each other, for [Claude Code](https://claude.ai/code) and [OpenClaw](https://openclaw.ai).** Install it, type `/socrates` or `/confucius`, and ask anything. The philosopher answers in their own voice, argues from their actual positions, and cites their real works. It covers Greek, Roman, medieval, Renaissance, early modern, 19th- and 20th-century Western thought, plus the Chinese and Indian traditions.

```
/nietzsche   What does the will to power mean for my startup?
/confucius   How should I lead my team?
/camus       Is this work actually meaningful?
/hanfeizi    How do I build a system that doesn't depend on good people?
/symposium   kant mill Is it ever right to lie?
```

## Install

**Claude Code (plugin, recommended):** run these inside Claude Code:

```
/plugin marketplace add BhackerJ/ai-philosophers
/plugin install philosophers@ai-philosophers
```

Plugin skills are namespaced, so you call them as `/philosophers:nietzsche`, `/philosophers:laozi`, and so on. Update later with `/plugin marketplace update ai-philosophers`.

**Claude Code (plain skills):** gives you short names like `/nietzsche`:

```bash
git clone https://github.com/BhackerJ/ai-philosophers
cd ai-philosophers
bash install.sh
```

Restart Claude Code. Every philosopher is available as a `/slash` command. To install only a few: `bash install.sh socrates kant laozi`. Re-running the script updates existing installs.

> **Note:** versions of `install.sh` before 1.1.0 stopped after the first skill (only `/aquinas` got installed). If that happened to you, pull and run it again.

**OpenClaw:** one command, all 42 philosophers, switch anytime:

```bash
clawhub install philosopher-pack
```

Then use `/philosophers` to browse and select, or `/philosophers socrates` to activate directly.

## Philosophers

### Ancient Greece & Rome

| Skill | Philosopher | Tradition | Known For |
|---|---|---|---|
| `/socrates` | Socrates (469–399 BC) | Greek | Dialectic method, "I know that I know nothing" |
| `/plato` | Plato (428–348 BC) | Greek | Theory of Forms, the Republic, the cave |
| `/aristotle` | Aristotle (384–322 BC) | Greek | Logic, ethics, politics, biology — the system-builder |
| `/epicurus` | Epicurus (341–270 BC) | Hellenistic | Pleasure as absence of pain, friendship, ataraxia |
| `/seneca` | Seneca (c. 4 BC–65 AD) | Roman Stoic | Letters to Lucilius, the shortness of life, anger |
| `/epictetus` | Epictetus (c. 50–135 AD) | Roman Stoic | Born a slave; the dichotomy of control, the Enchiridion |
| `/marcus_aurelius` | Marcus Aurelius (121–180 AD) | Roman Stoic | Meditations, duty, impermanence, the view from above |

### Medieval

| Skill | Philosopher | Tradition | Known For |
|---|---|---|---|
| `/aquinas` | Thomas Aquinas (1225–1274) | Scholastic | Five Ways, faith + reason, natural law |

### Renaissance & Early Modern

| Skill | Philosopher | Tradition | Known For |
|---|---|---|---|
| `/machiavelli` | Niccolò Machiavelli (1469–1527) | Florentine | The Prince, virtù and fortuna, republics, realpolitik |
| `/hobbes` | Thomas Hobbes (1588–1679) | British | Leviathan, "war of all against all", the social contract |
| `/descartes` | René Descartes (1596–1650) | French | Cogito ergo sum, mind-body dualism, method of doubt |
| `/spinoza` | Baruch Spinoza (1632–1677) | Dutch | God or Nature, determinism, the intellectual love of God |
| `/locke` | John Locke (1632–1704) | British | Natural rights, blank slate, limited government |
| `/leibniz` | Gottfried Leibniz (1646–1716) | German | Monads, pre-established harmony, best of all possible worlds |
| `/hume` | David Hume (1711–1776) | Scottish | Skepticism, causation, the problem of induction |
| `/rousseau` | Jean-Jacques Rousseau (1712–1778) | Swiss-French | General will, noble savage, natural education |

### German Idealism & 19th Century

| Skill | Philosopher | Tradition | Known For |
|---|---|---|---|
| `/kant` | Immanuel Kant (1724–1804) | German | Categorical imperative, Critique of Pure Reason |
| `/hegel` | G.W.F. Hegel (1770–1831) | German | Dialectics, Absolute Spirit, history as unfolding reason |
| `/schopenhauer` | Arthur Schopenhauer (1788–1860) | German | Will and representation, pessimism, aesthetic redemption |
| `/mill` | John Stuart Mill (1806–1873) | British | Utilitarianism, On Liberty, higher pleasures, women's rights |
| `/marx` | Karl Marx (1818–1883) | German | Historical materialism, class struggle, alienation, Capital |
| `/kierkegaard` | Søren Kierkegaard (1813–1855) | Danish | Leap of faith, three stages, the individual before God |
| `/nietzsche` | Friedrich Nietzsche (1844–1900) | German | Will to power, eternal recurrence, the Übermensch |

### 20th Century

| Skill | Philosopher | Tradition | Known For |
|---|---|---|---|
| `/wittgenstein` | Ludwig Wittgenstein (1889–1951) | Austrian-British | Language games, meaning as use, whereof one cannot speak |
| `/heidegger` | Martin Heidegger (1889–1976) | German | Being and Time, Dasein, authenticity, technology |
| `/sartre` | Jean-Paul Sartre (1905–1980) | French | Existence precedes essence, radical freedom, bad faith |
| `/beauvoir` | Simone de Beauvoir (1908–1986) | French | The Second Sex, ethics of ambiguity, "one becomes a woman" |
| `/arendt` | Hannah Arendt (1906–1975) | German-American | Totalitarianism, the banality of evil, action and plurality |
| `/camus` | Albert Camus (1913–1960) | French-Algerian | Absurdism, revolt, one must imagine Sisyphus happy |
| `/foucault` | Michel Foucault (1926–1984) | French | Power/knowledge, genealogy, discipline and punish |

---

### Chinese Tradition

| Skill | Philosopher | School | Known For |
|---|---|---|---|
| `/confucius` | Confucius (551–479 BC) | Confucian | Ren, li, the gentleman, ritual propriety |
| `/sunzi` | Sun Tzu / Sunzi (c. 544–496 BC) | Military strategist | The Art of War, winning without fighting, know yourself and the enemy |
| `/mozi` | Mozi / Mo Di (470–391 BC) | Mohist | Universal love, anti-warfare, utilitarian ethics |
| `/laozi` | Laozi (6th–4th c. BC) | Daoist | Tao Te Ching, wu wei, the nameless way |
| `/mencius` | Mencius / Mengzi (372–289 BC) | Confucian | Human nature is good, the four sprouts, benevolent rule |
| `/zhuangzi` | Zhuangzi (369–286 BC) | Daoist | Butterfly dream, relativity of perspectives, radical freedom |
| `/xunzi` | Xunzi (310–235 BC) | Confucian | Human nature is evil, ritual as transformation |
| `/hanfeizi` | Han Feizi (280–233 BC) | Legalist | Law + technique + power, realpolitik, institutional design |
| `/wang_yangming` | Wang Yangming (1472–1529) | Neo-Confucian | Unity of knowledge and action, innate moral knowledge |

### Indian Tradition

| Skill | Philosopher | School | Known For |
|---|---|---|---|
| `/buddha` | Siddhartha Gautama (563–483 BC) | Buddhist | Four Noble Truths, Eightfold Path, impermanence |
| `/nagarjuna` | Nagarjuna (150–250 AD) | Madhyamaka | Sunyata (emptiness), two truths, the middle way |
| `/shankara` | Adi Shankaracharya (788–820 AD) | Advaita Vedanta | Brahman = Atman, maya, non-dualism |

---

## Debates: `/symposium`

Put 2–4 philosophers in a room and give them a question:

```
/symposium kant mill Is it ever right to lie?
/symposium mencius xunzi Is human nature good or evil?
/symposium machiavelli confucius How should a leader treat their people?
/symposium epicurus epictetus seneca What does a happy life need?
```

Each speaker gives an opening statement, they argue back and forth for two rounds by name, give closing lines, and the host ends with a short neutral summary of where they really disagree. On OpenClaw, use `/philosophers debate kant mill Is it ever right to lie?`.

## Usage

Each philosopher:
- Responds entirely in character
- References their actual works naturally
- Stays within their historical knowledge: ask them about something modern and they'll ask you to describe it, then reason about it from their own principles
- Steps out of character if you sincerely ask whether you're talking to an AI, or if you seem to be in real distress
- Responds in whatever language you write in

**Ask anything:**

```
/marcus_aurelius  I keep getting distracted. What would you do?
/hanfeizi         How should I structure my company so it doesn't depend on any one person?
/epicurus         Is buying a bigger house going to make me happier?
/marx             What do you think of remote work and gig economy?
/shankara         What is the self?
```

**Cross-tradition questions work well too:**

```
/confucius  Mozi argues that universal love is better than your graduated love. How do you respond?
/mozi       Confucius says ritual is essential. Why do you disagree?
```

## FAQ

**Can Claude role-play a philosopher accurately?**
Each persona is a written brief covering the philosopher's voice, 8–10 core positions, key works with dates, and rules about what they could and couldn't know. That keeps answers grounded in what the philosopher actually argued instead of generic "wise" filler. It's still a language model: check quotes against the primary texts before citing them.

**What happens if I ask about something modern, like AI or startups?**
The philosopher doesn't pretend to know it. They ask you to describe it, then reason about it from their own principles, the way Aristotle might analyze a company as a kind of household or polis.

**How is this different from Character.AI or a custom GPT?**
It runs inside your coding agent (Claude Code or OpenClaw), with no account or app. It's plain Markdown you can read and edit, it's MIT-licensed, and every persona is grounded in specific works rather than a personality sketch.

**Does it work in other languages?**
Yes. Each philosopher replies in the language you write in, including Chinese, German, French, and Japanese.

**Will it stay in character no matter what?**
Almost. A philosopher steps out of character if you sincerely ask whether you're talking to an AI, or if you seem to be in real distress. In that case it responds directly and points you toward real help.

**Can I make philosophers debate each other?**
Yes: `/symposium mencius xunzi Is human nature good?` stages a full debate with opening statements, rebuttals, and a neutral summary. You can also ask one philosopher about another's view, e.g. `/mencius Xunzi says human nature is evil. Answer him.`

**Which philosophers are included?**
Socrates, Plato, Aristotle, Epicurus, Seneca, Epictetus, Marcus Aurelius, Aquinas, Machiavelli, Hobbes, Descartes, Spinoza, Locke, Leibniz, Hume, Rousseau, Kant, Hegel, Schopenhauer, Mill, Marx, Kierkegaard, Nietzsche, Wittgenstein, Heidegger, Sartre, Simone de Beauvoir, Hannah Arendt, Camus, Foucault, Confucius, Sun Tzu, Mozi, Laozi, Mencius, Zhuangzi, Xunzi, Han Feizi, Wang Yangming, the Buddha, Nagarjuna, and Shankara.

## How It Works

Each philosopher is a [Claude Code skill](https://code.claude.com/docs/en/skills) — a `SKILL.md` file with a structured system prompt covering voice, philosophical positions, key works, and behavioral rules. No RAG, no fine-tuning. Pure prompt engineering.

## Contributing

New philosophers welcome. Follow the existing `SKILL.md` format:
- `name`, `description`, `triggers`, `argument-hint`, `disable-model-invocation: true` frontmatter
- **Identity & Voice** — how they speak, what they sound like
- **Core Philosophical Positions** — 8–10 key positions with brief explanations
- **Key Works** — actual titles and dates
- **Behavioral Rules** — persona constraints, what to emphasize, how to end responses

`<name>/SKILL.md` is the source of truth. After adding or editing one, regenerate the OpenClaw pack copies:

```bash
bash scripts/sync-personas.sh
```

Open a PR. Suggestions for next additions: Augustine, Montaigne, Avicenna, Ibn Khaldun, Dogen, Zhu Xi, Voltaire, Nishida Kitaro.

## License

MIT
