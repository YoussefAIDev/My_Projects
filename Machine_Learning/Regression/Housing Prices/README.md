🏠 California Housing Price Prediction Model

This project implements a Linear Regression model to predict median house values in California based on demographic and geographic features from the California Housing dataset.

🔍 Model Overview

Algorithm: Linear Regression (scikit-learn)

Task: Regression

Target Variable: median_house_value

Input Features:
Includes numerical features such as population, median income, housing age, and a categorical feature (ocean_proximity) encoded using One-Hot Encoding.

🧹 Data Preprocessing

Missing values are handled using median imputation for numerical columns.

The categorical feature ocean_proximity is converted into numerical form using pd.get_dummies.

Special care is taken to ensure that training and testing datasets have identical feature columns, preventing feature mismatch errors.

📊 Model Evaluation

The model is evaluated using the R² score on the test dataset.

Train-test split is applied to measure generalization performance.

🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Jupyter Notebook

🚀 Purpose

This project is intended for learning and practicing:

Data preprocessing

Handling categorical variables

Building and evaluating regression models

Avoiding common machine learning pitfalls (such as feature mismatch between train and test sets)
