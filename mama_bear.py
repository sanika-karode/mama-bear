import streamlit as st
import numpy as np
import pickle 
from pathlib import Path
import streamlit_authenticator as stauth
import pyrebase
from datetime import datetime

# Configuration Key
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

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Our community app")

# Authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password',type = 'password')

# App 

# Sign up Block
if choice == 'Sign up':
    handle = st.sidebar.text_input(
        'Please input your app handle name', value='Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created suceesfully!')
        st.balloons()
        # Sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome' + handle)
        st.info('Login via login drop down selection')

# Login Block
if choice == 'Login':
    login = st.sidebar.button('Login')
    if login:
        try: 
            user = auth.sign_in_with_email_and_password(email,password)
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        except:
            st.error("Username/Password is incorrect")

# --- USER AUTHENTICATION ---

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

