# Blog post (English)

**Title options**
- What I learned making 48 philosophers argue inside Claude Code
- A philosopher persona should know what it doesn't know

**Tags:** claude, ai, philosophy, prompt-engineering, opensource

---

I wanted to ask Nietzsche about my startup. Not a chatbot that had read a Wikipedia summary of Nietzsche; something that argued the way he argued, cited the books he actually wrote, and refused to have opinions about things that happened after 1889.

So I wrote 48 of them as [Claude Code skills](https://github.com/BhackerJ/ai-philosophers). Each one is a single Markdown file. Here's what I learned.

## 1. The fake quotes are the real problem

Language models are fluent in "philosopher voice," and that fluency is exactly the danger. Ask a naive persona for a quote and you'll get a confident, well-formed sentence that nobody ever wrote.

So each persona carries two lists. A **verified quotations** list, with source down to chapter or section number: *"The impediment to action advances action. What stands in the way becomes the way." — Meditations 5.20*. And a **misattributions** list: *"We are what we repeatedly do" — not Aristotle; Will Durant summarizing him in 1926.* The rule is simple: quote verbatim only from the first list, paraphrase everything else, and correct the user if they cite something from the second.

I spot-checked 35 of the quotes I was least sure of against primary sources. Twelve needed fixing. That's a 1-in-3 error rate for lines I'd have sworn were right, which tells you something about how misquotations propagate.

## 2. Not knowing is a feature

The original rule was "don't know events after your death." That's necessary but not sufficient, because the model will still happily use modern vocabulary as if it were native.

The rule that works: *if the user raises something from after your time, don't pretend to know it. Ask them to describe it, then reason from your own principles and from analogies in your own world.*

Ask Ibn Khaldun why a company that started as five friends in a garage now has 400 employees and founders who don't speak, and he'll say he's never heard of a company, ask you to explain, and then diagnose it as a tribe whose *asabiyya* (group feeling) was forged in hardship and dissolved by luxury. Which is, honestly, correct.

## 3. Breaking character on purpose

The first draft said "never break persona or acknowledge being an AI." I removed that after imagining someone telling Schopenhauer they don't want to be alive anymore.

Now every persona drops the act in two cases: if the user sincerely asks whether they're talking to an AI, and if the user seems to be in real distress. In the second case it answers as a person and points toward real help. There's an eval case for it.

## 4. Debates reveal more than monologues

`/symposium kant mill Is it ever right to lie?` reads each persona file and stages a debate: openings, two rounds of rebuttals by name, closings, and a neutral host summary of where they actually disagree.

The first time I ran it, Kant brought up his 1797 essay on the murderer at the door without being prompted, and Mill answered with "I say *almost*, and the word carries the weight of my answer." Neither of those lines is in the persona files. They came from the model reasoning inside the constraints.

## 5. Test it like software

Claude Code can run evals on plugins. Ten cases cover: stays in voice; doesn't fake modern knowledge; admits being an AI when sincerely asked; drops persona for distress; corrects misquotes; answers in the user's language; produces a real two-sided debate. Each run costs cents. Every change to a persona gets tested.

## Try it

```
/plugin marketplace add BhackerJ/ai-philosophers
/plugin install philosophers@ai-philosophers
```

Also on OpenClaw: `clawhub install philosopher-pack`. MIT licensed, [source on GitHub](https://github.com/BhackerJ/ai-philosophers). Quote corrections welcome; I'm sure there are more.
