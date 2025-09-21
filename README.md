# 🌍 Global Happiness Report (2015–2023) – GDG Bowen University

This project analyzes the **World Happiness Report data (2015–2023)** as part of the **Google Developer Group on Campus (GDG) Data & ML Lead assessment** at Bowen University.

⚠️ **Note**: This version was completed before realizing the assignment required **2023 data only**. It still provides extended insights across multiple years and includes the full Stage 2 workflow.

---

## 📂 Project Structure

* **Notebooks/** → Jupyter notebooks for EDA & model training
* **models/** → Saved `.pkl` models (Linear Regression, CatBoost)
* **data/** → Cleaned & encoded dataset (2015–2023)
* **streamlit\_app.py** → Streamlit interface for predictions
* **requirements.txt** → Project dependencies
* **README\_STAGE2.md** → Detailed Stage 2 write-up for GDG application

---

## ⚡ Models Trained

1. **Linear Regression**
2. **CatBoost Regressor**

Both were evaluated on:

* **R² Score**
* **RMSE**
* **MSE**

CatBoost showed strong performance with non-linear relationships, while Linear Regression provided a simple interpretable baseline.

---

## 📖 Stage 2 Documentation

👉 Please see the detailed **Stage 2 README** in this project folder:
[Stage 2 README (2015–2023)](./README_STAGE2.md)
