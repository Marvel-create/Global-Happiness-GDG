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

### 📊 Model Performance

| Model              | R² Score | RMSE   | MSE    |
| ------------------ | -------- | ------ | ------ |
| Linear Regression  | 0.7876   | 0.5356 | 0.2869 |
| CatBoost Regressor | 0.7789   | 0.5466 | 0.2987 |

🔎 **Observation**:

* Linear Regression provided a simple and interpretable baseline.
* CatBoost handled non-linear relationships but performed slightly worse here.

---

## 📖 Stage 2 Documentation

👉 Please see the detailed **Stage 2 README** in this project folder:
[Stage 2 README (2015–2023)](./README_STAGE2.md)

---

## 🛠️ How to Run

Clone this repo:

```bash
git clone https://github.com/<marvel-create/global-happiness-2015-2023.git
cd global-happiness-2015-2023
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

