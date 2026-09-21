# Ethics and Safety

## Non-diagnostic educational prototype

This project is **not a depression detector**. It is **not diagnostic** and cannot infer a mental-health condition, wellbeing, intent, or risk from text. It is not suitable for clinical, employment, insurance, or individual-risk decisions.

## Design safeguards

- Only freshly authored, deliberately synthetic fixtures are accepted.
- Labels are `simulated_signal` and `simulated_control`, never clinical ground truth.
- The CLI uses built-in fixtures only; it accepts no external text or data path.
- Training is in memory; no real social-media data, model artifact, checkpoint, log, visualization, notebook output, or result is distributed.
- Evaluation prints aggregate toy metrics only.

## Human impact risks

Text classification can amplify stigma, make false inferences, and create unequal harms. Accuracy on a synthetic fixture does not establish safety, fairness, validity, or benefit. Do not deploy, score people, or make decisions based on this work.

## Reporting concerns

For a security or repository-boundary issue, use the private reporting path in [SECURITY.md](SECURITY.md). For an ethical concern, open a discussion that avoids personal data and includes no real-world text.
