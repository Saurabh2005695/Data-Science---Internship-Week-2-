import unittest

from sklearn.model_selection import train_test_split

from week2_predictive_modeling import evaluate_model, load_and_prepare_dataset, preprocess_dataset, train_model


class TestBankingPredictiveModel(unittest.TestCase):
    def test_pipeline_outputs_valid_metrics(self):
        df, target_name, feature_columns = load_and_prepare_dataset()
        self.assertIn("is_fraud", df.columns)
        self.assertEqual(target_name, "is_fraud")
        self.assertGreater(len(feature_columns), 0)

        X, y = preprocess_dataset(df)
        self.assertGreater(len(X), 0)
        self.assertEqual(len(X), len(y))

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        model = train_model(X_train, y_train)
        _, metrics, cm = evaluate_model(model, X_test, y_test)

        self.assertGreater(metrics["accuracy"], 0.8)
        self.assertGreater(metrics["precision"], 0.8)
        self.assertGreater(metrics["recall"], 0.8)
        self.assertGreater(metrics["f1_score"], 0.8)
        self.assertEqual(cm.shape, (2, 2))


if __name__ == "__main__":
    unittest.main()
