# Dashboard review: finding overdue work

This illustrative scenario uses a fictional dashboard and fictional observations. It does not report a user study.

## Reader task

An operations lead needs to identify overdue accounts and see the next action for each one.

## Example observations

- Overdue counts and routine counts use the same bright accent color.
- Each row shows the account status, but the age of the overdue item appears in a separate column far from the status.
- The last-updated time sits in the page footer, away from the data it describes.
- Several next-action labels wrap, so their relationship to the account is hard to scan.

These observations describe the fictional example above. A real review should point to visible elements in the supplied screen or file.

## Evidence and inference

Rosenholtz, Li, and Nakano (2007) studied visual clutter and visual search in map images. The [research note](../references/nielsen-rosenholtz.md) explains the study's scope. Their work gives a reason to inspect how visual features compete while someone searches for a target. It does not show that simplifying a business dashboard improves work outcomes.

Nielsen's eighth usability heuristic is a review prompt about information that competes with a user's goal. It is not a measured result for this dashboard.

## Design hypothesis

Group each overdue account's status, age, and next action. Keep the last-updated time close to the data it describes. Give overdue status a clear, consistent treatment that differs from routine counts.

This is a design hypothesis. Preserve the reporting period, units, source, filters, warnings, and other details people need to interpret the counts.

## Check the proposal

1. Compare the current and proposed views with the same data, viewport, and state.
2. Ask intended reviewers to find all overdue accounts and state the age and next action for each one.
3. Record correct answers and any point where reviewers confuse a status, count, or date.
4. Check loading, empty, and error states to confirm that the required labels and status remain available.

Report the result for the task and conditions you checked. The research sources alone do not establish that the proposal improves accuracy or speed.
