import streamlit as st
import numpy as np
import pickle
import pyrebase
from datetime import datetime

# Firebase Configuration
firebaseConfig = {
    'apiKey': "AIzaSyBt2E9uO--C9x4ZMl7mmvB4VCBueZIzfZc",
    'authDomain': "mama-bear-d5cfb.firebaseapp.com",
    'projectId': "mama-bear-d5cfb",
    'databaseURL': "mama-bear-d5cfb-default-rtdb.firebaseio.com",
    'storageBucket': "mama-bear-d5cfb.firebasestorage.app",
    'messagingSenderId': "282888877485",
    'appId': "1:282888877485:web:9e9ce8f8f2f2ad6c955d24",
    'measurementId': "G-SH06JEH22F"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# --- USER AUTHENTICATION --- 
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False  # Track login state

# --- PAGE CONFIG --- 
if st.session_state['logged_in']:
    st.set_page_config(page_title="Main App", layout="centered", initial_sidebar_state="collapsed")
else:
    st.set_page_config(page_title="Login", layout="centered")

# --- Login/SignUp Sidebar ---
def show_auth_form():
    choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up'])

    email = st.sidebar.text_input('Please enter your email address')
    password = st.sidebar.text_input('Please enter your password', type='password')

    if choice == 'Sign up':
        handle = st.sidebar.text_input('Please input your app handle name', value='Default')
        submit = st.sidebar.button('Create my account')

        if submit:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success('Your account is created successfully!')
                st.balloons()
                # After successful sign-up, log the user in
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state['logged_in'] = True
                #st.session_state['user_handle'] = email  # Store handle in session
                st.rerun()  # Rerun to load the main app page
            except Exception as e:
                st.error("Username already exists")
            
            

    if choice == 'Login':
        login = st.sidebar.button('Login')
        if login:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state['logged_in'] = True
                st.session_state['user_handle'] = email  # Store email or handle in session
                st.rerun()  # Rerun to load the main app page
            except Exception as e:
                # If login fails, show a general error message
                st.error("Incorrect Username/Passowrd")  # Show the error message from Firebase or network issues
# --- Main App (after login) ---
def show_main_app():
    with open('mama_bear.pkl', 'rb') as file:
        model = pickle.load(file)

    st.title("mama bear 🧸")
    st.write("Enter your specifications:")

    age = st.text_input("Enter your age")
    sysBP = st.text_input("Enter your systolic blood pressure")
    diaBP = st.text_input("Enter your diastolic BP")
    bs = st.text_input("Enter your blood sugar level")
    temp = st.text_input("Enter your temperature")
    hr = st.text_input("Enter your heart rate")

    if st.button("Predict"):
        try:
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
                st.write("Please take care and monitor your health.")
            else:
                st.write("Please consult a healthcare provider.")
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

    # Logout button
    if st.button("Log out"):
        st.session_state['logged_in'] = False
        st.session_state.pop('user_handle', None)  # Clear user handle
        st.rerun()  # Rerun to show login page again

# --- Main Application Flow ---
if st.session_state['logged_in']:
    show_main_app()  # Show main app if logged in
else:
    show_auth_form()  # Show auth form if not logged in
