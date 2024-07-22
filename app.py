# Streamlit web app
import streamlit as st
import openai
from streamlit.report_thread import add_report_ctx
import time

# Custom CSS
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #0f0f0f;
}
</style>
    """, unsafe_allow_html=True)

# Title & Icons
st.title(":tennis: Tennis Tutorial Assistant")
st.markdown("*A modern, sleek, and interactive tennis tutorial application.*")

# Text input for Open API Key
openai_api_key = st.text_input('Enter your OpenAI API Key', type='password')

# Text input for Tennis Tutorial Requests
request = st.text_input('What do you want to learn about tennis?')

# Create a button that when clicked, will take the input text and use chat models to generate a response
if st.button('Teach me!'):
    if openai_api_key != "":
        if request != "":
            st.success('Processing your request...')
            time.sleep(2)

            openai.api_key = openai_api_key

            add_report_ctx(None)
            
            # Your chat models
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant."
                    },
                    {
                        "role": "user",
                        "content": request
                    }
                ]
            )

            message_content = response['choices'][0]['message']['content'].strip()

            # Print chat model's response
            st.write(message_content)
        else:
            st.warning("Please enter your query!")
    else:
        st.warning("Please enter your OpenAI API Key!")