import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title('🚗 Car Price Prediction App')

# Sidebar
st.sidebar.header('Input Car Specifications')

# Input features
def user_input_features():
    year = st.sidebar.number_input('Year of Purchase', 1990, 2025, step=1, value=2015)
    present_price = st.sidebar.number_input('Showroom Price (in Lakhs)', min_value=0.0, max_value=100.0, value=5.0)
    kms_driven = st.sidebar.number_input('Kilometers Driven', 0, 1000000, step=1000, value=30000)
    owner = st.sidebar.selectbox('Number of Previous Owners', [0, 1, 2, 3])
    fuel_type = st.sidebar.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
    seller_type = st.sidebar.selectbox('Seller Type', ['Dealer', 'Individual'])
    transmission = st.sidebar.selectbox('Transmission Type', ['Manual', 'Automatic'])

    # Manual encoding as done in your notebook
    fuel_Petrol = 1 if fuel_type == 'Petrol' else 0
    fuel_Diesel = 1 if fuel_type == 'Diesel' else 0

    seller_type_individual = 1 if seller_type == 'Individual' else 0
    transmission_manual = 1 if transmission == 'Manual' else 0

    car_age = 2020 - year  # assuming model was trained on data up to 2020

    features = np.array([[present_price, kms_driven, owner, car_age,
                          fuel_Diesel, fuel_Petrol, seller_type_individual, transmission_manual]])
    
    return features

# Predict button
if st.button('Predict Car Price'):
    input_data = user_input_features()
    prediction = model.predict(input_data)
    st.success(f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")
