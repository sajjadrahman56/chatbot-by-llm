from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def get_response(input_text):
     response = model.generate_content(input_text)
     return response.text

st.set_page_config(page_title="Q & A", page_icon=":gem:")
st.header("I am your FRIEND Gemini")
st.subheader("Ask me anything and I will try to answer it for you as best as I can" )

input = st.text_input("Enter your question here", key="input")
submit = st.button("Submit")


if submit:
     response = get_response(input)
     st.subheader("The Response is :")
     st.write(response)
