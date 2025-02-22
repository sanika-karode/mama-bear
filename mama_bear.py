import streamlit as st
import numpy as np
import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

# --- USER AUTHENTICATION ---
names = ["pp", "rj"]
usernames = ["rp", "sk"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "mama_bear", "abcdef", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login", "main")
if authentication_status == False:
    st.error("Username/Password is incorrect. Try again")
elif authentication_status == None:
    st.warning("Please enter Username and Password.")
elif authentication_status:
    authenticator.logout("Log Out", "sidebar")
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