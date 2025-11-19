# Predictive Modeling for Agriculture 🌱

**Project Type:** Supervised Machine Learning – Multi-class Classification  
**Objective:** Help farmers select the best crop based on soil measurements.

---

## Project Overview

Farmers often need to decide which crop to plant to maximize yield. Measuring soil properties can be expensive, and sometimes only one key metric can be measured due to budget constraints.

This project uses **machine learning** to:

- Predict the optimal crop type based on soil measurements:
  - Nitrogen content (N)
  - Phosphorous content (P)
  - Potassium content (K)
  - pH value
- Identify the **single most predictive soil feature** for crop selection.

---

## Key Tasks

1. Perform **Exploratory Data Analysis (EDA)** to understand the soil dataset.  
2. Split the data into training and testing sets.  
3. Build a **multi-class classifier** (Logistic Regression) for each soil feature.  
4. Evaluate feature performance using **Weighted F1 Score**.  
5. Determine the **best predictive feature** and visualize feature importance.

---

## Outcome

- A dictionary variable `best_predictive_feature` contains the **feature name** and its **prediction performance**.  
- Visualizations show the performance of each soil feature in predicting crop types.

---

## Impact

By identifying the most predictive soil feature, farmers can make **cost-effective decisions** about which crop to plant, improving yields while minimizing unnecessary soil tests.

---

## Tools & Libraries

- Python
- pandas
- scikit-learn
- matplotlib
