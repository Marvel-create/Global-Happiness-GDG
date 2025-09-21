# Stage 2: Happiness Score Prediction

## Overview

This project predicts the **Happiness Score** for countries using historical World Happiness Report data. Two models were evaluated: **Linear Regression** and **CatBoost Regressor**. The final selected model is **CatBoost Regressor** due to its higher accuracy and ability to handle categorical features like `region`.

## Dataset

* Combined World Happiness Report datasets (2015–2023).
* Cleaned for missing values, duplicates, and outliers.
* Final cleaned dataset: `cleaned_data.csv`.

## Features

* **Numeric features:** GDP per capita, healthy life expectancy, freedom, generosity, perceptions of corruption, social support, etc.
* **Categorical features:** `region` (for CatBoost).
* **Dropped features:** `country` (not used in regression).

## Models

1. **Linear Regression** (numeric features only)

   * R² Score: 0.701
   * RMSE: 0.552
   * 10-Fold CV R² Score: 0.712 ± 0.037

2. **CatBoost Regressor** (numeric + categorical features)

   * R² Score: 0.858
   * RMSE: 0.380
   * 10-Fold CV R² Score: 0.824

**Reason for choosing CatBoost:**

* Handles categorical features directly.
* Higher accuracy (R² & RMSE).
* Better cross-validation performance.

## How to Use

1. Load the cleaned dataset: `cleaned_data.csv`.
2. Run the `Stage2_Prediction_Pipeline.ipynb` notebook.
3. The final trained **CatBoost model** is saved as:

   ```
   catboost_final_model.pkl
   ```
4. Use `joblib.load("catboost_final_model.pkl")` to load the model and make predictions on new data.

## Requirements

* Python 3.x
* Packages: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `catboost`, `joblib`
