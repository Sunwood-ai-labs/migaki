---
layout: home
hero:
  name: "Evidence-informed\ndesign"
  text: Review grouping, hierarchy, and visual clutter.
  tagline: Use research and design heuristics to choose one specific change, then check its result in the page, slide, document, or chart.
  actions:
    - theme: brand
      text: Install the skill
      link: /guide/install
    - theme: alt
      text: Read the evidence map
      link: /guide/research
features:
  - title: Start with the task
    details: Define what the reader needs to find, compare, understand, or do before changing the layout.
  - title: Name the kind of evidence
    details: Keep measured research, review heuristics, application hypotheses, and observations distinct.
  - title: Check the finished artifact
    details: Inspect the actual page, slide, document, or chart at the size and state where it will be used.
---

<section class="home-evidence-flow" aria-labelledby="evidence-flow-title">
  <p class="eyebrow">A reviewable method</p>
  <h2 id="evidence-flow-title">From source to check</h2>
  <div class="evidence-flow-grid">
    <div class="evidence-source-stack">
      <article class="evidence-node">
        <span class="step">Source</span>
        <strong>Research result</strong>
        <p>What did the study measure, and under which conditions?</p>
      </article>
      <article class="evidence-node">
        <span class="step">Review prompt</span>
        <strong>Design heuristic</strong>
        <p>What principle helps you inspect the current choice?</p>
      </article>
    </div>
    <span class="evidence-flow-arrow" aria-hidden="true">→</span>
    <article class="evidence-node evidence-node--decision">
      <span class="step">Design decision</span>
      <strong>Application hypothesis</strong>
      <p>State one change and the visible result you expect it to produce.</p>
    </article>
    <span class="evidence-flow-arrow" aria-hidden="true">→</span>
    <article class="evidence-node evidence-node--check">
      <span class="step">Artifact check</span>
      <strong>Observation</strong>
      <p>Record what the rendered or operated artifact shows. Name what remains untested.</p>
    </article>
  </div>
</section>

<p class="home-note">The skill uses evidence to guide a design decision. It does not turn a study into a universal style rule or treat a visual inspection as a user study.</p>

## Start with the reader’s task

Write down who needs to find or understand what, and where they will do it. Preserve the labels, units, warnings, and controls that task depends on. Then inspect whether layout, spacing, typography, and visual emphasis show the same relationships as the content.

## Keep four evidence types distinct

- **Research result** describes a finding with its participants, stimulus, task, measure, and conditions.
- **Heuristic** gives you a principle for reviewing an interface. It does not prove an outcome for a specific screen.
- **Application hypothesis** connects a source to a proposed change and a check you can perform.
- **Observation** records what you saw or did. It does not stand in for feedback from the intended users.

## Read the method and limits

[Research and scope](/guide/research) maps four source areas and shows what each can support. [Verify a design decision](/guide/verification) explains how to check a rendered artifact without claiming more than the check establishes.
