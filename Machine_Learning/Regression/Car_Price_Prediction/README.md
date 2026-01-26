# 🚗 Car Selling Price Prediction

Predict the selling price of used cars using machine learning regression models.  
This project demonstrates a **complete end-to-end ML workflow** — from data exploration and preprocessing to modeling, evaluation, visualization, and **Explainable AI (XAI)** — making it ideal for a portfolio showcase.

---

## 📂 Dataset

The dataset used is **`car data.csv`**, containing the following features:

| Feature | Description |
|------|------------|
| Car_Name | Name of the car |
| Year | Year of manufacturing |
| Selling_Price | **Target variable** – selling price (in lakhs INR) |
| Present_Price | Original showroom price (in lakhs) |
| Kms_Driven | Distance driven in kilometers |
| Owner | Number of previous owners |
| Fuel_Type | Petrol, Diesel, or CNG |
| Seller_Type | Dealer or Individual |
| Transmission | Manual or Automatic |

---

## 🛠 Project Workflow

### 1️⃣ Data Exploration (EDA)
- Checked for missing values and data types  
- Analyzed categorical feature distributions  
- Explored relationships between features  

---

### 2️⃣ Data Preprocessing
- Dropped irrelevant columns (`Car_Name`)  
- Encoded categorical features (`Fuel_Type`, `Seller_Type`, `Transmission`) using **OneHotEncoder**  
- Split the dataset into **training (90%)** and **testing (10%)** sets  
- Standardized numerical features using **StandardScaler**  

---

### 3️⃣ Modeling & Evaluation
The following regression models were trained and evaluated:
- **Linear Regression**
- **Lasso Regression (L1 Regularization)**

Model performance was evaluated using the **R² score**.

---

## 📊 Results

### 🔹 Model Performance

| Model | R² Score |
|------|----------|
| Linear Regression | 0.83 |
| Lasso Regression | 0.90 |

> R² values may vary slightly depending on train/test split and scaling.

---

## 🔍 Explainable AI (XAI) – Model Interpretation with SHAP

To understand **how and why** the model makes predictions, **SHAP (SHapley Additive exPlanations)** was applied to the **Lasso Regression model**.

### Methodology
- Used **`shap.LinearExplainer`** (optimized for linear models)  
- SHAP values computed **on the training set only**  
- Generated:
  - Feature importance (bar plot)

---

### 📌 SHAP Feature Impact (Lasso Regression)

| Feature | Impact on Selling Price |
|------|-------------------------|
| Present_Price | Strong positive impact |
| Year | Newer cars → higher price |
| Fuel_Type_Diesel | Slight positive effect |
| Seller_Type_Individual | Negative impact |
| Kms_Driven | Higher mileage → lower price |
| Transmission_Manual | Slight negative effect |
| Owner | Not significant |
| Fuel_Type_Petrol | Baseline category |

---

## 📈 Visualizations

- **Predicted vs Actual Prices**  
  Scatter plots with prediction reference line for both Linear and Lasso regression models

- **SHAP Visualizations**
  - Feature importance bar plots

---

## ⚡ Requirements

- Python 3.x  
- numpy  
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  
- shap  

---

## 🚀 How to Run

```bash
git clone https://github.com/YoussefAIDev/Car_Price_Prediction.git
