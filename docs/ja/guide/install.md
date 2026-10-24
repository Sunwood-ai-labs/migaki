# スキルをインストールする

<nav class="page-language" aria-label="言語">
  <a href="/migaki/guide/install.html" lang="en">English</a><span aria-hidden="true">/</span><a href="/migaki/ja/guide/install.html" lang="ja">日本語</a>
</nav>

リポジトリのルートから、スキル一式をインストールします。既定では `~/.codex/skills/migaki` に配置します。`SKILL.md`、`references/`、`agents/`、`LICENSE`、`NOTICE.md` が含まれます。

```powershell
uv run scripts/install_skill.py
```

別のスキル親ディレクトリへ入れる場合は、パスを指定します。

```powershell
uv run scripts/install_skill.py --destination "C:\path\to\skills"
```

## スキルを使う

Codex に具体的なWeb画面、スライド、文書、図表を提示して、スキルを使うよう依頼します。

```text
$migaki を使って、この画面の情報のまとまりと強調を見直してください。
利用者の課題、根拠の種類、変更案、実物での確認範囲を分けて報告してください。
```

スキルは `references/evidence-map.md` を最初に読み、今回の判断に必要な資料だけを使います。[研究と根拠のガイド](/ja/guide/research)で出典と限界を確認できます。

## チェックアウトを検証する

リポジトリの保守担当者は、ルートから構造検証とユニットテストを実行できます。

```powershell
uv run scripts/validate_repo.py
uv run python -m unittest discover -s tests
```