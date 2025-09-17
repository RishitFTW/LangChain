from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

st.header('AI Summarizer')

user_input= st.text_input("Enter the research paper")

response= model.invoke(user_input)

if st.button('summarize'):
    st.write(response.content)