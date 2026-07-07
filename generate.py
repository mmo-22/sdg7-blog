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
        desc="The goal, its targets and indicators — from the UN 2030 Agenda down to Bahrain's own energy plans.",
        sections="""
<h2>What SDG 7 says</h2>
<div class="todo">RUBRIC: Subject Knowledge (30). Summarise SDG 7 in your own words. Cover targets 7.1 (universal access), 7.2 (renewable share), 7.3 (double efficiency improvement), 7.a and 7.b. Cite the official UN SDG 7 page.</div>
<p>[Your text here]</p>

<h2>The indicators — how progress is measured</h2>
<div class="todo">List the key indicators: 7.1.1 % population with electricity access, 7.1.2 % with clean cooking, 7.2.1 renewable share of final energy, 7.3.1 energy intensity. Add the latest global figures from the UN Tracking SDG 7 report with the year stated.</div>
<p>[Your text here]</p>

<h2>From global frameworks to Bahrain's initiatives</h2>
<div class="todo">RUBRIC: the A-grade descriptor says "clearly connects the SDG to global frameworks and local (regional) initiatives" — this section earns that. Global: UN 2030 Agenda, Paris Agreement. Local: Bahrain's National Renewable Energy Action Plan (NREAP — verify its renewable targets for 2025 and 2035), the National Energy Efficiency Action Plan (NEEAP), and Bahrain's net-zero 2060 commitment. Cite the Sustainable Energy Authority (sea.gov.bh).</div>
<p>[Your text here]</p>
"""),
    dict(n=2, stage=1, stage_label="STAGE 1 · THE ENERGY NEED",
        title="The Need: Bahrain's Energy Picture",
        desc="A small island with big per-capita consumption — the regional and global need SDG 7 addresses.",
        sections="""
<h2>The global gap</h2>
<div class="todo">How many people still lack electricity access globally? What share of world energy is renewable? Use the latest IEA / UN Tracking SDG 7 figures with the year stated.</div>
<p>[Your text here]</p>

<h2>The regional picture: Bahrain</h2>
<div class="todo">RUBRIC: "regional and global energy needs" must both appear. Cover: Bahrain's annual electricity consumption (TWh/yr), near-total dependence on natural gas for generation, summer air-conditioning peak demand, per-capita electricity consumption among the highest in the world, and subsidised tariffs. Sources: Electricity and Water Authority (EWA) annual report, IEA country profile, Our World in Data. State the year for every number.</div>
<p>[Your text here]</p>

<figure>
  <img src="../assets/IMG-demand-chart.png" alt="Chart of Bahrain electricity demand growth">
  <figcaption>FIG 2.1 — Bahrain electricity consumption over time. Source: [ ], [year].</figcaption>
</figure>
"""),
    dict(n=3, stage=2, stage_label="STAGE 2 · CURRENT SYSTEM",
        title="The Current System: An Island Grid Built on Gas",
        desc="Bahrain's gas-fired power stations — consumption, emissions and a worked CO₂ calculation.",
        sections="""
<h2>Generation today</h2>
<div class="todo">Describe Bahrain's current fleet: gas-fired combined-cycle and thermal stations (Al Dur, Al Ezzel, Riffa, Al Hidd — verify names, capacities and shares from EWA). State that generation is effectively ~100% natural gas and where the gas comes from (Khuff field). Include a simple mix chart or table.</div>
<p>[Your text here]</p>

<h2>The carbon cost — my calculation</h2>
<div class="todo">RUBRIC: A-grade requires "sound data" and calculations. Show every step and the source of every number.</div>
<div class="calc"><span class="label">Worked example — replace with your verified numbers</span>
Annual generation      = [X] TWh = [X]&times;10⁹ kWh  (source: EWA [year])<br>
Grid emission factor   = [Y] kg CO₂ / kWh  (source: [ ])<br>
Annual CO₂            = [X]&times;10⁹ &times; [Y] = [Z] Mt CO₂ / year
</div>

<h2>Technical and economic strengths</h2>
<div class="todo">Be fair to the current system: dispatchable 24/7 power for extreme summer loads, high-efficiency combined-cycle plants, existing infrastructure, domestic gas. Then the weaknesses: emissions, exposure to gas depletion and future import cost, zero diversification. RUBRIC: "weighs technical, economic and environmental trade-offs".</div>
<p>[Your text here]</p>
"""),
    dict(n=4, stage=2, stage_label="STAGE 2 · FUTURE ALTERNATIVE",
        title="The Alternative: Solar on a Small Island",
        desc="Rooftops, car parks and landfill solar — the economics and the honest limits, ending in a justified judgement.",
        sections="""
<h2>Why solar — and why it's harder in Bahrain</h2>
<div class="todo">Bahrain has excellent irradiance but very little land — that tension is your most original angle. Cover: solar resource (kWh/m²/yr — verify), and Bahrain-specific deployment: rooftop net-metering (EWA scheme), car-park canopies, the Askar landfill solar project, university/mall rooftop projects, and utility plants in Sakhir (verify status and capacities from the Sustainable Energy Authority).</div>
<p>[Your text here]</p>

<h2>Cost comparison — my calculation</h2>
<div class="calc"><span class="label">LCOE comparison — replace with your verified numbers</span>
Solar LCOE (regional benchmark) = [A] $/kWh  (source: IRENA [year])<br>
Gas generation cost             = [B] $/kWh  (source: [ ])<br>
Avoided CO₂ per kWh            = [Y] kg  →  [ ] kt/yr if [ ] GWh switched
</div>

<h2>Honest trade-offs</h2>
<div class="todo">Intermittency vs evening AC peak, storage cost, dust soiling, land scarcity (why Bahrain can't copy Saudi mega-projects), grid integration limits. Compare against NREAP's own targets: is 10% by 2035 ambitious or timid?</div>
<p>[Your text here]</p>

<h2>My justified judgement</h2>
<div class="todo">RUBRIC KEYWORD: the A-descriptor says "reaches a well-justified judgement on how well each system meets regional and global energy needs sustainably". Write a clear verdict: what mix should Bahrain target by 2035 and why — grounded in YOUR numbers from this entry and Entry 3. This paragraph is also your strongest viva answer.</div>
<p>[Your text here]</p>
"""),
    dict(n=5, stage=3, stage_label="STAGE 3 · PRACTICAL ACTIVITY",
        title="The Audit: Measuring My Own Load",
        desc="A hands-on home energy audit with a power meter — real readings, real CO₂, linked back to the assessment.",
        sections="""
<h2>Method</h2>
<div class="todo">RUBRIC: "record the method and the results, and link them back". Describe your setup: which meter/smart plug, which devices (AC, fridge, router, TV...), measurement period (24h recommended), and how you logged readings. Include a dated photo of the meter in use.</div>
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
  <tr><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td><td>[ ]</td></tr>
</table>

<h2>Linking it back</h2>
<div class="calc"><span class="label">From my sockets to the grid</span>
My monthly total        = [ ] kWh<br>
&times; grid factor [Y] kg/kWh = [ ] kg CO₂ / month<br>
If supplied by solar    = ~[ ] kg CO₂ avoided / month
</div>
<div class="todo">Connect the audit to Entries 3–4: what % could efficiency cut (SDG target 7.3)? Which single change saves most? How does your AC share compare to Bahrain's national summer peak story from Entry 2?</div>
<p>[Your text here]</p>
"""),
    dict(n=6, stage=4, stage_label="STAGE 4 · ETHICS & SOCIAL DIMENSIONS",
        title="Who Pays, Who Benefits: Ethics of the Transition",
        desc="Energy justice applied to Bahrain — and the social dimension: who is affected and why engagement matters.",
        sections="""
<h2>The framework</h2>
<div class="todo">RUBRIC: "referenced to a recognized framework" — name it explicitly. The Energy Justice framework (distributional / procedural / recognition justice) works well. Cite an academic source (e.g. Sovacool &amp; Dworkin) properly.</div>
<p>[Your text here]</p>

<h2>Applying it to Bahrain</h2>
<div class="todo">Distributional: subsidised tariffs — who benefits, what happens to low-income and expatriate-worker households if subsidies reform. Procedural: who decides the energy mix and can citizens participate. Recognition: future generations inheriting the gas-depletion risk. Trade-offs and equity of access, per the brief.</div>
<p>[Your text here]</p>

<h2>The social dimension</h2>
<div class="todo">RUBRIC (brief, Stage 4): "who is affected, the community need addressed, and why engagement matters". Name the affected groups concretely, the community need your awareness session serves, and why public engagement changes outcomes — this paragraph also justifies Entry 7.</div>
<p>[Your text here]</p>

<h2>My position</h2>
<div class="todo">A short, reasoned personal judgement — what would a fair transition look like in Bahrain? Tie it back to SDG 7's phrase "for all".</div>
<p>[Your text here]</p>
"""),
    dict(n=7, stage=5, stage_label="STAGE 5 · AWARENESS ACTIVITY",
        title="The Session: Explaining It to Ten People",
        desc="What I presented, the quiz, the results — and the ethics evidence the rubric marks line by line.",
        sections="""
<h2>The session</h2>
<div class="todo">RUBRIC split: Quality 5 · Ethics 2 · Scope 2 · Collaboration 1. Scope: at least 5 people, 10 recommended — state the exact number, date, place. Describe what you presented (a short version of Entries 1–5). Include dated photos. Do NOT publish names or faces without consent; consent forms go separately to the assessor, never on this site.</div>
<p>[Your text here]</p>

<figure>
  <img src="../assets/IMG-session-photo.jpg" alt="Awareness session in progress">
  <figcaption>FIG 7.1 — Awareness session, [date, location]. [N] participants (faces blurred where requested).</figcaption>
</figure>

<h2>Ethics of the activity — evidenced</h2>
<div class="todo">RUBRIC Ethics (2): state explicitly, in one short paragraph each: (1) consent obtained before participation — forms submitted separately to the assessor; (2) feedback kept anonymous and protected; (3) participation voluntary; (4) safeguarding applied if any minors or vulnerable people were present. Collaboration (1): if anyone helped organise, name the role and state clearly what YOUR individual contribution was.</div>
<p>[Your text here]</p>

<h2>The quiz</h2>
<div class="todo">List the questions you asked. A before/after quiz (same 5 questions before and after your talk) is the strongest evidence of understanding. Include anonymised responses.</div>
<p>[Your text here]</p>

<h2>Results and reflection on understanding</h2>
<table>
  <tr><th>Question</th><th>Correct before</th><th>Correct after</th></tr>
  <tr><td>Q1 — [ ]</td><td>[ ]/10</td><td>[ ]/10</td></tr>
  <tr><td>Q2 — [ ]</td><td>[ ]/10</td><td>[ ]/10</td></tr>
</table>
<div class="todo">RUBRIC (brief): "a short reflection on how well the group understood" is explicitly required — write 4–6 sentences on what they grasped, what confused them, and what you'd explain differently.</div>
<p>[Your text here]</p>
"""),
    dict(n=8, stage=5, stage_label="CONCLUSION · REFLECTION",
        title="Reflection: What the Numbers Changed",
        desc="Pulling the five stages together — and the self-reflection that becomes Slide 3 of the presentation.",
        sections="""
<h2>What the project showed</h2>
<div class="todo">Pull the thread through all five stages in 3–4 paragraphs: the goal, Bahrain's gap, the comparison verdict, what your own audit proved at small scale, the ethical picture, and what your participants took away.</div>
<p>[Your text here]</p>

<h2>What surprised me</h2>
<p>[Your text here]</p>

<h2>Self-reflection</h2>
<div class="todo">Write this carefully — it becomes Slide 3 of the Moodle submission and feeds the viva. What would you do differently? What skills did you build?</div>
<p>[Your text here]</p>

<h2>Preparing for the viva</h2>
<div class="todo">Q&amp;A is 20/100. Prepare answers (don't publish them — keep private notes) for: Why solar and not wind/nuclear for Bahrain? What limits solar on a small island? Defend your grid emission factor. What is the difference between targets 7.2 and 7.3? What would change your judgement in Entry 4? You may delete this section before publishing.</div>
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
    <p class="lede">Assessing Bahrain's gas-fired grid against solar power — with real measurements, worked calculations, and a real audience.</p>
    <div class="cta-row">
      <a class="btn btn-solar" href="#entries">Read the 8 entries</a>
      <a class="btn" href="#stages">The 5 stages</a>
    </div>
  </div>
</section>

<section class="stats"><div class="wrap stats-in">
  <div class="stat"><b>[ X ] TWh</b><span>Bahrain annual electricity — Entry 2</span></div>
  <div class="stat"><b>[ X ] Mt CO₂</b><span>Grid emissions computed — Entry 3</span></div>
  <div class="stat"><b>10% by 2035</b><span>NREAP renewable target — Entry 4</span></div>
  <div class="stat"><b>10</b><span>Awareness participants — Entry 7</span></div>
</div></section>

<section id="project" class="section"><div class="wrap">
  <h2 class="sec-title">The Project</h2>
  <p class="sec-lede">This site documents an individual assessment project built around <b>UN Sustainable Development Goal 7</b>: ensuring access to affordable, reliable, sustainable and modern energy for all. Across eight entries it researches the goal, assesses Bahrain's current gas-fired energy system against a solar-powered alternative with data and calculations, evidences a hands-on energy audit, examines the ethics of the transition, and reports a live awareness session.</p>
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
  <div class="author-badge">FA</div>
  <div>
    <h2 class="sec-title" style="margin-bottom:.3rem;">Faisal Alrugaiti</h2>
    <p class="sec-lede" style="margin:0;">[Your program and institution — one or two lines about you and this course.]</p>
  </div>
</div></section>
"""
index += FOOT
with open("index.html", "w") as f:
    f.write(index)

print("Generated website: index.html + 8 entry pages.")
