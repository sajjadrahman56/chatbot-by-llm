from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("You and Me ! Here we go !! ")

input = st.text_input("Enter your question here", key="unique_input_key")
uploaded_file = st.file_uploader("select an image...", type=["jpg", "jpeg", "png"])

image=""   

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)


# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os 
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-pro")

# def get_response(input_text):
#      response = model.generate_content(input_text)
#      return response.text

# st.set_page_config(page_title="Q & A", page_icon=":gem:")

# st.header("Here you GO...!")
# input = st.text_input("Enter your question here", key="input")

# input = st.text_input("Enter your question here", key="input")
# submit = st.button("Submit")


# if submit:
#      response = get_response(input)
#      st.subheader("The Response is :")
#      st.write(response)
