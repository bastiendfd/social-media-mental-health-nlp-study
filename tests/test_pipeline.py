from synthetic_social_signal_nlp.pipeline import evaluate_synthetic_fixture


def test_evaluation_returns_bounded_aggregate_metrics() -> None:
    metrics = evaluate_synthetic_fixture()

    assert set(metrics) == {"accuracy", "macro_precision", "macro_recall", "macro_f1"}
    assert all(0.0 <= value <= 1.0 for value in metrics.values())
