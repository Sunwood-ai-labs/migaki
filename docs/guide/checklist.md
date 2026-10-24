# Design checklist

<nav class="page-language" aria-label="Language">
  <a href="/evidence-informed-design/guide/checklist.html" lang="en">English</a><span aria-hidden="true">/</span><a href="/evidence-informed-design/ja/guide/checklist.html" lang="ja">日本語</a>
</nav>

Choose the items that fit the artifact, reader, task, and constraints. These items are prompts, not a score or pass/fail threshold. Record unresolved issues and their impact.

The `[ ]` marks are static fields, not interactive controls; this page does not save their state. Copy or print the relevant items, then record the viewing conditions and observed result. A mark alone does not prove that you checked the finished artifact.

## How to use this checklist

Use the stable item IDs in notes and conversations. Keep existing IDs when adding items. Mark an item out of scope with a reason when it does not apply to the medium.

| Mark | State |
| --- | --- |
| `[ ]` | Not checked. |
| `[x]` | No issue was found, or you checked the expected result after a fix. |
| `[ ] Needs revision: details` | Record the issue. |
| `[ ] Out of scope: reason` | Record why the item does not apply. |

Do not mark an item as checked if you only viewed it or an issue remains. Recheck the artifact after a fix. Labels such as “practical check” name a method, not an evidence type.

## 1. Before you create

- [ ] PRE-01. Record who needs to find, decide, or do what, and in which situation. (Practical check)
- [ ] PRE-02. Define the current task and an observable result you can check in the artifact. (Practical check)
- [ ] PRE-03. List required information, conditions, labels, units, sources, and states. Confirm why each must remain. (Practical check)
- [ ] PRE-04. Check the medium, display or page conditions, use constraints, and existing conventions. (Practical check)

## 2. Grouping and hierarchy

- [ ] STR-01. Check that content relationships match the relationships shown by layout or shared appearance. Check possible false associations in the artifact. (Application hypothesis informed by W1923)
- [ ] STR-02. Decide which information should be found first and which information should share the same emphasis for comparison. (Practical check)
- [ ] STR-03. Check whether headings, labels, and order support the reader’s task and make relationships traceable. (Practical check)
- [ ] STR-04. Check whether differences in color, contrast, size, weight, or orientation compete and make the target information harder to find. (Application hypothesis informed by R2007. This does not calculate a clutter metric.)
- [ ] STR-05. Check whether decoration and distinctive styling fit the context and help rather than hinder identification or reading. (Practical check)

## 3. Required content and display states

- [ ] CNT-01. When simplifying the appearance, check that explanations, conditions, labels, states, and action results needed for the task remain. (Heuristic from N1994)
- [ ] CNT-02. Check that numbers and charts show the units, period, update time, comparison conditions, legend, and source needed to interpret them. (Practical check)
- [ ] CNT-03. Check that color is not the only way to distinguish a state or meaning. Use text or shape as well. Consult the applicable standard separately when you need a conformance decision. (Practical check)
- [ ] CNT-04. Check that text and labels remain readable without clipping or overlap, including at larger sizes and with wrapping. (Practical check)

## 4. Check the artifact

- [ ] VER-01. Display the artifact in its intended medium and record the actual viewport width, page, zoom, or other conditions. (Practical check)
- [ ] VER-02. For a before-and-after comparison, keep the content, display conditions, data, and interaction state the same. Record any condition you changed. (Practical check)
- [ ] VER-03. Use the artifact to find information, compare values, make a decision, or try the task. Record the result. (Practical check)
- [ ] VER-04. If the artifact has interactions, run the relevant actions and states. A screenshot alone does not confirm interaction or keyboard behavior. (Practical check)
- [ ] VER-05. Check for clipping, overlap, false associations, and missing information. Keep unchecked display conditions marked as unverified. (Practical check)

## 5. Record and report issues

- [ ] REP-01. Record the issue’s source (request, source code, image, actual screen, etc.) and the conditions you checked. Separate what you observed on the actual screen from what you inferred from explanatory text; mark anything you did not verify. (Practical check)
- [ ] REP-02. Link each proposed change to its evidence type. For an application hypothesis, include the target issue and how you will check it. (Practical check)
- [ ] REP-03. Report the checks you performed, their conditions and results, and unresolved issues. Do not report an unresolved issue as fixed. Record review submission separately from completion of artifact changes. (Practical check)

## Additional checks by medium

Use only the media-specific items that apply. These items supplement the core checks.

### Web

- [ ] WEB-01. At the target viewport widths, run the main navigation and input tasks. Check appearance and behavior. (Practical check)
- [ ] WEB-02. When assessing a website’s first impression, record how it was presented and what you evaluated. T2012 studied website screenshot complexity, typicality, and aesthetic first impressions. It did not test operational success. (Application hypothesis informed by T2012)

### Slides

- [ ] SLD-01. Display the slides as they will be presented. Check text, diagrams, and labels from the audience’s viewing distance and screen. (Practical check)
- [ ] SLD-02. Check that readers can match claims to evidence, diagrams to labels, and citations to their sources. (Practical check)

### Documents

- [ ] DOC-01. Check that heading levels match the content order and help readers reach the intended section. (Practical check)
- [ ] DOC-02. Check that notes, footnotes, and figure descriptions point to the right text or figure. (Practical check)

### Charts

- [ ] CHART-01. Show axes, units, periods, comparison conditions, legends, and sources so readers can interpret the values. (Practical check)
- [ ] CHART-02. Check that scales, baselines, and emphasis do not misrepresent differences or trends. (Practical check)

## Record an issue

Copy the fields you need for each item. Keep observations, proposed changes, evidence, and check results separate.

| Field | Record |
| --- | --- |
| Checklist item ID |  |
| Observed issue and viewing conditions |  |
| Issue source (request, source code, image, actual screen, etc.) |  |
| Source verification status | Checked or unverified |
| Proposed change |  |
| Evidence type and ID | Research result, heuristic, application hypothesis, or practical judgment with no named source. |
| Check method and conditions |  |
| Result |  |
| Unresolved issues |  |

## Evidence types and limits

- W1923 is a classic study of perceptual grouping. It covers points, shapes, lines, and motion. It does not define ideal spacing for modern interfaces or the effect of a specific screen change.
- N1994 provides heuristics for reviewing usability. It is not an experiment showing that removing a specific decoration or explanation will improve a particular artifact.
- R2007 studied visual clutter measures and their relationship to visual search in images. This qualitative checklist does not calculate those measures.
- T2012 studied visual complexity, typicality, and aesthetic first impressions of website screenshots. It does not establish effects on interaction, comprehension, trust, purchases, or long-term satisfaction.
- The media-specific prompts and review methods are not research findings. Treat an application of research or a heuristic to a specific layout as a hypothesis, and connect the proposed change to a check on the artifact.
- “Practical check” labels a review method, not an evidence type. Record the result of an observation or trial in the result field. Evidence types are research findings, heuristics, application hypotheses, or practical judgments with no named source.
- This checklist is not a validated scale or a standards-conformance test. Do not add up its items to create a quality score or pass/fail result.

See [Research and scope](/guide/research) for the source notes. The [Japanese source checklist](https://github.com/Sunwood-ai-labs/evidence-informed-design/blob/main/references/design-checklist.md) contains the stable IDs and full record template.
