# Data Card

## Purpose

The bundled fixture is an invented, minimal teaching input for deterministic software tests and a classroom-style TF-IDF/XGBoost demonstration.

## Composition and provenance

Every text string is freshly authored synthetic content. Rows use only `simulated_signal` and `simulated_control`. These names describe a controlled toy-classification exercise, **not clinical truth, mental-health status, symptom presence, or risk**.

No real social-media data, post text, account information, identifiers, timestamps, metadata, annotations, downloads, or derived records are included or used.

## Collection and preprocessing

There was no collection process. Fixtures are packaged in source code, validated for schema and allowable labels, and used in memory only. The program does not fetch external data.

## Appropriate use

Educational examples of input validation, text vectorization, and aggregate evaluation only. Never use this fixture or a model trained from it for clinical, employment, insurance, individual-risk, eligibility, or automated decision-making purposes.

## Limitations

The fixture is tiny, non-representative, intentionally artificial, and cannot support claims about people, language, prevalence, real-world performance, fairness, or generalization.
