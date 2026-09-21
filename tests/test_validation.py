import pytest

from synthetic_social_signal_nlp.validation import validate_fixture_rows


def test_rejects_non_simulated_labels() -> None:
    rows = [{"text": "a short synthetic fixture", "label": "clinical_positive"}]

    with pytest.raises(ValueError, match="simulated labels"):
        validate_fixture_rows(rows)
