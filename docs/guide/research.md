# Research and scope

<nav class="page-language" aria-label="Language">
  <a href="/migaki/guide/research.html" lang="en">English</a><span aria-hidden="true">/</span><a href="/migaki/ja/guide/research.html" lang="ja">日本語</a>
</nav>

The skill uses four source areas to inform visual organization and review. They do not share one method or support the same claims. Use the scope column before applying a finding to a modern interface.

## Source map

| Source and type | What it can inform | What it does not establish |
| --- | --- | --- |
| [Wertheimer (1923)](https://psychclassics.yorku.ca/Wertheimer/Forms/forms.htm), perceptual organization research. The page is a 1938 English reprint. | Whether proximity, similarity, direction, and other grouping cues agree with the relationships in the content. | A fixed spacing rule for modern interfaces, a universal ranking of grouping cues, or a business outcome. |
| [Nielsen’s usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), a review heuristic. | Whether unrelated information competes with what people need for their task. | Whether a particular redesign improves task performance. Heuristic review is not a user task study. |
| [Rosenholtz, Li, and Nakano (2007)](https://doi.org/10.1167/7.2.17), visual clutter research. | How image statistics such as feature variation relate to visual search in the studied map tasks. | A universal clutter score, a fixed color limit, or a general usability threshold. |
| [Tuch et al. (2012)](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/), website first-impression research. | How visual complexity and category typicality related to immediate beauty ratings of website screenshots under the study’s conditions. | Usability, comprehension, long-term satisfaction, conversion, or a rule that simpler pages always work better. |

## Use evidence at the right level

### Research result

A research result includes the task, material, participants, measure, and conditions that produced it. The finding applies within that studied scope. A result from map search or brief ratings of static websites does not directly predict how people will complete a task in an application.

### Heuristic

A heuristic gives reviewers a useful question. It is not a measured outcome for the interface being reviewed. Nielsen’s eighth heuristic asks whether unrelated information competes with the task. It does not call for removing useful labels, status, warnings, or controls.

### Application hypothesis

An application hypothesis connects a source to one design change. Pair it with a check. For example, if a form label seems attached to the neighboring value, group the label with its intended value and inspect the rendered form to see whether the relationship reads clearly.

### Observation

An observation reports what the reviewer saw or did in a named artifact and state. A source-code review does not confirm the rendered page. A rendered-page check does not establish that intended users understand it.

## Limits that apply across sources

The four sources do not set a required number of colors, typefaces, cards, buttons, border radii, or spacing ratios. They also do not ban gradients, centered headings, shadows, or decoration. Choose those details for the medium and task, then inspect the result.

Beauty, findability, comprehension, task success, and preference are separate outcomes. A positive first impression does not establish better task performance or a business result.

## Read the detailed notes

The repository keeps detailed source notes in Japanese. The notes record methods, access limits, source locations, findings, and the boundary between evidence and design inference.

- [Evidence map](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/evidence-map.md)
- [Wertheimer source note](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/wertheimer.md)
- [Nielsen and Rosenholtz source note](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/nielsen-rosenholtz.md)
- [Tuch source note](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/tuch.md)
- [Design and verification procedure](https://github.com/Sunwood-ai-labs/migaki/blob/main/references/design-decisions.md)