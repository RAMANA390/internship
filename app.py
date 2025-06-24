import streamlit as st
import pickle
import numpy as np

# Load model and encoder
model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

# Location options
locations = encoder.classes_

st.title("Welcome To House Price Predictor")

location = st.selectbox("Select the Location", locations)
bhk = st.number_input("Enter BHK", min_value=1, max_value=10, step=1)
bath = st.number_input("Enter Number of Bathrooms", min_value=1, max_value=10, step=1)
sqft = st.number_input("Enter Square Feet", min_value=100)

if st.button("Predict Price"):
    loc_encoded = encoder.transform([location])[0]
    input_data = np.array([[loc_encoded, bhk, bath, sqft]])
    prediction = model.predict(input_data)[0]
    st.success(f"Prediction: ₹ {round(prediction, 2)}")
