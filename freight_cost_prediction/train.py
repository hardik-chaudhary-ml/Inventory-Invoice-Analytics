import joblib
from pathlib import Path

from data_preprocessing import (
    load_vendor_invoice_data,
    prepare_features,
    split_data
)

from modeling_evaluation import (
    train_linear_regression,
    train_decision_tree,
    train_random_forest,
    evaluate_model
)


def main():
    # Base directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Create models folder
    model_dir = BASE_DIR / "models"
    model_dir.mkdir(exist_ok=True)

    model_path = model_dir / "predict_freight_model.pkl"

    # Load data
    df = load_vendor_invoice_data()

    # Prepare data
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train models
    lr_model = train_linear_regression(X_train, y_train)
    dt_model = train_decision_tree(X_train, y_train)
    rf_model = train_random_forest(X_train, y_train)

    # Evaluate
    results = []
    results.append(evaluate_model(lr_model, X_test, y_test, "Linear Regression"))
    results.append(evaluate_model(dt_model, X_test, y_test, "Decision Tree"))
    results.append(evaluate_model(rf_model, X_test, y_test, "Random Forest"))

    # Select best model
    best_model_info = min(results, key=lambda x: x["mae"])
    best_model_name = best_model_info["model_name"]

    best_model = {
        "Linear Regression": lr_model,
        "Decision Tree": dt_model,
        "Random Forest": rf_model
    }[best_model_name]

    # Save model
    joblib.dump(best_model, model_path)

    print(f"\nBest model: {best_model_name}")
    print(f"Saved at: {model_path}")


if __name__ == "__main__":
    main()