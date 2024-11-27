
# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load("HeartRisk.py")  

# Set up the Streamlit app
st.title('Heart Attack Risk Assessment')
st.write("This app predicts the risk of heart attack/disease based on treatment.")

# Input fields for user to enter feature values
Gender = st.number_input('Gender (GENDER)', min_value=0.0, max_value=2.0, value=10.0, step=1.0)
Age = st.number_input('Age (AGE)', min_value=1.0, max_value=100.0, value= 100.0, step=0.1)
Blood_pressure = st.number_input('Blood Pressure (mmHg) (BLOOD_PRESSURE(mmHg))', min_value=0.0, max_value=150.0,value = 10.0, step=0.1)
Cholesterol  = st.number_input('Cholesterol (mg/dL) (CHOLESTEROL)', min_value=0.0, max_value=100.0,value = 100.0, step=0.1)
Diabetes = st.number_input('Has Diabetes (DIABETES)', min_value=0.0, max_value=200.0,value = 200.0, step=1.0)
Smoking_status = st.number_input('Smoking Status (SMOKING_STATUS)', min_value=0.0, max_value=10.0, value = 10.0, step=1.0)
Chest_pain_type = st.number_input('Chest Pain Type (CHEST_PAIN_TYPE)', min_value=0.0, max_value=10.0, value=5.0, step=1.0)

# Create a dictionary with the input data
input_data = {
    'GENDER':Gender,
    'AGE':age,
    'BLOOD_PRESSURE':Blood Pressure (mmHg),
    'CHOLESTEROL':Cholesterol (mg/dL),
    'DIABETES':Has Diabetes,
    'SMOKING_STATUS':Smoking Status,
    'CHEST_PAIN_TYPE':Chest Pain Type
}

# Convert the dictionary to a DataFrame
input_df = pd.DataFrame([input_data])

# Predict churn probability using the loaded model
if st.button('Predict Risk Of Heart Attack'):
   attack_prediction = model.predict_proba(input_df)[:, 1]  # Probability of churn
    attack_probability = round(prediction[0] * 100, 2)
    st.write(f"The predicted heart attack/disease probability is {attack_probability}%")

# Option to display input data
if st.checkbox('Show Input Data'):
    st.write(input_df)

