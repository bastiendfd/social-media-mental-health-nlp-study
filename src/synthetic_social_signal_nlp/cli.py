"""Command-line entry point for the synthetic-only demonstration."""

from .pipeline import evaluate_synthetic_fixture


def main() -> int:
    """Print aggregate synthetic-fixture metrics and a non-diagnostic notice."""
    metrics = evaluate_synthetic_fixture()
    print("Educational synthetic-fixture metrics only; not diagnostic.")
    for name, value in metrics.items():
        print(f"{name}={value:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
