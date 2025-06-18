from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load model
model = joblib.load('../models/car_price_xgboost_model.pkl')


# Input schema
class CarFeatures(BaseModel):
    make_year: int
    mileage_kmpl: float
    engine_cc: int
    fuel_type: str
    owner_count: int
    brand: str
    transmission: str
    color: str
    service_history: str
    accidents_reported: int
    insurance_valid: int

# ========== Preprocessing function ==========
def prepare_input(df):
    df = df.copy()
    df['car_age'] = 2025 - df['make_year']

    def categorize_owner(x):
        if x <= 1:
            return '1'
        elif x <= 3:
            return '2-3'
        else:
            return '4+'
    df['owner_category'] = df['owner_count'].apply(categorize_owner)

    one_hot_cols = {
        'fuel_type': ['Electric', 'Petrol'],
        'brand': ['Chevrolet', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Nissan', 'Tesla', 'Toyota', 'Volkswagen'],
        'color': ['Blue', 'Gray', 'Red', 'Silver', 'White'],
        'owner_category': ['2-3', '4+']
    }


    df['transmission'] = df['transmission'].map({'Manual': 0, 'Automatic': 1})
    df['service_history'] = df['service_history'].map({'No': 0, 'Yes': 1})

    for col, categories in one_hot_cols.items():
        for cat in categories:
            df[f"{col}_{cat}"] = (df[col] == cat).astype(int)

    drop_cols = ['fuel_type', 'brand', 'color', 'owner_category', 'price_usd']
    df.drop(columns=[c for c in drop_cols if c in df.columns], inplace=True)

    model_features = [
        'make_year', 'mileage_kmpl', 'engine_cc', 'owner_count',
        'transmission', 'service_history', 'accidents_reported',
        'insurance_valid', 'car_age', 'fuel_type_Electric',
        'fuel_type_Petrol', 'brand_Chevrolet', 'brand_Ford',
        'brand_Honda', 'brand_Hyundai', 'brand_Kia', 'brand_Nissan',
        'brand_Tesla', 'brand_Toyota', 'brand_Volkswagen',
        'color_Blue', 'color_Gray', 'color_Red', 'color_Silver',
        'color_White', 'owner_category_2-3', 'owner_category_4+'
    ]

    for col in model_features:
        if col not in df.columns:
            df[col] = 0

    return df[model_features]

# ========== Prediction Endpoint ==========
@app.post("/predict")
def predict_price(data: CarFeatures):
    input_df = pd.DataFrame([data.dict()])
    input_prepared = prepare_input(input_df)
    prediction = float(model.predict(input_prepared)[0])
    return {"predicted_price_usd": round(prediction, 2)}
