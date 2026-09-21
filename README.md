# Synthetic Social Signal NLP Study

An **educational, synthetic-only** prototype demonstrating a conventional TF-IDF plus XGBoost text-classification workflow. Its short fixtures are invented for software testing and carry only the labels `simulated_signal` and `simulated_control`.

> **Safety boundary:** This is **not a depression detector**, is **not diagnostic**, and is not suitable for clinical, employment, insurance, moderation, eligibility, or individual-risk decisions. Outputs are educational examples only.

## What is included

- Deterministic validation that accepts only small, built-in synthetic fixtures.
- TF-IDF features and a reproducible XGBoost evaluation with aggregate metrics.
- A command-line training/evaluation demonstration.
- Tests and a CI workflow.

## What is not included

No real social-media data, accounts, posts, identifiers, dates, metadata, model artifacts, checkpoints, logs, notebooks, visualizations, or results are distributed. The project does not download external data and does not create or persist trained models.

## Quick start

```bash
uv venv .venv
uv pip install -e '.[dev]'
.venv/Scripts/python.exe -m pytest
.venv/Scripts/synthetic-nlp-study.exe
```

The command reports only aggregate evaluation metrics from its built-in fixtures. Do not interpret its output as an assessment of any person or population.

## Responsible use

Read [DATA_CARD.md](DATA_CARD.md), [MODEL_CARD.md](MODEL_CARD.md), [ETHICS_AND_SAFETY.md](ETHICS_AND_SAFETY.md), and [SECURITY.md](SECURITY.md) before reuse. This repository intentionally has no license selected.
