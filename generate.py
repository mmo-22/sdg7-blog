# Simple blog generator — plain student-style layout
# Run once: python3 generate.py  (DO NOT re-run after writing content)

def charge(stage):
    return ""  # not used in simple layout

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<header>
  <h1 class="site-title"><a href="{home}">My SDG 7 Project</a></h1>
  <p class="site-sub">Energy, Environment and Sustainability (EN8905) — Individual Project</p>
</header>
"""

FOOT = """<footer>
  <p>Faisal Alrugaiti — EN8905 Individual Project, 2026</p>
</footer>
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
  <img src="../assets/IMG-demand-chart.png" alt="Bar chart: Bahrain peak demand 3.4 GW in 2016 projected to 6.5 GW in 2030">
  <figcaption>FIG 2.1 — Bahrain's summer peak demand, 2016 actual vs 2030 projection. Source: Electricity &amp; Water master plan (via Enerdata). [Verify against the latest EWA report and update if needed.]</figcaption>
</figure>
<div class="todo">Useful verified numbers for this entry: per-capita gas-fired generation in Bahrain was the HIGHEST in the world in 2023 at about 22,986 kWh/person (Ember, Global Electricity Review 2025). Verify and cite before using.</div>
"""),
    dict(n=3, stage=2, stage_label="STAGE 2 · CURRENT SYSTEM",
        title="The Current System: An Island Grid Built on Gas",
        desc="Bahrain's gas-fired power stations — consumption, emissions and a worked CO₂ calculation.",
        sections="""
<h2>Generation today</h2>
<div class="todo">Describe Bahrain's current fleet: gas-fired combined-cycle and thermal stations (Al Dur, Al Ezzel, Riffa, Al Hidd — verify names, capacities and shares from EWA). State that generation is effectively ~100% natural gas and where the gas comes from (Khuff field). Include a simple mix chart or table.</div>
<p>[Your text here]</p>

<figure>
  <img src="../assets/IMG-mix-chart.png" alt="Bar chart: 99.9 percent of Bahrain electricity comes from natural gas">
  <figcaption>FIG 3.1 — Bahrain electricity generation by source. Source: World Bank / IEA, 2022 (natural gas = 99.85%). [Re-verify the latest year.]</figcaption>
</figure>

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
<div class="todo">Intermittency vs evening AC peak, storage cost, dust soiling, land scarcity (why Bahrain can't copy Saudi mega-projects), grid integration limits. Compare against NREAP's own targets — note they were REVISED in 2023 (roughly: 255 MW renewable capacity by 2025 and 710 MW by 2035, but only ~18 MW installed by end of 2024, per Enerdata). Is that ambitious or timid? The chart below is your strongest evidence.</div>
<p>[Your text here]</p>

<figure>
  <img src="../assets/IMG-targets-chart.png" alt="Bar chart comparing 18 MW installed renewables with 255 MW and 710 MW targets">
  <figcaption>FIG 4.1 — Bahrain's renewable capacity: installed (end 2024) vs NREAP targets. Sources: NREAP (2017, rev. 2023); installed capacity via Enerdata. [Verify against sea.gov.bh before submission.]</figcaption>
</figure>

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

for e in ENTRIES:
    n = e["n"]
    prev_link = f'<a href="entry-{n-1}.html">&larr; Previous entry</a>' if n > 1 else '<a href="../index.html">&larr; Home</a>'
    next_link = f'<a href="entry-{n+1}.html">Next entry &rarr;</a>' if n < 8 else '<a href="../index.html">Home &rarr;</a>'
    html = HEAD.format(title=f'Entry {n}: {e["title"]}', css="../assets/style.css", home="../index.html")
    html += f"""<main>
<p class="meta">Entry {n} of 8 &middot; {e["stage_label"].title()}</p>
<h1>{e["title"]}</h1>
<p class="meta">Published: [DATE — set the real date you publish]</p>
<article>
{e["sections"]}
{REFS}
</article>
<p class="pager">{prev_link} &nbsp;|&nbsp; {next_link}</p>
</main>
"""
    html += FOOT
    open(f"posts/entry-{n}.html", "w").write(html)

items = ""
for e in ENTRIES:
    items += f"""<li>
  <span class="meta">Entry {e["n"]} &middot; {e["stage_label"].title()}</span><br>
  <a href="posts/entry-{e["n"]}.html"><b>{e["title"]}</b></a><br>
  {e["desc"]}
</li>
"""

index = HEAD.format(title="My SDG 7 Project — Affordable and Clean Energy", css="assets/style.css", home="index.html")
index += f"""<main>
<h1>Can an island that runs on gas switch to sunlight?</h1>
<p>Welcome to my project blog for EN8905. Across eight entries I research <b>UN Sustainable
Development Goal 7</b> (Affordable and Clean Energy), assess Bahrain's current gas-fired
electricity system against a solar alternative using data and my own calculations, carry out
a hands-on energy audit at home, look at the ethics of the energy transition, and share the
results of an awareness session I ran with a small group.</p>
<div class="todo">Rewrite this welcome paragraph in your own words when the entries are done.</div>
<h2>The entries</h2>
<ol class="entry-list">
{items}
</ol>
<h2>About me</h2>
<p>My name is Faisal Alrugaiti. [Your programme and one or two lines about yourself.]</p>
</main>
"""
index += FOOT
open("index.html", "w").write(index)
print("Simple site generated.")
