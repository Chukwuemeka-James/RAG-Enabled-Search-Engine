import streamlit as st

def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="RAG-Enabled Search Engine",
        page_icon="🔎",
        layout="centered",
        initial_sidebar_state="expanded"
    )

def show_footer():
    """Show footer for the app"""
    st.markdown("---")
