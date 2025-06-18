# Car Price Prediction System

A comprehensive machine learning project that predicts used car prices using Random Forest and XGBoost models, with both FastAPI and Streamlit interfaces for deployment.

## Project Structure

```
├── app/
│   ├── app.py                    # FastAPI backend
│   └── streamlit_app.py          # Streamlit frontend
├── data/
│   └── used_car_price_dataset_extended.csv  # Dataset
├── models/
│   ├── car_price_rf_model.pkl    # Trained Random Forest model
│   └── car_price_xgboost_model.pkl  # Trained XGBoost model
├── notebook/
│   └── Assignment4.ipynb         # Complete ML pipeline notebook
├── assets/
│   ├── fastapi.png              # FastAPI interface screenshot
│   └── streamlit.png            # Streamlit interface screenshot
├── Dockerfile                   # Container configuration
├── requirements.txt             # Python dependencies
├── .gitignore                  # Git ignore rules
└── Steps.pdf                   # Project documentation
```

## Project Overview

This project implements a complete machine learning pipeline for predicting used car prices using advanced regression techniques. The system includes comprehensive data analysis, feature engineering, model training, and deployment through both API and web interfaces.


![Image](https://github.com/user-attachments/assets/247f6c6c-1422-4b2a-95e5-81960479a613)


## Key Features

- **Comprehensive EDA**: Detailed exploratory data analysis with visualizations
- **Feature Engineering**: Advanced feature creation including car age and owner categorization
- **Multiple Models**: Random Forest and XGBoost implementations with hyperparameter tuning
- **Dual Interface**: Both FastAPI REST API and Streamlit web interface
- **Containerization**: Docker support for easy deployment
- **Model Persistence**: Trained models saved using joblib

## Dataset Features

The dataset includes the following features:
- **make_year**: Manufacturing year of the car
- **mileage_kmpl**: Fuel efficiency in kilometers per liter
- **engine_cc**: Engine capacity in cubic centimeters
- **fuel_type**: Type of fuel (Petrol, Diesel, Electric)
- **owner_count**: Number of previous owners
- **brand**: Car manufacturer (BMW, Toyota, Honda, etc.)
- **transmission**: Transmission type (Manual, Automatic)
- **color**: Car color
- **service_history**: Service maintenance record (Full, Partial)
- **accidents_reported**: Number of reported accidents
- **insurance_valid**: Insurance validity status
- **price_usd**: Target variable - car price in USD

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abdelrahman-Elshahed/Konecta_Tasks.git
    cd Assignment_4
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the applications**
   
   **FastAPI Backend:**
   ```bash
   cd app
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
   
   **Streamlit Frontend:**
   ```bash
   cd app
   streamlit run streamlit_app.py --server.port 8501
   ```

### Using Docker

```bash
# Build and run with Docker
docker build -t car-price-prediction .
docker run -p 8000:8000 -p 8501:8501 car-price-prediction
```


## API Usage

### FastAPI Endpoint
![Image](https://github.com/user-attachments/assets/19231679-43b6-4db5-9ac8-bda17ec602d4)

**POST** `/predict`

**Request Body:**
```json
{
  "make_year": 2015,
  "mileage_kmpl": 20.23,
  "engine_cc": 4000,
  "fuel_type": "Diesel",
  "owner_count": 5,
  "brand": "Kia",
  "transmission": "Manual",
  "color": "White",
  "service_history": "Full",
  "accidents_reported": 1,
  "insurance_valid": 1
}
```

**Response:**
```json
{
  "predicted_price_usd": 9775.36
}
```
