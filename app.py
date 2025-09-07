import streamlit as st  
import numpy as np
import joblib 

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit the predict for getting prediction.")


st.divider()

age = st.number_input("Enter Age",min_value=12,max_value=83,value=25)

gender = st.selectbox("Select Gender",options=["Male","Female"])

tenure = st.number_input("Enter Tenure",min_value=0,max_value=130,value=10)

monthly_charges = st.number_input("Enter Monthly Charges",min_value=0,max_value=1000,value=50)

st.divider()

predictButton = st.button("Predict")

if predictButton:
  gender_selected = 1 if gender == "Female" else 0

  x_arr = scaler.transform(np.array([[age,gender_selected,tenure,monthly_charges]]))

  prediction = model.predict(x_arr)[0]
  
  predicted = "Yes" if prediction == 1 else "No"

  st.write(f"Predicted Churn: {predicted}")

  
else:
  st.write("Please enter the values and hit the predict for getting prediction.")