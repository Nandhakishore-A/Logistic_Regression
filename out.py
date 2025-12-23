import streamlit as st
import joblib
import numpy as np

# ✅ Page configuration MUST be first Streamlit command
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

# Load model & encoder
model = joblib.load("model.pkl")
sex_encoder = joblib.load("sex_encoder.pkl")

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict survival")

# User inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Gender", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=30)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=50.0)

# Encode gender
sex_encoded = sex_encoder.transform([sex])[0]

# Prediction
if st.button("Predict Survival"):
    input_data = np.array([[pclass, sex_encoded, age, fare]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")
