import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

# Set page title and favicon
st.set_page_config(
    page_title="HuberMind AI", 
    page_icon="⚗️",  # You can use an emoji or a path to an image file
)
# Set the title of the app
# st.title("HuberMind AI ⚗️")

st.markdown("<h1 style='text-align: center'>HuberMind AI ⚗️</h1>", unsafe_allow_html=True)

# Create a text input for the user to enter their question
question = st.text_input("Ask Andrew:")

# Create a button for submitting the question
if st.button("Submit") or question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)
    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
