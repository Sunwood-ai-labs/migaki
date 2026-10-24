<div align="center">
  <img src="assets/logo.svg" alt="" width="112">
  <h1>MIGAKI（ミガキ）</h1>
  <p>インターフェース、スライド、文書、図表を研究知見に基づいてレビューします。</p>
</div>

<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/migaki/actions/workflows/ci.yml"><img src="https://github.com/Sunwood-ai-labs/migaki/actions/workflows/ci.yml/badge.svg" alt="CIの状態"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Sunwood-ai-labs/migaki" alt="MITライセンス"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ja.md">日本語</a>
</p>

<p align="center">
  <a href="https://sunwood-ai-labs.github.io/migaki/">英語のドキュメント</a> · <a href="https://sunwood-ai-labs.github.io/migaki/ja/">日本語のドキュメント</a>
</p>

作成やレビューを始めるときは、[設計チェックリスト](https://sunwood-ai-labs.github.io/migaki/ja/guide/checklist.html)から該当項目を選び、完成した成果物で確認します。

重要な情報が見つけにくい、または情報同士の関係が分かりにくいときに使うエージェントスキルです。研究知見と設計判断を結び、提案した変更を確かめる方法まで示します。研究知見をあらゆる場面に当てはまる作風の規則には変えません。

## このスキルでできること

レビューでは読み手の課題と必要な情報を最初に確認します。そのうえで、次の点を調べます。

- 関連する項目がまとまり、無関係な項目が区別されているか。
- 情報の優先順位や視覚的な競合が、実際の利用状況に合っているか。
- ラベル、単位、警告、状態、出典など、判断や操作に必要な情報が残っているか。
- 研究結果、実務上の助言、設計上の仮説、実際に確認した結果が区別されているか。
- 表示した成果物を課題と照らし、変更が影響する状態も確認できるか。

Webインターフェース、スライド、文書、図表のレビューや作成に使えます。スクリーンショットや元ファイル、想定読者、課題、制約を渡すと、内容に沿って提案します。

## 根拠と限界

参照資料では、各研究が測ったことと、スキルが実務へ応用する内容を分けています。

- Wertheimerの1923年の論文は、点、線、曲線などの視覚的なまとまりを論じています。現代のインターフェースへ適用する判断は、設計上の推論です。
- Nielsenのユーザビリティ・ヒューリスティックは、レビューに使う助言です。特定の画面を改修した効果を測ったものではありません。
- Rosenholtz、Li、Nakano（2007）は、地図画像の視覚的クラッターと探索を調べています。インターフェース全般に使えるクラッターの基準値や、項目の削減で課題が改善するという因果関係は示していません。
- Tuchら（2012）は企業サイトのスクリーンショットに対する美的な第一印象を調べています。課題の達成、理解、成約、長期的な満足度は測っていません。

これらの資料から、色数、余白、カード数、角丸の半径などの一律の基準は導けません。グラデーション、中央揃え、カード、影、角丸を一律に禁止する根拠にもなりません。それぞれが実際のデザインで果たす役割を確かめてください。この4つの資料はアクセシビリティの適合基準も定めていません。適合性の確認が必要な場合は、対象となる規格を別途確認してください。

詳しい調査ノートは現在日本語で [`references/`](references/) にあります。実務ガイドは[英語版](docs/index.md)と[日本語版](docs/ja/index.md)を用意しています。

## スキルをインストールする

Python 3.11以降と[uv](https://docs.astral.sh/uv/)を使います。リポジトリのルートで次を実行してください。

```sh
git clone https://github.com/Sunwood-ai-labs/migaki.git
cd migaki
uv run scripts/install_skill.py
```

既定では `~/.codex/skills` の下に `migaki` を作成します。インストーラーは `SKILL.md`、`agents/`、`references/`、`LICENSE`、`NOTICE.md` をコピーします。以前の名前でインストール済みのスキルはMIGAKIと併用できます。旧版を削除するかどうかは利用者が選べます。

別のスキル格納先を指定する場合は `--destination` に親ディレクトリを渡します。PowerShellでは次のように指定できます。

```powershell
$skillsParent = Join-Path $env:USERPROFILE ".agents\skills"
uv run scripts/install_skill.py --destination $skillsParent
```

同じ内容がすでにあれば何も変更しません。競合する内容がある場合は処理を止めます。上書きオプションはありません。ドキュメントサイト、テスト、Gitのメタデータはコピーしません。

## スキルを使う

`$migaki` を呼び出し、読み手、課題、制約を説明してください。可能であれば、レビューするスクリーンショットや元ファイルも渡します。

```text
$migaki
このダッシュボードをレビューしてください。主な課題は、期限を過ぎたアカウントと次の対応を見つけることです。対象期間、単位、更新時刻、状態、必要な警告は残してください。観察した内容と設計上の仮説を分け、変更を確かめる方法も提案してください。
```

依頼に応じて、成果物または優先度順の修正案を返します。判断の根拠と、実施した確認で分かったこと・分からなかったことも示します。

## 例

研究知見、推論、検証を分ける例を用意しています。

- [ダッシュボードで期限超過の作業を見つける](examples/dashboard-priority-review.md)
- [Webサイトの第一印象をレビューする](examples/website-first-impression.md)

作例本文は英語のみです。どちらも架空の画面を扱い、ユーザー調査の結果を報告していません。

## リポジトリを確認する

次のコマンドをリポジトリのルートで実行します。リポジトリのツールにはPython 3.11以降と `uv` が必要です。サイトのビルドにはNode.js 24と `npm` が必要です。ビルドの前に、ドキュメントの依存関係をインストールします。

```sh
uv run scripts/validate_repo.py
uv run python -m unittest discover -s tests -v
npm --prefix docs ci
npm --prefix docs run docs:build
```

## リポジトリの構成

| パス | 内容 |
| --- | --- |
| `SKILL.md` | 主な手順と根拠の扱い方。 |
| `references/` | 日本語の研究ノート、出典リンク、設計チェックリスト。 |
| `docs/` | 英語と日本語の実務ガイド。 |
| `examples/` | 架空の画面を使ったレビュー例。 |
| `agents/openai.yaml` | エージェント一覧用のメタデータ。 |
| `scripts/` | インストールとリポジトリ確認のツール。 |
| `tests/` | リポジトリの自動確認。 |
| `assets/logo.svg` | READMEとドキュメントで使うロゴ。 |
| `.github/workflows/ci.yml` | 継続的インテグレーション。 |

## 出典

まず[根拠の対応表](references/evidence-map.md)を確認してください。設計上の問いに対応する資料と、その限界をまとめています。[設計と検証の手順](references/design-decisions.md)では、研究知見から確認可能な仮説と課題を組み立てる方法を説明しています。

- [Wertheimerの調査ノート](references/wertheimer.md)
- [NielsenとRosenholtzの調査ノート](references/nielsen-rosenholtz.md)
- [Tuchらの調査ノート](references/tuch.md)

調査ノートには原典や書誌記録へのリンクがあります。アクセスできなかった資料も記録し、原典の結果と設計への応用を区別しています。

## ライセンスと出典の帰属

このリポジトリで作成した指示、要約、例、ドキュメント、コード、画像はMITライセンスの対象です。引用・参照した論文、翻訳、記事、外部サイトには、それぞれの権利が適用されます。ライセンスと出典の帰属については、[LICENSE](LICENSE) と [NOTICE.md](NOTICE.md) を確認してください。
