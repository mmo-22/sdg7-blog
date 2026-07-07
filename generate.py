# Generates index.html and posts/entry-1..8.html — full website layout
# Run once: python3 generate.py  (DO NOT re-run after writing content — it overwrites pages)

# Per-entry SVG motif icons (line art, drawn inline in banners and cards)
ICONS = {
 1: '<circle cx="32" cy="32" r="22" fill="none" stroke="#ffb020" stroke-width="2.5"/><circle cx="32" cy="32" r="13" fill="none" stroke="#3ec6de" stroke-width="2"/><circle cx="32" cy="32" r="4" fill="#ffb020"/>',
 2: '<path d="M12 50 V34 H22 V50 M27 50 V24 H37 V50 M42 50 V14 H52 V50" fill="none" stroke="#3ec6de" stroke-width="2.5"/><path d="M10 50 H54" stroke="#ffb020" stroke-width="2.5"/>',
 3: '<path d="M32 10 C24 22 20 28 20 36 a12 12 0 0 0 24 0 c0-8-4-14-12-26z" fill="none" stroke="#ffb020" stroke-width="2.5"/><path d="M32 28 c-3 5-5 7-5 10 a5 5 0 0 0 10 0 c0-3-2-5-5-10z" fill="#f2555a"/>',
 4: '<rect x="12" y="16" width="40" height="26" rx="2" fill="none" stroke="#3ec6de" stroke-width="2.5"/><path d="M12 29 H52 M25 16 V42 M39 16 V42" stroke="#3ec6de" stroke-width="1.5"/><path d="M32 42 V52 M24 52 H40" stroke="#ffb020" stroke-width="2.5"/>',
 5: '<path d="M14 44 a18 18 0 1 1 36 0" fill="none" stroke="#3ec6de" stroke-width="2.5"/><path d="M32 44 L42 26" stroke="#ffb020" stroke-width="3" stroke-linecap="round"/><circle cx="32" cy="44" r="3.5" fill="#ffb020"/>',
 6: '<path d="M32 12 V50 M20 50 H44" stroke="#ffb020" stroke-width="2.5"/><path d="M14 22 H50" stroke="#3ec6de" stroke-width="2.5"/><path d="M14 22 l-6 12 a8 6 0 0 0 12 0 z M50 22 l-6 12 a8 6 0 0 0 12 0 z" fill="none" stroke="#3ec6de" stroke-width="2"/>',
 7: '<circle cx="22" cy="22" r="6" fill="none" stroke="#3ec6de" stroke-width="2.5"/><circle cx="42" cy="22" r="6" fill="none" stroke="#ffb020" stroke-width="2.5"/><path d="M12 48 a10 10 0 0 1 20 0 M32 48 a10 10 0 0 1 20 0" fill="none" stroke="#3ec6de" stroke-width="2.5"/>',
 8: '<circle cx="32" cy="32" r="22" fill="none" stroke="#3ec6de" stroke-width="2.5"/><path d="M21 33 l8 8 14-18" fill="none" stroke="#ffb020" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>',
}

def icon(n, size=64):
    return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" aria-hidden="true">{ICONS[n]}</svg>'

def charge(stage):
    bars = "".join(f'<i class="{"on" if i < stage else ""}"></i>' for i in range(5))
    return f'<span class="charge">{bars}</span>'

NAV = """<nav class="topnav"><div class="wrap">
  <a class="logo" href="{home}"><span class="led"></span>SDG7<span class="dim">.PROJECT</span></a>
  <div class="links">
    <a href="{home}#project">The Project</a>
    <a href="{home}#entries">Entries</a>
    <a href="{home}#stages">Stages</a>
    <a href="{home}#author">Author</a>
  </div>
</div></nav>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
</head>
<body>
"""

FOOT = """<footer class="site"><div class="wrap">
  <span>INDIVIDUAL PROJECT · 2026</span>
  <span>SDG 7 — AFFORDABLE AND CLEAN ENERGY</span>
  <span class="clock" id="clk">--:--:--</span>
</div></footer>
<script>
(function(){var e=document.getElementById("clk");if(!e)return;
function t(){e.textContent=new Date().toLocaleTimeString("en-GB",{hour12:false})+" AST"}
t();setInterval(t,1000)})();
</script>
</body>
</html>
"""

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
    prev_link = f'<a href="entry-{n-1}.html">&larr; Entry {n-1:02d}</a>' if n > 1 else '<a href="../index.html#entries">&larr; All entries</a>'
    next_link = f'<a href="entry-{n+1}.html">Entry {n+1:02d} &rarr;</a>' if n < 8 else '<a href="../index.html#entries">Back to site &rarr;</a>'
    html = HEAD.format(title=f'{e["title"]} — SDG 7 Project', css="../assets/style.css")
    html += NAV.format(home="../index.html")
    html += f"""<div class="banner">
  <div class="wrap banner-in">
    <div class="banner-icon">{icon(n, 84)}</div>
    <div>
      <div class="crumb">MODULE {n:02d}/08 · {e["stage_label"]} {charge(e["stage"])}</div>
      <h1>{e["title"]}</h1>
      <div class="date">Published: [DATE — set the real date you publish]</div>
    </div>
  </div>
</div>
<main class="wrap">
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

# ---- Build index (website landing) ----
cards = ""
for e in ENTRIES:
    cards += f"""<a class="tile" href="posts/entry-{e["n"]}.html">
  <div class="tile-visual">{icon(e["n"], 72)}<span class="tile-id">{e["n"]:02d}</span></div>
  <div class="tile-body">
    <div class="tile-meta">{e["stage_label"]} {charge(e["stage"])}</div>
    <h3>{e["title"]}</h3>
    <p>{e["desc"]}</p>
  </div>
</a>
"""

STAGES = [
 ("01","SDG Research","Targets, indicators and the energy need — Entries 1–2"),
 ("02","System Assessment","Current grid vs solar, with calculations — Entries 3–4"),
 ("03","Practical Activity","Hands-on energy audit with a power meter — Entry 5"),
 ("04","Ethics & Equity","Energy justice framework applied — Entry 6"),
 ("05","Social Awareness","Session with 10 participants + quiz — Entry 7"),
]
stages_html = "".join(f"""<div class="stage">
  <div class="stage-n">{s[0]}</div>
  <div><h3>{s[1]}</h3><p>{s[2]}</p></div>
</div>""" for s in STAGES)

index = HEAD.format(title="SDG 7 Project — Affordable and Clean Energy", css="assets/style.css")
index += NAV.format(home="index.html")
index += f"""
<section class="hero-site">
  <div class="hero-art"><img src="assets/hero.svg" alt="Desert landscape with solar panels and a transmission tower under an amber sun"></div>
  <div class="wrap hero-copy">
    <div class="eyebrow">/// SDG 7 · AFFORDABLE AND CLEAN ENERGY · INDIVIDUAL PROJECT</div>
    <h1>Can the desert that exports oil<br>run on <span class="hl">sunlight</span>?</h1>
    <p class="lede">Assessing Saudi Arabia's oil-and-gas grid against utility-scale solar — with real measurements, worked calculations, and a real audience.</p>
    <div class="cta-row">
      <a class="btn btn-solar" href="#entries">Read the 8 entries</a>
      <a class="btn" href="#stages">The 5 stages</a>
    </div>
  </div>
</section>

<section class="stats"><div class="wrap stats-in">
  <div class="stat"><b>[ X ] TWh</b><span>KSA annual electricity — Entry 2</span></div>
  <div class="stat"><b>[ X ] Mt CO₂</b><span>Grid emissions computed — Entry 3</span></div>
  <div class="stat"><b>[ X ] $/kWh</b><span>Sudair solar tariff — Entry 4</span></div>
  <div class="stat"><b>10</b><span>Awareness participants — Entry 7</span></div>
</div></section>

<section id="project" class="section"><div class="wrap">
  <h2 class="sec-title">The Project</h2>
  <p class="sec-lede">This site documents an individual assessment project built around <b>UN Sustainable Development Goal 7</b>: ensuring access to affordable, reliable, sustainable and modern energy for all. Across eight entries it researches the goal, assesses the current Saudi energy system against a solar-powered alternative with data and calculations, evidences a hands-on energy audit, examines the ethics of the transition, and reports a live awareness session.</p>
  <div class="todo">Rewrite this paragraph in your own words after you finish the entries — it's the first thing the assessor reads.</div>
</div></section>

<section id="entries" class="section"><div class="wrap">
  <h2 class="sec-title">The Entries</h2>
  <div class="grid">
{cards}
  </div>
</div></section>

<section id="stages" class="section alt"><div class="wrap">
  <h2 class="sec-title">Five Assessment Stages</h2>
  <div class="stages">{stages_html}</div>
</div></section>

<section id="author" class="section"><div class="wrap author-in">
  <div class="author-badge">MA</div>
  <div>
    <h2 class="sec-title" style="margin-bottom:.3rem;">Mohammed O. Alotaibi</h2>
    <p class="sec-lede" style="margin:0;">IT specialist and engineering student, Al-Khobar, Saudi Arabia. [One or two more lines about you and this course.]</p>
  </div>
</div></section>
"""
index += FOOT
with open("index.html", "w") as f:
    f.write(index)

print("Generated website: index.html + 8 entry pages.")
