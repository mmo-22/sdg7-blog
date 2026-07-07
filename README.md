# SDG 7 Project Blog — deploy guide

Static blog for the Individual Project (SDG 7: Affordable and Clean Energy).
8 entries covering all 5 required stages. No build step — plain HTML + CSS.

## Deploy to GitHub Pages (5 minutes)

Option A — new repo (recommended, gives a clean link):
1. Create a public repo, e.g. `sdg7-project`
2. Push these files to the `main` branch
3. Repo → Settings → Pages → Source: `main` / root → Save
4. Blog appears at `https://<username>.github.io/sdg7-project/`

Option B — subfolder of your existing `mmo-22.github.io` repo:
copy this folder in as `/sdg7/` → link becomes `https://mmo-22.github.io/sdg7/`

## Workflow

- Each entry has amber dashed **TO DO** boxes with instructions.
  Write your content, then DELETE every `.todo` box before publishing.
- Replace `[ ... ]` placeholders everywhere (dates, numbers, sources).
- Put photos/charts in `assets/` using the filenames referenced in each
  entry (IMG-meter-photo.jpg etc.), or update the `<img src>` paths.
- `generate.py` rebuilds the pages from scratch — DO NOT re-run it after
  you start writing content, or it will overwrite your work. It's only
  there if you want to change the template structure before writing.

## Compliance checklist (from the assessment brief)

- [ ] All 5 stages covered (mapped in the entry meter strips)
- [ ] Calculations shown step-by-step with sources (Entries 3, 4, 5)
- [ ] Practical activity evidenced with dated photos (Entry 5)
- [ ] Ethics referenced to a recognized framework (Entry 6)
- [ ] Awareness session: ≥5 participants, dated photos, quiz shown (Entry 7)
- [ ] Consent forms submitted SEPARATELY to assessor — never published here
- [ ] No personal data of participants on the blog
- [ ] References list completed in every entry
- [ ] All TO DO boxes deleted
- [ ] Link tested in an incognito window before Moodle submission
