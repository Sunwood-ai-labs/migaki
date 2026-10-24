---
layout: home
hero:
  name: "MIGAKI（ミガキ）"
  text: 読み手の課題に合わせて、情報のまとまりと強調を整えます。
  tagline: 研究と経験則を設計判断に使い、実際の成果物で確かめるCodexスキルです。
  actions:
    - theme: brand
      text: インストールする
      link: /ja/guide/install
    - theme: alt
      text: 根拠の対応を見る
      link: /ja/guide/research
features:
  - title: 読み手の課題から始める
    details: 誰が何を見つけ、比べ、理解し、操作するのかを、レイアウトの変更前に定めます。
  - title: 根拠の種類を分ける
    details: 研究結果、レビューの経験則、応用仮説、観察結果を混同しません。
  - title: 成果物で確かめる
    details: Web画面、スライド、文書、図表を、実際に使う大きさと状態で確認します。
---

<section class="home-evidence-flow" aria-labelledby="evidence-flow-title">
  <p class="eyebrow">確認できる設計手順</p>
  <h2 id="evidence-flow-title">出典から確認へ</h2>
  <div class="evidence-flow-grid">
    <div class="evidence-source-stack">
      <article class="evidence-node">
        <span class="step">出典</span>
        <strong>研究結果</strong>
        <p>その研究は何を、どの条件で測ったか。</p>
      </article>
      <article class="evidence-node">
        <span class="step">点検の観点</span>
        <strong>設計の経験則</strong>
        <p>今の設計を見直すために、どの原則を使うか。</p>
      </article>
    </div>
    <span class="evidence-flow-arrow" aria-hidden="true">→</span>
    <article class="evidence-node evidence-node--decision">
      <span class="step">設計判断</span>
      <strong>応用仮説</strong>
      <p>一つの変更と、画面で確かめられる予想を記す。</p>
    </article>
    <span class="evidence-flow-arrow" aria-hidden="true">→</span>
    <article class="evidence-node evidence-node--check">
      <span class="step">成果物の確認</span>
      <strong>観察結果</strong>
      <p>表示や操作で実際に分かったことと、未確認のことを記す。</p>
    </article>
  </div>
</section>

<p class="home-note">研究を普遍的な作風の規則に置き換えず、表示確認をユーザーテストと呼びません。</p>

## 読む人の課題から始める

誰が、何を、どこで見つけたり理解したりする必要があるかを記します。その作業に必要なラベル、単位、警告、操作を残します。そのうえで、配置、余白、文字、強調が内容上の関係を伝えているかを確かめます。

## 4種類の根拠を区別する

- **研究結果**は、参加者、刺激、課題、測定項目、条件を伴う知見です。
- **経験則**は、画面を点検するための原則です。特定の画面での効果を証明するものではありません。
- **応用仮説**は、出典を具体的な変更案と確認方法へ結び付けます。
- **観察結果**は、実物を見たり操作したりして分かったことです。対象利用者の評価とは区別します。

## 手順と限界を読む

[研究と根拠の範囲](/ja/guide/research)では4つの出典と、各出典から言えることを説明します。[設計判断を検証する](/ja/guide/verification)では、成果物を確認し、その確認で分かった範囲を報告する方法を説明します。
