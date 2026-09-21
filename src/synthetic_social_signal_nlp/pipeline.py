"""In-memory TF-IDF and XGBoost demonstration over synthetic fixtures."""

from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from .validation import validate_fixture_rows

SYNTHETIC_FIXTURE: tuple[dict[str, str], ...] = (
    {"text": "invented quiet afternoon with a book", "label": "simulated_control"},
    {"text": "invented plan for a walk after lunch", "label": "simulated_control"},
    {"text": "invented note about sharing a recipe", "label": "simulated_control"},
    {"text": "invented class project progress update", "label": "simulated_control"},
    {"text": "invented message describing a bright routine", "label": "simulated_control"},
    {"text": "invented reflection about low energy today", "label": "simulated_signal"},
    {"text": "invented note about withdrawing from a group", "label": "simulated_signal"},
    {"text": "invented diary phrase about a heavy morning", "label": "simulated_signal"},
    {"text": "invented short line about losing motivation", "label": "simulated_signal"},
    {"text": "invented reflection about feeling disconnected", "label": "simulated_signal"},
)


def evaluate_synthetic_fixture() -> dict[str, float]:
    """Fit in memory and return aggregate metrics for the synthetic holdout."""
    rows = list(SYNTHETIC_FIXTURE)
    validate_fixture_rows(rows)
    texts = [row["text"] for row in rows]
    labels = [row["label"] for row in rows]
    train_texts, test_texts, train_labels, test_labels = train_test_split(
        texts, labels, test_size=0.4, random_state=17, stratify=labels
    )
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    train_features = vectorizer.fit_transform(train_texts)
    test_features = vectorizer.transform(test_texts)
    numeric_train = [1 if label == "simulated_signal" else 0 for label in train_labels]
    classifier = XGBClassifier(
        n_estimators=12,
        max_depth=2,
        learning_rate=0.3,
        subsample=1.0,
        colsample_bytree=1.0,
        random_state=17,
        n_jobs=1,
        eval_metric="logloss",
    )
    classifier.fit(train_features, numeric_train)
    predictions = classifier.predict(test_features)
    numeric_test = [1 if label == "simulated_signal" else 0 for label in test_labels]
    precision, recall, f1, _ = precision_recall_fscore_support(
        numeric_test, predictions, average="macro", zero_division=0
    )
    return {
        "accuracy": float(accuracy_score(numeric_test, predictions)),
        "macro_precision": float(precision),
        "macro_recall": float(recall),
        "macro_f1": float(f1),
    }
