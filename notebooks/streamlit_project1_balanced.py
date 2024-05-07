import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Loading the trained model
model_file = '/Users/harikatamma/Downloads/DATA606/decision_tree_model.joblib'
model = joblib.load(model_file)


model.feature_names_in_ = ['age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
       'diaBP', 'prevalentStroke','BMI', 'glucose']


mappings = {
    'currentSmoker': {'Yes': 1, 'No': 0},
    'BPMeds': {'Yes': 1, 'No': 0},
    'prevalentHyp': {'Yes': 1, 'No': 0},
    'diabetes': {'Yes': 1, 'No': 0},
    'prevalentStroke': {'Yes': 1, 'No': 0}

}

def predict_risk(data):
    # Create a DataFrame with the user input data
    data_new = pd.DataFrame(data, index=[0])
    # Map categorical inputs to numerical values
    for col, mapping in mappings.items():
        data_new[col] = data_new[col].map(mapping)
    # Make prediction
    prediction = model.predict(data_new)
    return prediction

    
def main():
    html_temp = """
    <div style="background-color: lightblue;padding:16px">
    <h2 style="color:black;text-align:center;">Heart Disease Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown("##### Welcome to the Heart Disease Prediction App!")
    st.markdown("##### Please provide the following information to predict the likelihood of heart disease.")

    st.write('')
    st.write('')

    # Collect user inputs
    age = st.number_input("Age", min_value=0, max_value=150, value=50, step=1)
    currentSmoker = st.selectbox("Is the patient a current smoker?", ['Yes', 'No'])
    cigsPerDay = st.number_input("Average cigarettes per day", min_value=0, max_value=100, value=0, step=1)
    BPMeds = st.selectbox("Is the patient on blood pressure medication?", ['Yes', 'No'])
    
    prevalentHyp = st.selectbox("Does the patient have a history of hypertension?", ['Yes', 'No'])
    diabetes = st.selectbox("Does the patient have diabetes?", ['Yes', 'No'])
    totChol = st.number_input("Total cholesterol (mg/dL)", min_value=0, max_value=600, value=200, step=1)
    sysBP = st.number_input("Systolic blood pressure (mmHg)", min_value=0, max_value=300, value=120, step=1)
    diaBP = st.number_input("Diastolic blood pressure (mmHg)", min_value=0, max_value=200, value=80, step=1)
    prevalentStroke = st.selectbox("Has the patient had a stroke before?", ['Yes', 'No'])
    BMI = st.number_input("Body mass index (kg/m^2)", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
    glucose = st.number_input("Glucose level (mg/dL)", min_value=0, max_value=600, value=100, step=1)

    # Prepare data for prediction
    data = {
        'age': age,
        'currentSmoker': currentSmoker,
        'cigsPerDay': cigsPerDay,
        'BPMeds': BPMeds,
        'prevalentHyp': prevalentHyp,
        'diabetes': diabetes,
        'totChol': totChol,
        'sysBP': sysBP,
        'diaBP': diaBP,
        'prevalentStroke': prevalentStroke,
        'BMI': BMI,
        'glucose': glucose
    }

    # Perform prediction
    if st.button('Predict'):
        prediction = predict_risk(data)
        if prediction == 1:
            st.error('You have a high risk of heart disease. Please consult a doctor.')
        else:
            st.success('You have a low risk of heart disease. Stay healthy!')

if __name__ == '__main__':
    main()