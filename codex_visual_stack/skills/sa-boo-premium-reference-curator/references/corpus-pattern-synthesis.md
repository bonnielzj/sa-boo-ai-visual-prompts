# Corpus pattern synthesis / 图库规律提炼

Use this method when an existing visual library should teach a reusable design
method, not merely grow in count. It joins deterministic measurement, visual
interpretation, and Bonnie's feedback without treating any one layer as sufficient.

## Evidence layers

1. **Deterministic corpus facts** — Lab palette and luminance distributions,
   saturation, contrast, colorfulness, edge/detail density, aspect ratio, spatial
   concentration, OCR text area/position when boxes exist, duplicate state, and
   coarse clusters. These describe pixels and metadata only.
2. **Designer interpretation** — hierarchy, type-image relationship, proportion,
   rhythm, material behavior, cultural or emotional meaning, and the design move
   that produces an effect. Inspect full-size representatives and counterexamples;
   do not infer these from a numeric cluster name.
3. **User evidence** — `USER_ACCEPTED_RESULT`, `USER_ACCEPTED_DIMENSION`,
   `USER_SELECTED_FOR_DEVELOPMENT`, `PARTIALLY_SUPPORTED`, `USER_REJECTED`, or
   `REVIEW_PENDING`, bound to an exact asset/version and scope. Silence and technical
   PASS are not positive labels.

## Bounded loop

1. Define one question, for example: “Which color-area relationships recur in the
   strongest typography references?” Do not ask the corpus to reveal “good taste” in
   general.
2. Reuse the canonical library. Run the Asset Index corpus analyzer only when the
   metrics are missing or a meaningful batch has changed.
3. Review the overall distributions and 2–4 representative images per cluster at
   full-image scale. Include at least one counterexample that shares the metric but
   not the visual effect.
4. Cross-tab the observed mechanism with explicit tags, transfer rules, and user
   labels. Frequency without acceptance means “common in the collection,” not
   “preferred” or “effective.”
5. Write at most 3–5 candidate mechanisms:

```text
observed relationship
corpus evidence + representative IDs
counterexample / failure condition
user evidence and scope
next controlled design action
status: HYPOTHESIS / PARTIALLY_SUPPORTED / USER_ACCEPTED / TRANSFER_VALIDATED
```

6. Update the existing method ledger or owning skill only when the finding changes a
   future choice. Do not create a second database, a daily report, or a universal
   palette/style rule.

## Cadence and workload

- A practical default is after roughly 8–10 new labeled items or during a weekly
  review. A smaller batch is enough when Bonnie gives decisive feedback.
- Corpus synthesis replaces that session's normal poster or reference-collection
  exercise. It is not extra work added on top.
- Stop when no new mechanism or coverage gap changes the next action. More images do
  not automatically produce more knowledge.

## Tool boundary

`analyze_visual_corpus.py` produces measurement evidence and representative samples.
Optional semantic embeddings or external models may improve retrieval only after a
task-specific capability and privacy check. Neither deterministic features nor
embeddings can judge taste, originality, cultural fit, or approval without visual
inspection and user labels.
