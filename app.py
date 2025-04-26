import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("energy_theft_model.pkl")

st.title("Energy Theft Detection")

st.write("Enter 8 feature values:")

# 8 inputs
features = []
for i in range(8):
    value = st.number_input(f"Feature {i+1}", step=0.1)
    features.append(value)

# Predict button
if st.button("Predict"):
    prediction = model.predict([features])
    if prediction[0] == 1:
        st.error("⚠️ Theft Detected!")
    else:
        st.success("✅ No Theft Detected.")
