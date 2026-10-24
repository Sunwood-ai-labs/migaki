# 研究と根拠の範囲

<nav class="page-language" aria-label="言語">
  <a href="/migaki/guide/research.html" lang="en">English</a><span aria-hidden="true">/</span><a href="/migaki/ja/guide/research.html" lang="ja">日本語</a>
</nav>

このスキルは、視覚的なまとまりや点検の判断に4つの出典を使います。出典は同じ方法で調べられたものではなく、支持できる主張も異なります。現代の画面に応用する前に、各出典が扱った範囲を確認してください。

## 出典の対応表

| 出典と種類 | 判断に使えること | この出典だけでは言えないこと |
| --- | --- | --- |
| [Wertheimer（1923）](https://psychclassics.yorku.ca/Wertheimer/Forms/forms.htm)。知覚の組織化に関する研究。閲覧できるページは1938年の英訳再掲です。 | 近接、類似、方向などのまとまりの手がかりと、内容上の関係が一致しているか。 | 現代UIに最適な余白、普遍的な手がかりの順位、事業上の成果。 |
| [Nielsenのユーザビリティ・ヒューリスティクス](https://www.nngroup.com/articles/ten-usability-heuristics/)。レビューの経験則です。 | 課題に関係しない情報が、必要な情報と競合していないか。 | 特定の画面の変更でタスク成績が上がるか。ヒューリスティック評価はユーザーのタスク実験ではありません。 |
| [Rosenholtz、Li、Nakano（2007）](https://doi.org/10.1167/7.2.17)。視覚的クラッターの研究です。 | 研究で扱った地図上の視覚探索と、特徴の変動などの画像統計量との関係。 | すべての画面に使えるクラッター値、色数の上限、ユーザビリティのしきい値。 |
| [Tuchほか（2012）](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/)。Webサイトの第一印象に関する研究です。 | 研究条件内で、サイト画像の視覚的複雑さや種類らしさが直後の美しさ評定とどう関係したか。 | 操作のしやすさ、理解、長期満足、購入、または「簡素な画面ほど常によい」という規則。 |

## 根拠を適切な強さで使う

### 研究結果

研究結果には、それを得た課題、素材、参加者、測定項目、条件があります。知見は調べた範囲に結び付けて扱います。地図の探索やWebサイト静止画の短時間評定は、アプリ上の操作課題を直接予測しません。

### 経験則

経験則は、設計を見直すための問いを与えます。対象画面の結果を測ったものではありません。Nielsenの第8項は、無関係な情報が課題と競合しないかを問います。必要なラベル、状態、警告、操作を取り除く指示ではありません。

### 応用仮説

応用仮説では、出典と一つの変更案を結び付けます。変更案と一緒に確認方法を決めます。たとえば、入力欄のラベルが隣の値と結び付いて見える場合、ラベルを本来の値のそばに移し、表示したフォームで関係が読めるかを確かめます。

### 観察結果

観察結果では、対象の成果物と状態を示し、実際に見たことや操作したことを報告します。ソースコードの確認だけでは表示を確かめられません。画面表示の確認だけでは、対象利用者が内容を理解するかは分かりません。

## どの出典にも当てはまる限界

この4出典から、色、書体、カード、ボタンの数、角丸、余白の比率は決まりません。グラデーション、中央揃え、影、装飾も一律に禁止されません。媒体と課題に合わせて選び、成果物で確認してください。

美しさ、情報の見つけやすさ、理解、タスクの成功、好みは別の評価項目です。第一印象がよいという結果だけでは、タスク成績や事業上の成果は分かりません。

## 詳細な調査ノート

詳細な調査資料は日本語でリポジトリにあります。方法、閲覧範囲、原典の該当箇所、結果、推論の限界を記録しています。

- [根拠の対応表](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/evidence-map.md)
- [Wertheimerの調査ノート](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/wertheimer.md)
- [NielsenとRosenholtzの調査ノート](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/nielsen-rosenholtz.md)
- [Tuchの調査ノート](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/tuch.md)
- [設計と検証の手順](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/design-decisions.md)