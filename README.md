# RAG-Enabled Search Engine

This interactive AI assistant leverages the power of **Llama 2** combined with Retrieval-Augmented Generation techniques. Users can engage in a conversation about Machine Learning, AI, or recent research papers, and receive relevant information in real time.

## Features

- **Research Assistance**: Retrieve accurate information from reputable sources such as Arxiv and Wikipedia.
- **User-Friendly Interface**: Simple and intuitive UI using Streamlit for seamless user experience.
- **Chat Functionality**: Engage in a conversation with the AI assistant that keeps track of chat history.
- **Customization**: Enter your Groq API Key for access to LLM models.

# Project Structure


app/
│
├── main.py               # Main app for Streamlit interface
├── settings.py           # Settings for environment variables and configurations
├── chat.py               # Handles chat-related functionality
├── api_wrappers.py       # Handles API Wrappers for Arxiv, Wikipedia, etc.
├── agent.py              # Handles agent initialization and interaction
└── utils.py              # Utility functions for common tasks


To run the project go to the project directory and run

``
streamlit run main.py
``