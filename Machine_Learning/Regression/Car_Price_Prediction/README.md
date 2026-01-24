Car Selling Price Prediction

Predicting the selling price of used cars using machine learning regression models. This project demonstrates a full workflow from data exploration → preprocessing → modeling → evaluation → visualization, and can serve as a showcase of practical ML skills for a portfolio.

Dataset

The project uses car data.csv which includes the following features:

Car_Name: Name of the car

Year: Year of manufacturing

Selling_Price: Target variable, selling price in lakhs (INR)

Present_Price: Original price of the car in lakhs

Kms_Driven: Distance driven in kilometers

Owner: Number of previous owners

Fuel_Type: Petrol, Diesel, or CNG

Seller_Type: Dealer or Individual

Transmission: Manual or Automatic

Project Steps
Data Exploration (EDA)

Checked for missing values and data types.

Analyzed categorical feature distributions.

Data Preprocessing

Dropped irrelevant columns such as Car_Name.

Encoded categorical features (Fuel_Type, Seller_Type, Transmission) using OneHotEncoding.

Split the data into training and testing sets (90% train, 10% test).

Standardized numerical features for better model performance.

Modeling

Applied Linear Regression and Lasso Regression.

Evaluated models using R² score.

Results
Model Performance
Model	R² Score
Linear Regression	0.85
Lasso Regression	0.83

R² values may vary slightly depending on train/test split and scaling.

Feature Importance (Lasso)
Feature	Coefficient	Impact on Selling Price
Present_Price	3.66	Higher original price → higher selling price
Year	1.01	Newer cars → higher price
Fuel_Type_Diesel	0.55	Diesel cars slightly higher price
Seller_Type_Individual	-0.40	Selling from individual → lower price
Kms_Driven	-0.09	More kilometers → slightly lower price
Transmission_Manual	-0.13	Manual cars slightly lower price
Owner	0	Not important in this model
Fuel_Type_Petrol	0	Not important (baseline category)
Visualizations

Predicted vs Actual Prices: Scatterplots for Linear and Lasso regression with a perfect prediction line.

Residuals Comparison: Residuals (actual minus predicted) for both models to visually inspect errors and model fit.

Getting Started
Requirements

Python 3.x with the following libraries:

numpy

pandas

matplotlib

seaborn

scikit-learn

Running the Project

Clone the repository.

Open the Jupyter Notebook and run all cells.

Ensure the dataset file car data.csv is in the correct path.
