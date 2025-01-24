import streamlit as st
from transformers import pipeline

st.title("English To French Translator")

pipe = pipeline("text2text-generation", model="Shyam-duba/my_awesome_opus_books_model")

@st.cache_data
def process_text(text):
    return pipe("translate English to French: "+text)

text = st.text_input("Please Enter text in English")
submit = st.button("Submit")
if submit and text:
    st.write(f"French Text : {process_text(text)[0]['generated_text']}")
