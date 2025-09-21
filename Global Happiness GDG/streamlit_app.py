import numpy
import streamlit as st
import pandas as pd
import pickle
from catboost import CatBoostRegressor, Pool


with open("final_model.pkl", "rb") as f:
    cat_model = pickle.load(f)

st.title("🌍 Global Happiness Predictor")

# User inputs

region = st.selectbox(
    "Region",
    [
        "Sub-Saharan Africa",
        "Central and Eastern Europe",
        "Latin America and Caribbean",
        "Middle East and North Africa",
        "Western Europe",
        "South Asia",
        "Southeast Asia",
        "East Asia",
        "Commonwealth of Independent States",
        "North America and ANZ"
    ]
)

gdp = st.number_input("GDP per capita", min_value=0.0, max_value=2.0, value=1.0, step=0.10)
social_support = st.number_input("Social support", min_value=0.0, max_value=1.5, value=1.0, step=0.10)
life_expectancy = st.number_input("Healthy life expectancy", min_value=0.0, max_value=1.5, value=0.8, step=0.10)
freedom = st.number_input("Freedom to make life choices", min_value=0.0, max_value=1.0, value=0.5, step=0.10)
generosity = st.number_input("Generosity", min_value=0.0, max_value=1.0, value=0.2, step=0.10)
corruption = st.number_input("Perceptions of corruption", min_value=0.0, max_value=1.0, value=0.3, step=0.10)
year = st.number_input("Year", min_value=2005, max_value=2025, value=2020, step=1)


# Build input DataFrame

input_df = pd.DataFrame({
    "region": [region],
    "gdp_per_capita": [gdp],
    "social_support": [social_support],
    "healthy_life_expectancy": [life_expectancy],
    "freedom_to_make_life_choices": [freedom],
    "generosity": [generosity],
    "perceptions_of_corruption": [corruption],
    "year": [year]
})


#Now to the Prediction
if st.button("Predict Happiness Score"):
    input_pool = Pool(input_df, cat_features=["region"])
    prediction = cat_model.predict(input_pool)[0]

    # Convert to float it gave numpy formatting error
    prediction = float(prediction)

    st.success(f"🌟 Predicted Happiness Score: {prediction:.2f}")

    # Visualization: scale score between 2 and 8
    scaled_score = min(max(prediction, 2), 8) 
    st.write("📊 World Happiness Scale (2 = Low, 8 = High)")
    st.progress((scaled_score - 2) / 6) 
