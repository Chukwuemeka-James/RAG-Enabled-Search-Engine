from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun

def create_arxiv_wrapper():
    """Create and return Arxiv API Wrapper"""
    arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    return ArxivQueryRun(api_wrapper=arxiv_wrapper)

def create_wiki_wrapper():
    """Create and return Wikipedia API Wrapper"""
    wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    return WikipediaQueryRun(api_wrapper=wiki_wrapper)

def create_search_tool():
    """Create and return DuckDuckGo search tool"""
    return DuckDuckGoSearchRun(name="Search")
