import streamlit as st
from chatbot import Chatbot
import streamlit as st


Chatbot = Chatbot()

st.title('Chatbot')

#initializing the chatbot
if "chatbot" not in st.session_state:
    st.session_state.chatbot = []

#Display chat message from history
for message in st.session_state.chatbot:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Chatbot: {message['content']}")

# React to user input
if prompt := st.chat_input("You:"):
    st.chat_message("You:").markdown(prompt)
    #add user input to chat history
    st.session_state.chatbot.append({"role": "user", "content": prompt})

    response = Chatbot.chat(prompt)

    #Display chat message from history
    with st. chat_message("Chatbot:"):
        st.markdown(response)
    #add assistant response to chat history
    st.session_state.chatbot.append({"role": "system", "content": response})

