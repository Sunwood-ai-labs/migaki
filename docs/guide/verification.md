# Verify a design decision

<nav class="page-language" aria-label="Language">
  <a href="/evidence-informed-design/guide/verification.html" lang="en">English</a><span aria-hidden="true">/</span><a href="/evidence-informed-design/ja/guide/verification.html" lang="ja">日本語</a>
</nav>

Use the check that matches the design question. Record the artifact, viewing conditions, action, and result so another person can understand what you verified.

## Connect the question to a check

1. **Name the reader’s task.** State what someone needs to find, compare, understand, or do.
2. **Record the content relationships.** Identify which labels, values, warnings, controls, or notes belong together.
3. **Choose a source and name its type.** Separate a research result from a heuristic or a design inference.
4. **State one design hypothesis.** Describe the change and the visible or behavioral result you expect.
5. **Check the finished artifact.** Use the intended medium, viewport, content, and relevant state.
6. **Report the boundary.** Say what the check confirms and what needs a different check.

## Match claims to evidence

| Check | What it can confirm | What it leaves open |
| --- | --- | --- |
| Content review | Required labels, units, conditions, warnings, and source notes remain present. | Whether people understand the content. |
| Rendered view | The layout, hierarchy, wrapping, clipping, and visual relationships at the checked size. | Keyboard access, assistive technology behavior, or task success. |
| Operation check | The named interaction and its loading, error, or completion state. | Whether users know when or how to take that action. |
| Task attempt | What the person doing the check could find or complete in that run. | General results for other people or tasks. |
| Intended-user evaluation | Responses from participants on the tested tasks and conditions. | Results outside the tested participants and conditions. |

## Report the result plainly

Use a short record such as this:

> **Observation:** The period label appears closer to the neighboring value than to its intended amount.
>
> **Change:** Place the period label beside its amount.
>
> **Basis:** Application hypothesis based on Wertheimer’s discussion of proximity.
>
> **Check:** In the rendered form, the label and amount read as one group. Whether intended users make fewer mistakes remains untested.

Name a rendered view as a rendered-view check. Call a session a user evaluation only when intended users tried the task. Do not report a clutter score, reading-time improvement, or error reduction unless you measured it with a stated method.

[Research and scope](/guide/research) links each source to the question it can support. The repository’s [design and verification procedure](https://github.com/Sunwood-ai-labs/evidence-informed-design/blob/main/references/design-decisions.md) contains more examples.
