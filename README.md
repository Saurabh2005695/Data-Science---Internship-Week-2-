<<<<<<< HEAD
# Data-Science---Internship-Week-2-
This repository showcases a machine learning project completed during Week 2 of a Data Science Internship. It uses a banking transactions dataset to build a fraud detection model with Python and scikit-learn, covering data preprocessing, train-test split, Random Forest training, evaluation metrics, and visualization.
=======
# Predictive Modeling Using Machine Learning

## Project Overview
This project implements a supervised machine learning workflow for a banking dataset to predict whether a card transaction is fraudulent or not. The solution uses a Random Forest Classifier and follows the standard steps of a predictive modeling project: data loading, preprocessing, train-test splitting, model training, prediction, evaluation, and visualization.

## Objective
The main goal of this project is to build a machine learning model that can classify transactions as either:
- Fraudulent
- Non-fraudulent

This type of model is useful in banking and financial systems for fraud detection and risk management.

## Dataset
The project uses the Kaggle dataset:
- Banking Transactions Dataset

The dataset is downloaded automatically using KaggleHub. The script uses the card transactions file from the dataset and builds a classification model based on transaction features.

## Technologies Used
- Python
- pandas
- scikit-learn
- matplotlib
- seaborn
- kagglehub

## Project Steps
The project follows these steps:

1. Dataset Selection
   - A supervised learning dataset was selected.
   - The banking transactions dataset was used for classification.

2. Dataset Loading
   - The dataset was downloaded and loaded into Python using pandas.

3. Data Preprocessing
   - Missing values were handled.
   - Duplicate values were removed.
   - Categorical data was converted into numerical form using one-hot encoding.
   - Feature scaling was applied using StandardScaler.

4. Train-Test Split
   - The data was divided into training and testing sets.
   - An 80/20 split was used.

5. Model Selection
   - The Random Forest Classifier was used.

6. Model Training
   - The model was trained on the training dataset.

7. Prediction
   - Predictions were made on the test dataset.

8. Evaluation
   - The following metrics were calculated:
     - Accuracy
     - Precision
     - Recall
     - F1 Score

9. Visualization
   - A confusion matrix was created and saved as an image.

## Model Performance
The trained Random Forest model achieved excellent results on the test set:
- Accuracy: 0.9949
- Precision: 0.9898
- Recall: 0.9949
- F1 Score: 0.9924

These results show that the model performs very well for this classification task.

## Files in the Project
- week2_predictive_modeling.py
  - Main Python script for the project
- test_week2_predictive_modeling.py
  - Unit test for validating the workflow
- requirements.txt
  - Required Python packages
- confusion_matrix.png
  - Saved confusion matrix visualization

## How to Run the Project
### 1. Open the project folder
Open the folder in VS Code or any Python editor.

### 2. Create and activate a virtual environment (optional but recommended)
Run the following commands:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the main script
```bash
python week2_predictive_modeling.py
```

### 5. Run the test
```bash
python -m unittest -q test_week2_predictive_modeling.py
```

## Result and Conclusion
This project successfully demonstrates how to build a predictive model using machine learning. The Random Forest Classifier produced highly accurate predictions for fraud detection on the banking dataset.

### Conclusion
- The model performed very well.
- The project shows the full workflow of machine learning from data loading to performance evaluation.
- Future improvements could include:
  - Trying other algorithms such as Decision Tree or Logistic Regression
  - Hyperparameter tuning
  - Using a larger dataset
  - Adding a ROC curve for further evaluation

## Summary
This project is a complete example of predictive modeling using machine learning for fraud detection in the banking domain.
>>>>>>> e6455de (Initial commit for Data Science Internship Week-2)
