import streamlit as st
import json
import random

# Load knowledge base
with open('knowledge_base.json', 'r') as f:
    data = json.load(f)

def get_response(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return data['fallback']

# Streamlit UI
st.title("Fitness & Workout Assistant")
st.write("Hello! How can I help you train today?")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})