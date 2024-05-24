import streamlit as st
from chatbot import Chatbot

Chatbot = Chatbot()

st.write('# Hello, world!\n\nThis is a simple example of a Streamlit app.')

input = st.text_input('Enter your name')

output = Chatbot.chat(input)

st.write(output)