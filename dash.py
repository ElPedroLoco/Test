import streamlit as st
import requests

response = requests.get('http://ec2-35-181-155-27.eu-west-3.compute.amazonaws.com:5000/data')
data = response.json()
st.write(f"Data from Flask: {data['value']}")
