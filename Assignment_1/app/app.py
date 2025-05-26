import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('../model/insurance_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set page title
st.title('Insurance Cost Prediction')
st.write('Enter your information to get an estimated insurance cost')

# Create input fields
col1, col2 = st.columns(2)

with col1:
    age = st.slider('Age', 18, 64, 30)
    bmi = st.slider('BMI', 15.0, 54.0, 25.0, 0.1)
    children = st.slider('Number of Children', 0, 5, 0)

with col2:
    smoker = st.selectbox('Smoker', ['No', 'Yes'])
    sex = st.selectbox('Sex', ['Female', 'Male'])
    region = st.selectbox('Region', ['Northeast', 'Northwest', 'Southeast', 'Southwest'])

# Create a button to trigger prediction
if st.button('Predict Insurance Cost'):
    # Process inputs
    smoker_encoded = 1 if smoker == 'Yes' else 0
    sex_male = 1 if sex == 'Male' else 0
    
    # Initialize region columns with zeros
    region_northwest = 0
    region_southeast = 0
    region_southwest = 0
    
    # Set the appropriate region column to 1
    if region == 'Northwest':
        region_northwest = 1
    elif region == 'Southeast':
        region_southeast = 1
    elif region == 'Southwest':
        region_southwest = 1
    
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker_encoded],
        'sex_male': [sex_male],
        'region_northwest': [region_northwest],
        'region_southeast': [region_southeast],
        'region_southwest': [region_southwest]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result
    st.success(f'Estimated Insurance Cost: ${prediction:.2f}')
    
    # Display input summary
    st.subheader('Input Summary')
    st.write(f"Age: {age}")
    st.write(f"BMI: {bmi}")
    st.write(f"Children: {children}")
    st.write(f"Smoker: {smoker}")
    st.write(f"Sex: {sex}")
    st.write(f"Region: {region}")

# Add an explanation section
with st.expander("About the Model"):
    st.write("""
    This application uses a Random Forest Regression model trained on insurance data.
    The model predicts medical insurance costs based on personal attributes.
    
    Key factors that influence insurance costs:
    - Being a smoker significantly increases costs
    - Age correlates with higher insurance costs
    - BMI above 30 (obese range) leads to higher costs
    - Number of children/dependents affects pricing
    """)