import streamlit as st
import requests

st.title('Hello, Streamlit!')
st.write('This is a Streamlit app running alongside a Flask app.')

url = 'http://ec2-35-181-155-27.eu-west-3.compute.amazonaws.com:5000/predict_client'  # Replace with your Flask server's public DNS and port
data = {
    "key1": "value1",
    "key2": "value2"
}

if st.button('Send Request'):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.write(f"Error: {response.status_code}")
