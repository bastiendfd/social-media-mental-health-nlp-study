# Model Card

## Model type

A reproducible educational pipeline: `TfidfVectorizer` followed by a small `XGBClassifier`. It exists solely to demonstrate plumbing and aggregate metrics on bundled synthetic fixtures.

## Intended use

Software education, test examples, and discussion of responsible ML boundaries.

## Out of scope and prohibited uses

This is **not a depression detector** and is **not diagnostic**. It must not be used for clinical care, screening, triage, therapy, crisis response, employment, insurance, credit, housing, education, moderation, surveillance, eligibility, or any individual-risk decision.

## Training and evaluation data

Only freshly written synthetic short text fixtures with `simulated_signal` / `simulated_control` labels are used. No real social-media data or model artifact is distributed. The CLI trains in memory and intentionally does not save a model.

## Metrics

The CLI prints accuracy, macro precision, macro recall, and macro F1 for a deterministic synthetic holdout. Metrics are aggregates from a toy fixture, not evidence of validity or performance in any setting.

## Limitations and risks

The data are tiny, artificial, and non-representative. Language can be context-sensitive and ambiguous. The setup lacks external validation, calibration, subgroup analysis, causal evidence, human-subject review, and real-world utility assessment. Any reuse beyond education is unsafe.
