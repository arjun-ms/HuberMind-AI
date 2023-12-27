import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))


# Set the title of the app
st.title("Ask Andrew!")

# Create a text input for the user to enter their question
question = st.text_input("Enter your question:")

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
