import streamlit as st
from settings import load_config
from chat import initialize_chat, display_chat_history, handle_user_input
from agent import create_agent, run_agent
from utils import configure_page, show_footer

# Load configuration
api_key = load_config()

# Page Setup
configure_page()

# Sidebar Settings
st.sidebar.title("🔧 Settings")
st.sidebar.text_input("Enter your Groq API Key:", type="password", help="The API key is required to use the LLM models.")

# Header
st.title("RAG-Enabled Search Engine")
st.markdown(
    """
    This interactive AI assistant uses **Llama 2** combined with Retrieval-Augmented Generation (RAG) techniques.
    You can ask research-related questions and retrieve accurate information from Arxiv, Wikipedia, and DuckDuckGo search.
    """
)

# Initialize chat and display history
initialize_chat()
display_chat_history()

# Handle user input
prompt = handle_user_input()

# If user input exists, process and generate response
if prompt:
    agent = create_agent(api_key)
    response = run_agent(agent, st.session_state.messages)
    
    # Display assistant's response
    st.session_state.messages.append({'role': 'assistant', "content": response})
    st.write(response)

# Show footer
show_footer()
