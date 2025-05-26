# Insurance Cost Prediction

A machine learning web application that predicts medical insurance costs based on personal attributes using Random Forest Regression.


## Table of Contents

  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Dataset](#dataset)
  - [Project Structure](#project-structure)
  - [Installation and Setup](#installation-and-setup)
  - [Run with Streamlit Application](#run-with-streamlit-application)
  - [Usage](#usage)
  - [Model Performance](#model-performance)



## Project Overview

This project uses a Random Forest model trained on insurance data to predict medical insurance costs. The application is built with Streamlit and provides an interactive interface for users to input their information and receive cost estimates.
![Image](https://github.com/user-attachments/assets/c350ff77-724b-4346-bdd2-19fd97d87779)

## Features

- Interactive web interface built with Streamlit
- Random Forest Regression model for accurate predictions
- Real-time cost estimation based on user inputs
- Comprehensive data analysis and visualization
- Docker containerization for easy deployment

## Dataset

The model is trained on insurance data with the following features:
- **Age**: Age of the primary beneficiary
- **Sex**: Insurance contractor gender (female/male)
- **BMI**: Body mass index
- **Children**: Number of children/dependents covered
- **Smoker**: Smoking status (yes/no)
- **Region**: Beneficiary's residential area (northeast, northwest, southeast, southwest)
- **Charges**: Individual medical costs billed by health insurance

## Project Structure

```
Assignment_1/
├── app/
│   └── app.py              # Streamlit web application
│
├── assets/                # Screenshots and images for documentation
│
├── data/
│   └── Insurance.csv       # Dataset
├── model/
│   └── insurance_model.pkl # Trained Random Forest model
├── notebook/
│   └── Assignment1.ipynb   # Jupyter notebook with analysis
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Installation and Setup

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abdelrahman-Elshahed/Konecta_Tasks.git
   cd Assignment_1
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Docker Setup

1. **Build Docker image**
   ```bash
   docker build -t insurance-prediction .
   ```

2. **Run Docker container**
   ```bash
   docker run -p 8501:8501 insurance-prediction
   ```

3. **Access the application**
   Open your browser and navigate to `http://localhost:8501`


## Run with Streamlit Application

   - Run the application
     ```bash
     cd app
     streamlit run app.py
     ```
   - The application will be available at [http://localhost:8501](http://localhost:8501/).


![Image](https://github.com/user-attachments/assets/ac2c7c73-c0c1-4759-a1c0-3320043121a9)

![Image](https://github.com/user-attachments/assets/9bf09950-cb46-47fa-97c6-fb3f033b0056)

## Usage

1. **Input Parameters**: Use the sliders and dropdowns to enter your information:
   - Age (18-64 years)
   - BMI (15.0-54.0)
   - Number of children (0-5)
   - Smoking status
   - Gender
   - Region

2. **Get Prediction**: Click the "Predict Insurance Cost" button to receive your estimated insurance cost

3. **View Results**: The application displays:
   - Estimated insurance cost
   - Input summary
   - Model information

## Model Performance

The Random Forest Regression model achieves:
- **R² Score**: High coefficient of determination
- **Low MAE**: Mean Absolute Error
- **Low RMSE**: Root Mean Square Error

Key insights from the model:
- Smoking status is the strongest predictor of insurance costs
- Age positively correlates with insurance costs
- BMI above 30 (obesity) increases costs significantly
- Number of dependents affects pricing

## Data Processing

The project includes comprehensive data preprocessing:
- **Missing Values**: Checked and handled
- **Duplicates**: Removed if present
- **Encoding**: 
  - Label encoding for binary smoker variable
  - One-hot encoding for categorical variables (sex, region)
- **Feature Engineering**: Age group categorization


