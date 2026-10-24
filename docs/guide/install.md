# Install the skill

<nav class="page-language" aria-label="Language">
  <a href="/evidence-informed-design/guide/install.html" lang="en">English</a><span aria-hidden="true">/</span><a href="/evidence-informed-design/ja/guide/install.html" lang="ja">日本語</a>
</nav>

Install the complete skill bundle from the repository root. The installer places the skill in `~/.codex/skills/evidence-informed-design` by default and includes `SKILL.md`, `references/`, `agents/`, `LICENSE`, and `NOTICE.md`.

```powershell
uv run scripts/install_skill.py
```

To install under another skills parent directory, pass its path:

```powershell
uv run scripts/install_skill.py --destination "C:\path\to\skills"
```

## Use the skill

Ask Codex to apply the skill to a concrete page, slide, document, or chart:

```text
$evidence-informed-design を使って、この画面の情報のまとまりと強調を見直してください。
利用者の課題、根拠の種類、変更案、実物での確認範囲を分けて報告してください。
```

The skill starts with `references/evidence-map.md`. It then uses only the source notes needed for the current decision. The [research guide](/guide/research) summarizes those sources and their limits.

## Check a checkout

Repository maintainers can run the structural validator and unit tests from the repository root:

```powershell
uv run scripts/validate_repo.py
uv run python -m unittest discover -s tests
```