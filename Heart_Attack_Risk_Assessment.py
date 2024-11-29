
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
# Input field for Gender
Gender = st.selectbox('Select Gender:', options=['Male', 'Female', 'Other'])

# Encoding the selected gender
gender_mapping = {'Male': 0, 'Female': 1, 'Other': 2}
gender_encoded = gender_mapping[Gender]

Age = st.number_input('Age (AGE)', min_value=1.0, max_value=100.0, value= 100.0, step=0.1)
BloodPressure = st.number_input('Blood Pressure (mmHg) (BLOOD_PRESSURE(mmHg))', min_value=0.0, max_value=150.0,value = 10.0, step=0.1)
Cholesterol  = st.number_input('Cholesterol (mg/dL) (CHOLESTEROL)', min_value=0.0, max_value=100.0,value = 100.0, step=0.1)
# Input field for Diabetes
Diabetes = st.selectbox('Does the person have Diabetes?', options=['No', 'Yes'])

# Map the selected option to a numeric value
diabetes_mapping = {'No': 0, 'Yes': 1}
diabetes_encoded = diabetes_mapping[diabetes]

SmokingStatus = st.number_input('Smoking Status (SMOKING_STATUS)', min_value=0.0, max_value=10.0, value = 10.0, step=1.0)
ChestPainType = st.number_input('Chest Pain Type (CHEST_PAIN_TYPE)', min_value=0.0, max_value=10.0, value=5.0, step=1.0)

st.write(f"Encoded Gender: {gender_encoded}")
st.write(f"Encoded Diabetes Value: {diabetes_encoded}")

# Create a dictionary with the input data
input_data = {
    'Gender': Gender,
    'Age': age,
    'Blood Pressure (mmHg)': BloodPressure,
    'Cholesterol (mg/dL)': Cholesterol,
    'Diabetes': Diabetes,
    'Smoking Status': SmokingStatus,
    'Chest Pain Type': ChestPainType,
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

