from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq
from api_wrappers import create_arxiv_wrapper, create_wiki_wrapper, create_search_tool

def create_agent(groq_api_key, model_name="Llama3-8b-8192"):
    """Create and initialize the AI agent"""
    llm = ChatGroq(groq_api_key=groq_api_key, model_name=model_name, streaming=True)
    arxiv = create_arxiv_wrapper()
    wiki = create_wiki_wrapper()
    search = create_search_tool()
    tools = [search, arxiv, wiki]
    
    # Initialize the agent
    return initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)

def run_agent(agent, messages):
    """Run the agent and return its response"""
    st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
    return agent.run(messages, callbacks=[st_cb])
