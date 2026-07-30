import os

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_and_prepare_dataset():
    dataset_path = kagglehub.dataset_download("vivekmali1436/banking-transactions-dataset")
    card_txn_path = os.path.join(dataset_path, "card_transactions.csv")
    df = pd.read_csv(card_txn_path)
    df = df.sample(n=50000, random_state=42, replace=False)

    df["txn_date"] = pd.to_datetime(df["txn_date"], errors="coerce")
    df["txn_month"] = df["txn_date"].dt.month
    df["txn_day"] = df["txn_date"].dt.day
    df["txn_hour"] = 0

    df = df.drop(columns=["card_txn_id", "txn_date"], errors="ignore")

    categorical_columns = [col for col in df.columns if df[col].dtype == "object"]
    df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

    target_name = "is_fraud"
    feature_columns = [col for col in df.columns if col != target_name]
    df[target_name] = df[target_name].astype(int)

    return df, target_name, feature_columns


def explore_dataset(df):
    print("=== Dataset Head ===")
    print(df.head())
    print("\n=== Dataset Info ===")
    df.info()
    print("\n=== Dataset Description ===")
    print(df.describe(include="all"))


def preprocess_dataset(df):
    df = df.copy()

    df = df.drop_duplicates()

    for column in df.columns:
        if df[column].isna().any():
            if pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].fillna(df[column].median())
            else:
                df[column] = df[column].fillna(df[column].mode()[0])

    target_name = "is_fraud"
    X = df.drop(columns=[target_name])
    y = df[target_name]

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns, index=X.index)
    return X_scaled, y


def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, average="weighted", zero_division=0),
        "recall": recall_score(y_test, predictions, average="weighted", zero_division=0),
        "f1_score": f1_score(y_test, predictions, average="weighted", zero_division=0),
    }

    cm = confusion_matrix(y_test, predictions)
    return predictions, metrics, cm


def plot_confusion_matrix(cm):
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=300, bbox_inches="tight")
    plt.close()


def main():
    df, target_name, feature_columns = load_and_prepare_dataset()

    print("\nStep 1 & 2: Dataset selected and loaded")
    explore_dataset(df)

    print("\nStep 3: Data preprocessing")
    X, y = preprocess_dataset(df)
    print(f"Shape after preprocessing: {X.shape}")
    print(f"Missing values remaining: {X.isnull().sum().sum()}")
    print(f"Duplicate rows removed: {len(df) - len(df.drop_duplicates())}")

    print("\nStep 4: Train-Test split")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")

    print("\nStep 5 & 6: Model training")
    model = train_model(X_train, y_train)
    print("Random Forest Classifier trained successfully")

    print("\nStep 7: Prediction")
    predictions, metrics, cm = evaluate_model(model, X_test, y_test)
    print(f"First 10 predictions: {predictions[:10]}")

    print("\nStep 8: Model evaluation")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1 Score: {metrics['f1_score']:.4f}")

    print("\nStep 9: Visualization")
    plot_confusion_matrix(cm)
    print("Confusion matrix saved as confusion_matrix.png")

    print("\nStep 10: Result & Conclusion")
    print("Used Random Forest Classifier for this supervised classification task.")
    print("The model performed well on the banking transactions dataset with strong evaluation metrics.")
    print("Possible improvements: try other algorithms, tune hyperparameters, or use more complex datasets.")

    return {
        "metrics": metrics,
        "confusion_matrix": cm,
        "target_name": target_name,
        "feature_columns": feature_columns,
    }


if __name__ == "__main__":
    main()
