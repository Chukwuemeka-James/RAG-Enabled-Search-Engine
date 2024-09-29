import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Wrappers for Arxiv and Wikipedia tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

# ---- PAGE SETUP ----
st.set_page_config(
    page_title="RAG-Enabled Search Engine",
    page_icon="🔎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- SIDEBAR ----
st.sidebar.title("🔧 Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password", help="The API key is required to use the LLM models.")

st.sidebar.markdown("💡 **Tip**: Try asking questions related to recent ML papers!")

# ---- HEADER ----
st.title("RAG-Enabled Search Engine")
st.markdown(
    """
    This interactive AI assistant uses **Llama 2** combined with Retrieval-Augmented Generation (RAG) techniques.
    You can ask research-related questions and retrieve accurate information from Arxiv, Wikipedia, and DuckDuckGo search.
    """
)

st.markdown("---")
# ---- WELCOME MESSAGE ----
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm your AI research assistant! How can I help you today?"}
    ]
# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# User Input
if prompt := st.chat_input(placeholder="Ask me about Machine Learning, AI, or recent research papers..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Chatbot functionality
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    tools = [search, arxiv, wiki]

    search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)

    with st.chat_message("assistant"):
        # Interactive callback for showing thoughts and actions
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])

        # Save assistant response in the chat history
        st.session_state.messages.append({'role': 'assistant', "content": response})
        st.write(response)

# ---- FOOTER ----
st.markdown("---")

