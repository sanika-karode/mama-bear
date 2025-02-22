import streamlit as st
import numpy as np
import pickle 
with open('mama_bear.pkl', 'rb') as file:
    model = pickle.load(file)


st.title("mama bear 🧸")
st.write("enter your specifications")

age = st.text_input("Enter your age")
sysBP = st.text_input("enter your systolic blood pressure")
diaBP = st.text_input("enter your diastolic BP")
bs = st.text_input("enter your blood sugar level")
temp = st.text_input("enter your temperature")
hr = st.text_input("enter your heart rate")

if st.button("predict"):
    features = np.array([[float(age), float(sysBP), float(diaBP), float(bs), float(temp), float(hr)]])
    prediction = model.predict(features)
    if prediction[0] == 0:
        risk = "Low Risk"
    elif prediction[0] == 1:
        risk = "Medium Risk"
    else:
        risk = "High Risk"
    st.write(f"Predicted Risk Level: {risk}")

    if risk == "Low Risk":
        st.write("You're all good. Keep going mama!")
    elif risk == "Medium Risk":
        st.write("bye")