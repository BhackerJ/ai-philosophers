#!/usr/bin/env python3
"""Generate docs/ (the GitHub Pages site) from the SKILL.md files.

    python3 scripts/build-site.py

Reads every <name>/SKILL.md, groups philosophers by the sections in README.md,
and writes docs/index.html, docs/sitemap.xml, docs/robots.txt, docs/llms.txt.
Run it after adding or editing a philosopher; commit the output.
"""
import html
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://bhackerj.github.io/ai-philosophers/"
REPO = "https://github.com/BhackerJ/ai-philosophers"
SKIP = {"philosopher-pack", "symposium"}


def frontmatter_desc(text):
    m = re.search(r"^description: \|\n((?:  .*\n)+)", text, re.M)
    d = " ".join(l.strip() for l in m.group(1).splitlines())
    return re.sub(r"\s*Invoke with /[a-z_]+( to [^.]*)?\.$", "", d).strip()


def readme_groups():
    """Return [(section_title, [(slug, name, tradition, known_for)])] from README tables."""
    text = (ROOT / "README.md").read_text()
    groups, current = [], None
    for line in text.splitlines():
        if line.startswith("### "):
            current = (line[4:].strip(), [])
            groups.append(current)
        elif current and line.startswith("| `/"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            slug = cells[0].strip("`/")
            current[1].append((slug, cells[1], cells[2], cells[3]))
    return [g for g in groups if g[1]]


def main():
    DOCS.mkdir(exist_ok=True)
    descs = {}
    for f in sorted(ROOT.glob("*/SKILL.md")):
        if f.parent.name not in SKIP:
            descs[f.parent.name] = frontmatter_desc(f.read_text())
    groups = readme_groups()
    listed = {s for _, rows in groups for s, *_ in rows}
    assert listed == set(descs), f"README tables and SKILL.md dirs differ: {listed ^ set(descs)}"
    total = len(descs)

    excerpt = (ROOT / "docs" / "excerpt-kant-mill.md").read_text()
    excerpt_html = md_to_html(excerpt)

    cards = []
    for title, rows in groups:
        items = "".join(
            f'<li class="card" id="{s}"><h4><code>/{s}</code> <span>{html.escape(name)}</span></h4>'
            f'<p class="trad">{html.escape(trad)}</p><p>{html.escape(descs[s])}</p></li>'
            for s, name, trad, _ in rows
        )
        cards.append(f'<section class="group"><h3>{html.escape(title)}</h3><ul class="cards">{items}</ul></section>')

    ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "AI Philosophers",
        "applicationCategory": "DeveloperApplication",
        "operatingSystem": "Any",
        "url": SITE,
        "codeRepository": REPO,
        "license": "https://opensource.org/licenses/MIT",
        "description": f"{total} philosopher personas for Claude Code and OpenClaw. Each answers in the philosopher's own voice, cites real works, and corrects misquotations. Includes /symposium debates.",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "featureList": [f"/{s}" for s in sorted(descs)] + ["/symposium"],
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in FAQ
        ],
    }
    faq_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in FAQ)

    page = TEMPLATE.format(
        total=total,
        cards="".join(cards),
        excerpt=excerpt_html,
        faq=faq_html,
        ld=json.dumps(ld, ensure_ascii=False),
        faq_ld=json.dumps(faq_ld, ensure_ascii=False),
        site=SITE,
        repo=REPO,
    )
    (DOCS / "index.html").write_text(page)
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{SITE}</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>\n</urlset>\n"
    )
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    shutil.copy(ROOT / "llms.txt", DOCS / "llms.txt")
    (DOCS / ".nojekyll").write_text("")
    print(f"docs/ built: {total} philosophers")


def md_to_html(md):
    out, in_p = [], []
    def flush():
        if in_p:
            out.append("<p>" + inline(" ".join(in_p)) + "</p>")
            in_p.clear()
    for line in md.splitlines():
        if line.startswith("## "):
            flush(); out.append(f"<h4>{inline(line[3:])}</h4>")
        elif line.startswith("# "):
            flush()
        elif line.strip() == "---":
            flush()
        elif not line.strip():
            flush()
        else:
            in_p.append(line)
    flush()
    return "\n".join(out)


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


FAQ = [
    ("Can Claude role-play a philosopher accurately?",
     "Each persona is a written brief covering the philosopher's voice, core positions, key works with dates, a list of verified quotations with sources, and rules about what they could and couldn't know. The persona quotes only from the verified list and paraphrases everything else. It's still a language model: check quotes against the primary texts before citing them."),
    ("What happens if I ask about something modern, like AI or startups?",
     "The philosopher doesn't pretend to know it. They ask you to describe it, then reason about it from their own principles, the way Ibn Khaldun analyzes a startup as a tribe losing its group feeling."),
    ("How is this different from Character.AI or a custom GPT?",
     "It runs inside your coding agent (Claude Code or OpenClaw), with no account or app. It's plain Markdown you can read and edit, MIT-licensed, and every persona is grounded in specific works rather than a personality sketch."),
    ("Does it work in Chinese or other languages?",
     "Yes. Each philosopher replies in the language you write in. The Chinese philosophers carry their quotations in the original."),
    ("Will it stay in character no matter what?",
     "Almost. A philosopher steps out of character if you sincerely ask whether you're talking to an AI, or if you seem to be in real distress. In that case it responds directly and points you toward real help."),
    ("Can I make philosophers debate each other?",
     "Yes. /symposium kant mill Is it ever right to lie? stages a full debate with opening statements, two rounds of rebuttals, closings, and a neutral summary of where they disagree."),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Philosophers: {total} philosopher personas for Claude Code</title>
<meta name="description" content="Talk with Socrates, Nietzsche, Confucius, Laozi, Arendt and {total} philosophers inside Claude Code or OpenClaw. Each answers in their own voice, cites real works, and corrects misquotations. Free, MIT, one-command install.">
<link rel="canonical" href="{site}">
<meta property="og:type" content="website">
<meta property="og:title" content="AI Philosophers: {total} philosopher personas for Claude Code">
<meta property="og:description" content="Talk with {total} philosophers in their own voice inside Claude Code. Stage debates with /symposium. Free and open source.">
<meta property="og:url" content="{site}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="text/plain" href="{site}llms.txt" title="llms.txt">
<script type="application/ld+json">{ld}</script>
<script type="application/ld+json">{faq_ld}</script>
<!-- Analytics: paste a Cloudflare Web Analytics or GoatCounter snippet here. -->
<style>
:root{{--bg:#faf8f3;--fg:#1f1d1a;--muted:#6b6560;--line:#e3ded4;--accent:#8b2f1f;--card:#fff;--code:#f1ede4}}
@media(prefers-color-scheme:dark){{:root{{--bg:#16140f;--fg:#ebe6dc;--muted:#a09a90;--line:#2d2922;--accent:#e2876f;--card:#1f1c16;--code:#262219}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,"Times New Roman",serif}}
main{{max-width:960px;margin:0 auto;padding:0 16px 64px}}
header{{padding:64px 0 32px;border-bottom:1px solid var(--line)}}
h1{{font-size:2.6rem;line-height:1.1;margin:0 0 12px}}
h2{{font-size:1.7rem;margin:48px 0 12px}}
h3{{font-size:1.25rem;margin:32px 0 8px;color:var(--accent)}}
.lead{{font-size:1.2rem;max-width:720px}}
.muted{{color:var(--muted)}}
pre,code{{font:15px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
pre{{background:var(--code);padding:14px 16px;border-radius:8px;overflow-x:auto}}
.install pre{{white-space:pre-wrap;word-break:break-all}}
code{{background:var(--code);padding:1px 5px;border-radius:4px}}
pre code{{padding:0;background:none}}
.install{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}}
.install div{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px}}
.install h4{{margin:0 0 8px}}
.cards{{list-style:none;padding:0;margin:0;display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}}
.card h4{{margin:0;font-size:1.05rem}}
.card h4 span{{font-weight:normal;color:var(--muted);margin-left:6px}}
.card .trad{{margin:2px 0 6px;font-size:.85rem;color:var(--accent)}}
.card p{{margin:0;font-size:.95rem}}
.excerpt{{background:var(--card);border-left:4px solid var(--accent);padding:8px 24px;margin:16px 0;border-radius:0 10px 10px 0}}
.excerpt h4{{margin:20px 0 4px;color:var(--accent);font-size:1rem;text-transform:uppercase;letter-spacing:.04em}}
details{{border-bottom:1px solid var(--line);padding:10px 0}}
summary{{cursor:pointer;font-weight:bold}}
footer{{margin-top:64px;padding-top:24px;border-top:1px solid var(--line);color:var(--muted);font-size:.9rem}}
a{{color:var(--accent)}}
nav a{{margin-right:18px}}
</style>
</head>
<body>
<main>
<header>
<h1>AI Philosophers</h1>
<p class="lead"><strong>{total} philosopher personas for <a href="https://claude.ai/code">Claude Code</a> and <a href="https://openclaw.ai">OpenClaw</a>.</strong> Type <code>/socrates</code> or <code>/confucius</code> and ask anything. Each philosopher answers in their own voice, argues from their documented positions, cites their real works, and corrects you when you quote something they never said. Free and open source.</p>
<nav><a href="#install">Install</a><a href="#philosophers">Philosophers</a><a href="#debate">Debates</a><a href="#faq">FAQ</a><a href="{repo}">GitHub</a></nav>
</header>

<pre><code>/nietzsche    What does the will to power mean for my startup?
/confucius    How should I lead my team?
/ibn_khaldun  Our garage startup is now 400 people. What's happening to us?
/symposium    kant mill Is it ever right to lie?</code></pre>

<h2 id="install">Install</h2>
<div class="install">
<div><h4>Claude Code (plugin)</h4><pre><code>/plugin marketplace add BhackerJ/ai-philosophers
/plugin install philosophers@ai-philosophers</code></pre><p class="muted">Skills are namespaced: <code>/philosophers:nietzsche</code>.</p></div>
<div><h4>Claude Code (short names)</h4><pre><code>git clone {repo}
cd ai-philosophers
bash install.sh</code></pre><p class="muted">Gives you <code>/nietzsche</code>, <code>/laozi</code>, etc.</p></div>
<div><h4>OpenClaw</h4><pre><code>clawhub install philosopher-pack</code></pre><p class="muted">Then <code>/philosophers socrates</code>, or <code>/philosophers debate kant mill ...</code></p></div>
</div>

<h2 id="debate">A debate, unedited</h2>
<p class="muted">Output of <code>/symposium kant mill Is it ever right to lie?</code>, exactly as generated. Excerpt.</p>
<div class="excerpt">{excerpt}</div>

<h2 id="philosophers">The {total} philosophers</h2>
{cards}

<h2 id="faq">FAQ</h2>
{faq}

<h2>How it works</h2>
<p>Each philosopher is a <a href="https://code.claude.com/docs/en/skills">Claude Code skill</a>: one <code>SKILL.md</code> file with the philosopher's voice, core positions, key works, a list of verified quotations with sources (plus famous misattributions to correct), and behavioral rules. No fine-tuning, no retrieval. The repo ships an eval suite that checks personas stay in voice, don't fake knowledge of modern things, admit to being an AI when sincerely asked, and drop the persona for someone in distress.</p>

<footer>MIT licensed. <a href="{repo}">Source on GitHub</a> · <a href="llms.txt">llms.txt</a> · New philosophers welcome, open a PR.</footer>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    main()
