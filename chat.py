import streamlit as st

def initialize_chat():
    """Initialize chat session state if not already initialized"""
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hi, I'm your AI research assistant! How can I help you today?"}
        ]

def display_chat_history():
    """Display the chat history"""
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg['content'])

def handle_user_input():
    """Handle user input and append to the chat history"""
    if prompt := st.chat_input(placeholder="Ask me about Machine Learning, AI, or recent research papers..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        return prompt
    return None
