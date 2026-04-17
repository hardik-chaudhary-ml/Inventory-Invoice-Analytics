from pathlib import Path
import joblib

from data_preprocessing import load_invoice_data, split_data, scale_features, apply_labels
from modeling_evaluation import train_random_forest, evaluate_classifier


FEATURES = [
    "invoice_quantity",
    "invoice_dollars",
    "Freight",
    "total_item_quantity",
    "total_item_dollars"
]

TARGET = "flag_invoice"


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Paths
    scaler_path = BASE_DIR / "models" / "scaler.pkl"
    model_path = BASE_DIR / "models" / "predict_flag_invoice.pkl"

    # Load + label data
    df = load_invoice_data()
    df = apply_labels(df)

    # Split
    X_train, X_test, y_train, y_test = split_data(df, FEATURES, TARGET)

    # Scale
    X_train_scaled, X_test_scaled = scale_features(
        X_train, X_test, scaler_path
    )

    # Train
    grid_search = train_random_forest(X_train_scaled, y_train)

    # Evaluate
    evaluate_classifier(
        grid_search.best_estimator_,
        X_test_scaled,
        y_test,
        "Random Forest Classifier"
    )

    # Save model in MAIN models folder
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(grid_search.best_estimator_, model_path)

    print(f"\nModel saved at: {model_path}")


if __name__ == "__main__":
    main()