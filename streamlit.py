import streamlit as st
import os
from langchain_core.messages import HumanMessage

# Check if API key is configured
if not os.getenv("OPENAI_API_KEY"):
    try:
        if "OPENAI_API_KEY" not in st.secrets:
            st.error("⚠️ Error: OPENAI_API_KEY is not configured!")
            st.info("""
            To use this chatbot, please add your OpenAI API key:
            
            **On Streamlit Cloud:**
            1. Go to your app settings (⋮ menu)
            2. Click "Secrets"
            3. Add: `OPENAI_API_KEY = "your-api-key"`
            4. Save and the app will restart
            
            **Locally:**
            1. Create a `.env` file in the project directory
            2. Add: `OPENAI_API_KEY=your-api-key`
            """)
            st.stop()
    except:
        st.error("⚠️ Error: OPENAI_API_KEY is not configured!")
        st.stop()

from chatbot_graph import chatbot

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

st.set_page_config(page_title="LangGraph Chatbot", page_icon="💬", layout="centered")
st.title("💬 LangGraph Chatbot")
st.markdown("*Powered by OpenAI GPT & LangGraph*")

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_input = st.chat_input('Type your message here...')

if user_input:
    # Add user message to history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.write(user_input)

    try:
        # Get response from chatbot
        response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
        
        ai_message = response['messages'][-1].content
        # Add assistant message to history
        st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
        with st.chat_message('assistant'):
            st.write(ai_message)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.session_state['message_history'].pop()  # Remove the user message if there was an error