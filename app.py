from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if image is None:
        st.warning("Please upload an image.")
        return None
    
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    
    return response.text if response else None

st.set_page_config(page_title="Here we go!", page_icon=":gem:")

st.header("You and Me! Here we go!")

input_text = st.text_input("Enter your question here", key="unique_input_key")
uploaded_file = st.file_uploader("Select an image...", type=["jpg", "jpeg", "png"])

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Describe about the image")

if submit:
    response = get_gemini_response(input_text, image)
    if response is not None:
        st.subheader("Answer:> ")
        st.write(response)

 
 
