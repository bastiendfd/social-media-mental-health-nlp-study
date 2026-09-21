"""Validation for the bundled synthetic fixture only."""

from collections.abc import Sequence

ALLOWED_LABELS = frozenset({"simulated_signal", "simulated_control"})


def validate_fixture_rows(rows: Sequence[dict[str, str]]) -> None:
    """Reject malformed rows and anything outside the synthetic label set."""
    if not rows:
        raise ValueError("fixture rows must not be empty")
    for row in rows:
        if set(row) != {"text", "label"}:
            raise ValueError("each fixture row must contain text and label")
        if not isinstance(row["text"], str) or not row["text"].strip():
            raise ValueError("fixture text must be non-empty")
        if row["label"] not in ALLOWED_LABELS:
            raise ValueError("fixture rows must use simulated labels")
