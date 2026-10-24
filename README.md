<div align="center">
  <img src="assets/logo.svg" alt="" width="112">
  <h1>Evidence-informed design</h1>
  <p>Research-grounded reviews for interfaces, slides, documents, and charts.</p>
</div>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/evidence-informed-design/actions/workflows/ci.yml"><img src="https://github.com/Sunwood-ai-labs/evidence-informed-design/actions/workflows/ci.yml/badge.svg" alt="CI status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Sunwood-ai-labs/evidence-informed-design" alt="MIT License"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ja.md">日本語</a>
</p>

<p align="center">
  <a href="https://sunwood-ai-labs.github.io/evidence-informed-design/">Read the published docs</a> · <a href="https://sunwood-ai-labs.github.io/evidence-informed-design/ja/">日本語ドキュメント</a>
</p>

Use this agent skill when important information is hard to find or relate. It helps you connect research and design decisions, then pair each proposed change with a check. It does not turn research into universal style rules.

## What the skill does

The review starts with the reader's task and the information they need. It then helps the agent:

- Check whether related items look related and unrelated items look distinct.
- Review hierarchy and visual competition in context.
- Keep information needed to act, such as labels, units, warnings, status, and sources.
- Separate research findings, practitioner guidance, design hypotheses, and observed results.
- Check a rendered result against the task and the states the change affects.

Use the skill for design reviews and creation work across web interfaces, slides, documents, and charts. It can propose a review when you provide a screenshot or source file, the intended reader, the task, and any constraints.

## Evidence and limits

The source notes distinguish what each reference measured from how the skill applies it:

- Wertheimer's 1923 paper discusses how people organize visual forms such as points, lines, and curves. Applying those ideas to a modern interface is a design inference.
- Nielsen's usability heuristics are review guidance. They do not measure the effect of a specific redesign.
- Rosenholtz, Li, and Nakano (2007) studied visual clutter and search in map images. Their results do not define a universal clutter score for interfaces or prove that removing elements improves a task.
- Tuch and colleagues (2012) studied aesthetic first impressions of company website screenshots. They did not measure task success, comprehension, conversion, or long-term satisfaction.

These sources do not establish universal limits for color counts, spacing, card counts, or corner radii. They also do not support blanket bans on gradients, centered text, cards, shadows, or rounded corners. Evaluate each choice by its role in the actual design. These sources do not define accessibility conformance criteria; check the applicable standard separately when compliance is in scope.

The detailed research notes in `references/` are currently in Japanese. Start with the [English guide](docs/index.md) or the [Japanese guide](docs/ja/index.md).

## Install the skill

Use Python 3.11 or newer with [uv](https://docs.astral.sh/uv/). From the repository root, run:

```sh
git clone https://github.com/Sunwood-ai-labs/evidence-informed-design.git
cd evidence-informed-design
uv run scripts/install_skill.py
```

The installer creates `evidence-informed-design` under `~/.codex/skills` by default. It copies `SKILL.md`, `agents/`, `references/`, `LICENSE`, and `NOTICE.md`. It does not copy the docs site, tests, or Git metadata.

To choose another skills parent directory, pass it with `--destination`. For example, in PowerShell:

```powershell
$skillsParent = Join-Path $env:USERPROFILE ".agents\skills"
uv run scripts/install_skill.py --destination $skillsParent
```

An identical existing installation is a no-op. The installer refuses a conflicting destination and has no overwrite option.

## Use the skill

Invoke `$evidence-informed-design` and describe the reader, their task, and the constraints. Provide the screenshot, source file, or other material to review when available.

```text
$evidence-informed-design
Review this dashboard. The main task is to identify overdue accounts and their next action. Keep the reporting period, units, update time, status, and required warnings. Separate what you observe from the design hypothesis, then suggest a check for the change.
```

The skill produces the requested artifact or an ordered set of proposed changes. It names the evidence behind a decision and reports what the available checks did and did not establish.

## Examples

These examples show how to keep research, inference, and verification separate:

- [Review a dashboard for overdue work](examples/dashboard-priority-review.md)
- [Review a website's first impression](examples/website-first-impression.md)

Both examples use fictional screens and do not report user-study results.

## Check the repository

Run these commands from the repository root. Repository tools require Python 3.11 or newer and `uv`. The docs build requires Node.js 24 and `npm`. Install the docs dependencies before building the site.

```sh
uv run scripts/validate_repo.py
uv run python -m unittest discover -s tests -v
npm --prefix docs ci
npm --prefix docs run docs:build
```

## Repository map

| Path | Contents |
| --- | --- |
| `SKILL.md` | Main workflow and evidence-handling rules. |
| `references/` | Japanese research notes, source links, and design checks. |
| `docs/` | English and Japanese practical guides. |
| `examples/` | Fictional, worked design reviews. |
| `agents/openai.yaml` | Agent catalog metadata. |
| `scripts/` | Installation and repository validation tools. |
| `tests/` | Automated repository checks. |
| `assets/logo.svg` | Project logo used by the README and docs. |
| `.github/workflows/ci.yml` | Continuous integration workflow. |

## Sources

Start with the [evidence map](references/evidence-map.md), which links each design question to the relevant source note and summarizes its limits. The [design and verification guide](references/design-decisions.md) shows how to turn a finding into a reviewable hypothesis and task check.

- [Wertheimer research note](references/wertheimer.md)
- [Nielsen and Rosenholtz research note](references/nielsen-rosenholtz.md)
- [Tuch et al. research note](references/tuch.md)

The notes link to the cited papers and records. They document access limits and distinguish source findings from applications to design work.

## License and attribution

The repository's original instructions, summaries, examples, documentation, code, and artwork are under the MIT License. Cited papers, translations, articles, and external sites retain their respective rights. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) for the license and source attributions.
