# Data-Driven Product Management: Market Analysis for Digital Fitness Products

This project explores global and national search interest in fitness-related keywords to help identify opportunities for digital fitness products. Using Google Trends data, the analysis focuses on understanding how the demand for workouts, home workouts, gym workouts, and home gym products has changed over time, especially during the COVID-19 pandemic.

## 📊 Project Overview

As a product manager in a fitness studio, the goal of this analysis is to evaluate:
- Global trends in workout-related searches  
- The peak year of global interest in the keyword **"workout"**
- The most popular fitness-related keywords during the COVID period vs. today  
- Countries with the highest interest in workouts  
- Comparison of home workout demand between **Philippines** and **Malaysia**  

The findings can help inform product strategy, market expansion decisions, and the development of digital fitness services.

---

## 🧰 Tools & Technologies
- **Python**
- **Pandas** (data manipulation)
- **Matplotlib** (data visualization)
- **Google Trends datasets (CSV files)**

---

## 📁 Dataset Description

### **workout.csv**
| Column | Description |
|--------|-------------|
| month | Month of measurement |
| workout_worldwide | Global search index for "workout" |

### **three_keywords.csv**
Includes 3 worldwide fitness-related keywords:
- *home_workout_worldwide*
- *gym_workout_worldwide*
- *home_gym_worldwide*

### **workout_geo.csv**
Search interest in "workout" by country (2018–2023)

### **three_keywords_geo.csv**
Interest by country for:
- home workout  
- gym workout  
- home gym  

---

## 🔍 Key Tasks Completed
1. Loaded and explored all datasets  
2. Identified the year with peak global interest for **“workout”**  
3. Visualized popularity trends for three fitness keywords  
4. Determined:
   - Most popular keyword during COVID  
   - Most popular keyword today  
5. Identified the country with the highest interest in workouts  
6. Compared home workout demand between the **Philippines** and **Malaysia**  

---

## 📈 Visualizations
A multi-line plot was created to visualize trends in:
- home workout  
- gym workout  
- home gym  

This helps compare user interest and identify key growth periods.

---

## 🧾 Results Summary
- **Peak global interest year:** *Found programmatically*  
- **Most popular keyword during COVID:** `home_workout`  
- **Most popular keyword currently:** `gym_workout`  
- **Top workout country (global):** *Determined via dataset*  
- **Higher home workout demand (Philippines vs Malaysia):** *Calculated from data*  
