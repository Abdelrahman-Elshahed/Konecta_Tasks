import streamlit as st
import requests

st.title("Car Price Prediction [xgboost model]")

# ==== Inputs in Two Columns ====
col1, col2 = st.columns(2)

with col1:
    make_year = st.number_input("Make Year", 2000, 2025, step=1)

with col2:
    mileage_kmpl = st.number_input("Mileage (kmpl)", 0.0, 50.0)

col3, col4 = st.columns(2)

with col3:
    engine_cc = st.number_input("Engine (cc)", 500, 5000)

with col4:
    fuel_type = st.selectbox("Fuel Type", ["Diesel", "Petrol", "Electric"])

col5, col6 = st.columns(2)

with col5:
    owner_count = st.slider("Owner Count", 0, 10)

with col6:
    brand = st.selectbox("Brand", ["BMW", "Ford", "Toyota", "Honda", "Nissan", "Hyundai", "Volkswagen", "Kia", "Chevrolet", "Tesla"])

col7, col8 = st.columns(2)

with col7:
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

with col8:
    color = st.selectbox("Color", ["Black", "White", "Silver", "Gray", "Blue", "Red"])

col9, col10 = st.columns(2)

with col9:
    service_history = st.selectbox("Service History", ["Full", "Partial"])

with col10:
    accidents_reported = st.slider("Accidents Reported", 0, 5)

col11, _ = st.columns(2)

with col11:
    insurance_valid = st.selectbox("Insurance Valid", ["Yes", "No"])

# Convert "Yes"/"No" to int
insurance_valid = 1 if insurance_valid == "Yes" else 0
service_history = "Full" if service_history == "Full" else "No"  # Treat "Partial" as "No"

# ==== Submit Button ====
if st.button("Predict Price"):
    payload = {
        "make_year": make_year,
        "mileage_kmpl": mileage_kmpl,
        "engine_cc": engine_cc,
        "fuel_type": fuel_type,
        "owner_count": owner_count,
        "brand": brand,
        "transmission": transmission,
        "color": color,
        "service_history": service_history,
        "accidents_reported": accidents_reported,
        "insurance_valid": insurance_valid
    }

    try:
        res = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = res.json()
        st.success(f"Predicted Price: ${result['predicted_price_usd']}")
    except Exception as e:
        st.error("Failed to get prediction from API.")
        st.exception(e)