# 🐧 Penguin Clustering using K-Means

This project applies **unsupervised machine learning** techniques to analyze and cluster penguin species based on their physical measurements.  
The goal is to discover hidden patterns and natural groupings within the data without using labeled species information.

---

## 📊 Dataset

- **Name:** Palmer Penguins Dataset
- **Source:**  
  Collected by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER  
- **Format:** CSV
- **Description:**  
  The dataset contains physical measurements of penguins, such as:
  - Culmen length (mm)
  - Culmen depth (mm)
  - Flipper length (mm)
  - Body mass (g)

---

## ⚙️ Project Workflow

1. **Data Loading**
   - Importing the dataset using Pandas

2. **Data Preprocessing**
   - Handling missing values
   - Selecting relevant numerical features

3. **Clustering**
   - Applying **K-Means clustering**
   - Assigning cluster labels to each data point

4. **Visualization**
   - Scatter plots to visualize clusters
   - Color-coded clusters for clarity

5. **Statistical Analysis**
   - Creating a final statistical DataFrame
   - Computing mean values of features for each cluster

---

## 🧠 Machine Learning Technique

- **Algorithm:** K-Means
- **Learning Type:** Unsupervised Learning
- **Objective:** Identify natural groupings in penguin physical characteristics

---

## 📈 Results

- Penguins were successfully grouped into distinct clusters
- Each cluster shows unique average physical characteristics
- The results demonstrate how clustering can reveal meaningful biological patterns without labeled data

---

## 🛠️ Tech Stack

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook
