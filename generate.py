# Generates index.html and posts/entry-1..8.html
# Run once: python3 generate.py  (safe to re-run; overwrites pages)

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
</head>
<body>
<header class="site"><div class="wrap">
  <div class="brand">
    <a href="{home}">SDG&nbsp;7 · ENERGY PROJECT</a>
    <span>MOHAMMED O. ALOTAIBI</span>
  </div>
</div></header>
"""

FOOT = """<footer class="site"><div class="wrap" style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:.6rem;">
  <span>Individual Project · 2026</span>
  <span>Built for assessment — SDG 7: Affordable and Clean Energy</span>
</div></footer>
</body>
</html>
"""

def charge(stage):
    # 5 bars, filled up to stage number (0 = intro/reflection style)
    bars = "".join(f'<i class="{"on" if i < stage else ""}"></i>' for i in range(5))
    return f'<span class="charge">{bars}</span>'

ENTRIES = [
    dict(n=1, stage=1, stage_label="STAGE 1 · SDG RESEARCH",
        title="Powering Everything: What SDG 7 Actually Asks",
        desc="The goal, its targets and indicators — and why energy sits underneath every other SDG.",
        sections="""
<h2>What SDG 7 says</h2>
<div class="todo">Summarise SDG 7 in your own words. Cover targets 7.1 (universal access), 7.2 (renewable share), 7.3 (double efficiency improvement), 7.a and 7.b. Cite the official UN SDG 7 page.</div>
<p>[Your text here]</p>

<h2>The indicators — how progress is measured</h2>
<div class="todo">List the key indicators: 7.1.1 % population with electricity access, 7.1.2 % with clean cooking, 7.2.1 renewable share of final energy, 7.3.1 energy intensity. Add the latest global figures from the UN Tracking SDG 7 report.</div>
<p>[Your text here]</p>

<h2>Why this goal, why now</h2>
<div class="todo">One or two paragraphs on why you chose SDG 7 and how it connects to your context in Saudi Arabia (Vision 2030, rising demand, cooling loads).</div>
<p>[Your text here]</p>
"""),
    dict(n=2, stage=1, stage_label="STAGE 1 · THE ENERGY NEED",
        title="The Need: Saudi Arabia's Energy Picture",
        desc="Regional demand, global gaps — the scale of the problem SDG 7 is trying to solve.",
        sections="""
<h2>The global gap</h2>
<div class="todo">How many people still lack electricity access globally? What share of world energy is renewable? Use the latest IEA / UN Tracking SDG 7 figures with the year stated.</div>
<p>[Your text here]</p>

<h2>The regional picture: Saudi Arabia</h2>
<div class="todo">Cover: total electricity consumption (TWh/yr), peak demand driven by summer cooling, per-capita consumption vs world average, and Vision 2030's 50% renewable electricity target. Cite Saudi Electricity Company / IEA / Our World in Data.</div>
<p>[Your text here]</p>

<figure>
  <img src="../assets/IMG-demand-chart.png" alt="Chart of Saudi electricity demand">
  <figcaption>FIG 2.1 — [Replace with a demand chart you make; state the data source and year]</figcaption>
</figure>
"""),
    dict(n=3, stage=2, stage_label="STAGE 2 · CURRENT SYSTEM",
        title="The Current System: A Grid Built on Oil and Gas",
        desc="Consumption, generation mix and CO₂ — with the numbers worked out, not just quoted.",
        sections="""
<h2>Generation mix today</h2>
<div class="todo">State the current Saudi mix (roughly gas + oil-fired steam/gas turbines, small but growing solar). Give the % split and the source year.</div>
<p>[Your text here]</p>

<h2>The carbon cost — my calculation</h2>
<div class="todo">Do a worked calculation. Example structure: annual generation (TWh) × grid emission factor (kg CO₂/kWh) = annual CO₂. Show every step and state where each number came from. This is what earns marks in "technical reasoning, data and calculations".</div>
<div class="calc"><span class="label">Worked example — replace with your verified numbers</span>
Annual generation      = [X] TWh = [X]&times;10⁹ kWh<br>
Grid emission factor   = [Y] kg CO₂ / kWh  (source: [ ])<br>
Annual CO₂            = [X]&times;10⁹ &times; [Y] = [Z] Mt CO₂ / year
</div>

<h2>Technical and economic strengths</h2>
<div class="todo">Be fair to the current system: dispatchable 24/7 power, existing infrastructure, low domestic fuel cost. A one-sided assessment loses marks on "weighing trade-offs".</div>
<p>[Your text here]</p>
"""),
    dict(n=4, stage=2, stage_label="STAGE 2 · FUTURE ALTERNATIVE",
        title="The Alternative: Utility-Scale Solar in the Desert",
        desc="Sudair, NEOM and the economics of photovoltaics — trade-offs included.",
        sections="""
<h2>Why solar fits this region</h2>
<div class="todo">Solar irradiance in Saudi Arabia (kWh/m²/day), land availability, and flagship projects — Sudair PV plant (capacity, cost per kWh from its PPA), Al Shuaibah, NEOM green hydrogen. Verify capacities and record-low tariff figures with sources.</div>
<p>[Your text here]</p>

<h2>Cost comparison — my calculation</h2>
<div class="calc"><span class="label">LCOE comparison — replace with your verified numbers</span>
Solar PPA price (Sudair)    = [A] $/kWh  (source: [ ])<br>
Gas/oil generation cost     = [B] $/kWh  (source: [ ])<br>
Avoided CO₂ per kWh        = [Y] kg  →  [ ] Mt/yr if [ ] TWh switched
</div>

<h2>Honest trade-offs</h2>
<div class="todo">Intermittency and night-time demand, storage cost, dust soiling on panels, water for cleaning, land use, and the transition cost for an oil-based economy. Then your reasoned judgement: what mix makes sense by 2030?</div>
<p>[Your text here]</p>
"""),
    dict(n=5, stage=3, stage_label="STAGE 3 · PRACTICAL ACTIVITY",
        title="The Audit: Measuring My Own Load",
        desc="A hands-on home energy audit with a power meter — real readings, real CO₂.",
        sections="""
<h2>Method</h2>
<div class="todo">Describe your setup: which meter/smart plug, which devices (AC, router, Raspberry Pi server, fridge, TV...), measurement period (24h recommended), and how you logged readings. Include a dated photo of the meter in use.</div>
<p>[Your text here]</p>

<figure>
  <img src="../assets/IMG-meter-photo.jpg" alt="Power meter measuring an appliance">
  <figcaption>FIG 5.1 — Measurement setup, [date]. [Device], reading [W].</figcaption>
</figure>

<h2>Results</h2>
<table>
  <tr><th>Device</th><th>Power (W)</th><th>Hours/day</th><th>kWh/day</th><th>kWh/month</th></tr>
  <tr><td>[Air conditioner]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
  <tr><td>[Router]</td><td>[ ]</td><td>24</td><td>[ ]</td><td>[ ]</td></tr>
  <tr><td>[Home server]</td><td>[ ]</td><td>24</td><td>[ ]</td><td>[ ]</td></tr>
  <tr><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
</table>

<h2>Linking it back</h2>
<div class="calc"><span class="label">From my sockets to the grid</span>
My monthly total        = [ ] kWh<br>
&times; grid factor [Y] kg/kWh = [ ] kg CO₂ / month<br>
If supplied by solar    = ~[ ] kg CO₂ avoided / month
</div>
<div class="todo">Connect the audit to Entries 3–4: what % could efficiency cut (SDG target 7.3)? Which single change saves most?</div>
<p>[Your text here]</p>
"""),
    dict(n=6, stage=4, stage_label="STAGE 4 · ETHICS & EQUITY",
        title="Who Pays, Who Benefits: Ethics of the Transition",
        desc="Energy justice — affordability, workers, and fairness between generations.",
        sections="""
<h2>The framework</h2>
<div class="todo">Name a recognised framework and use it explicitly — the Energy Justice framework (distributional / procedural / recognition justice) works well, or the IEEE/engineering code of ethics. The brief requires referencing a recognised framework, so cite it properly.</div>
<p>[Your text here]</p>

<h2>Applying it</h2>
<div class="todo">Distributional: who gets affordable power, subsidy reform impact on low-income households. Procedural: who decides the energy mix. Recognition: workers in the oil sector, future generations, regional neighbours without Saudi solar resources.</div>
<p>[Your text here]</p>

<h2>My position</h2>
<div class="todo">A short, reasoned personal judgement — what would a fair transition look like here? Tie it back to SDG 7's word "for all".</div>
<p>[Your text here]</p>
"""),
    dict(n=7, stage=5, stage_label="STAGE 5 · AWARENESS ACTIVITY",
        title="The Session: Explaining It to Ten People",
        desc="What I presented, the quiz, the results — evidence that understanding happened.",
        sections="""
<h2>The session</h2>
<div class="todo">Who, where, when (exact date), how many participants (aim for 10). What you presented — a short version of Entries 1–5. Include dated photos. Do NOT publish names or faces without consent; consent forms go separately to the assessor, never on this blog.</div>
<p>[Your text here]</p>

<figure>
  <img src="../assets/IMG-session-photo.jpg" alt="Awareness session in progress">
  <figcaption>FIG 7.1 — Awareness session, [date, location]. [N] participants (faces blurred where requested).</figcaption>
</figure>

<h2>The quiz</h2>
<div class="todo">List the 5 questions you asked (before/after format is strong evidence: same quiz before and after your talk shows learning happened). Show score improvement.</div>
<p>[Your text here]</p>

<h2>Results</h2>
<table>
  <tr><th>Question</th><th>Correct before</th><th>Correct after</th></tr>
  <tr><td>Q1 — [ ]</td><td>[ ]/10</td><td>[ ]/10</td></tr>
  <tr><td>Q2 — [ ]</td><td>[ ]/10</td><td>[ ]/10</td></tr>
</table>
<p>[Your text here — what the numbers show about their understanding]</p>
"""),
    dict(n=8, stage=5, stage_label="CONCLUSION · REFLECTION",
        title="Reflection: What the Numbers Changed",
        desc="What I found, what surprised me, and what I now think about the 2030 energy mix.",
        sections="""
<h2>What the project showed</h2>
<div class="todo">Pull the thread through all five stages in 3–4 paragraphs: the goal, the gap, the comparison result, what your own audit proved at small scale, the ethical picture, and what your participants took away.</div>
<p>[Your text here]</p>

<h2>What surprised me</h2>
<p>[Your text here]</p>

<h2>Self-reflection</h2>
<div class="todo">Write this one carefully — you can reuse it directly as Slide 3 of your Moodle submission and it will come up in the viva. What would you do differently? What skills did you build?</div>
<p>[Your text here]</p>
"""),
]

REFS = """
<div class="refs">
<h2>References</h2>
<ol>
  <li>[Author/Org], "[Title]", [Year]. [URL]</li>
  <li>[Add every source you used in this entry — the rubric will look for referencing]</li>
</ol>
</div>
"""

# ---- Build post pages ----
for e in ENTRIES:
    n = e["n"]
    prev_link = f'<a href="entry-{n-1}.html">← Entry {n-1:02d}</a>' if n > 1 else '<a href="../index.html">← All entries</a>'
    next_link = f'<a href="entry-{n+1}.html">Entry {n+1:02d} →</a>' if n < 8 else '<a href="../index.html">Back to index →</a>'
    html = HEAD.format(title=f'{e["title"]} — SDG 7 Project', css="../assets/style.css", home="../index.html")
    html += f"""<main class="wrap">
<div class="post-head">
  <div class="meter">
    <span class="cell">ENTRY {n:02d}/08</span>
    <span class="cell">{e["stage_label"]}</span>
    {charge(e["stage"])}
  </div>
  <h1>{e["title"]}</h1>
  <div class="date">Published: [DATE — set the real date you publish]</div>
</div>
<article class="post">
{e["sections"]}
{REFS}
</article>
<nav class="pager">{prev_link}{next_link}</nav>
</main>
"""
    html += FOOT
    with open(f"posts/entry-{n}.html", "w") as f:
        f.write(html)

# ---- Build index ----
cards = ""
for e in ENTRIES:
    cards += f"""<div class="card">
  <div class="meter" style="border-top:none;">
    <span class="cell">ENTRY {e["n"]:02d}</span>
    <span class="cell">{e["stage_label"]}</span>
    {charge(e["stage"])}
  </div>
  <h2><a href="posts/entry-{e["n"]}.html">{e["title"]}</a></h2>
  <p>{e["desc"]}</p>
</div>
"""

index = HEAD.format(title="SDG 7 Project — Affordable and Clean Energy", css="assets/style.css", home="index.html")
index += f"""<main class="wrap">
<section class="hero">
  <h1>Can the desert that exports oil run on <em>sunlight</em>?</h1>
  <p class="lede">An eight-entry project blog assessing Saudi Arabia's current energy system against utility-scale solar, through the lens of UN Sustainable Development Goal 7 — with real measurements, real calculations, and a real audience.</p>
</section>
<section class="entries">
{cards}
</section>
</main>
"""
index += FOOT
with open("index.html", "w") as f:
    f.write(index)

print("Generated index.html and 8 posts.")
