🚗 Car Selling Price Prediction

Predict the selling price of used cars using machine learning regression models.
This project demonstrates a complete ML workflow from data exploration → preprocessing → modeling → evaluation → visualization, making it perfect for a portfolio showcase.

📂 Dataset

The dataset used is car data.csv and contains the following features:

Feature	Description
Car_Name	Name of the car
Year	Year of manufacturing
Selling_Price	Target variable – selling price in lakhs (INR)
Present_Price	Original price of the car in lakhs
Kms_Driven	Distance driven in kilometers
Owner	Number of previous owners
Fuel_Type	Petrol, Diesel, or CNG
Seller_Type	Dealer or Individual
Transmission	Manual or Automatic
🛠 Project Workflow
1. Data Exploration (EDA)

Checked for missing values and data types.

Analyzed categorical feature distributions.

Identified correlations and potential feature importance.

2. Data Preprocessing

Dropped irrelevant columns such as Car_Name.

Encoded categorical features (Fuel_Type, Seller_Type, Transmission) using OneHotEncoder.

Split the dataset into training (90%) and testing (10%) sets.

Standardized numerical features using StandardScaler for better model performance.

3. Modeling and Visualization

Built Linear Regression and Lasso Regression models.

Evaluated models using R² score.

Compared model predictions visually using scatterplots and residual plots.

📊 Results
Model Performance
Model	R² Score
Linear Regression	0.83
Lasso Regression	0.90

R² values may vary slightly depending on train/test split and scaling.

Explainable AI – Feature Importance (Lasso)
Feature	Coefficient	Impact on Selling Price
Present_Price	3.66	Higher original price → higher selling price
Year	1.01	Newer cars → higher price
Fuel_Type_Diesel	0.55	Diesel cars slightly increase price
Seller_Type_Individual	-0.40	Selling from an individual → lower price
Kms_Driven	-0.09	More kilometers → slightly lower price
Transmission_Manual	-0.13	Manual transmission → slightly lower price
Owner	0	Not significant in this model
Fuel_Type_Petrol	0	Not significant (baseline category)
📈 Visualizations

Predicted vs Actual Prices: Scatterplots for Linear and Lasso Regression with a perfect prediction line.

Residuals Comparison: Residuals (Actual − Predicted) for both models to inspect errors and model fit visually.

Visualization helps quickly identify model accuracy and potential overfitting.

⚡ Requirements

Python 3.x with the following libraries:

numpy

pandas

matplotlib

seaborn

scikit-learn

🚀 Steps to Run

Clone the repository:

git clone https://github.com/YoussefAIDev/Car_Price_Prediction.git


Open the Jupyter Notebook and run all cells.

Ensure car data.csv is in the correct path.
