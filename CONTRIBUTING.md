# Contributing

Contributions should help readers make a design decision they can explain and check. Keep research findings, practitioner guidance, design hypotheses, and observed results separate.

## Start with the reader's task

- Read `SKILL.md` and the [evidence map](references/evidence-map.md) before changing the review method.
- Read only the source notes that apply to the change.
- State the intended reader, their task, the medium, and the constraints in new examples.
- Keep labels, units, source details, warnings, and state information when people need them to act.

## Keep claims within the evidence

- Name the source and the outcome it measured. Do not present a heuristic as an experiment.
- Mark an application to a different medium, audience, or task as a design hypothesis.
- Pair a design hypothesis with a check that could support or reject it.
- Do not turn the cited studies into universal rules about color, spacing, cards, alignment, gradients, or other styles.
- Do not report a screenshot review as a user study or claim a usability improvement without a task check.

## Add examples and documentation

- Label invented screens and observations as illustrative. Do not add raw user conversations or private screenshots.
- Keep the section order aligned between `README.md` and `README.ja.md`.
- Keep English and Japanese guides structurally parallel, while writing each language naturally.
- Preserve citations and access limits when changing the research notes.

## Verify the change

Run the relevant checks from the repository root. Repository tools require Python 3.11 or newer and `uv`. The docs build requires Node.js 24 and `npm`. Install the documentation dependencies before building the docs.

```sh
uv run scripts/validate_repo.py
uv run python -m unittest discover -s tests -v
npm --prefix docs ci
npm --prefix docs run docs:build
```

## Preserve attribution

The MIT License applies to original material in this repository. Papers, translations, articles, figures, and other third-party material keep their own rights. Before adding third-party content, check its terms and record the source and attribution in `NOTICE.md`. Do not add complete papers or unlicensed figure reproductions.

## Describe your change

In a pull request, state the reader problem, the files changed, the sources behind any research claim, and the checks you ran. Label untested design claims as hypotheses and list any remaining limits.
