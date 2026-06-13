import os

from dotenv import load_dotenv

from tavily import TavilyClient

load_dotenv()

def search_tool(query):

    results = []

    try:
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        
        search_results = client.search(query=query, max_results=5)
        
        for item in search_results.get("results", []):
            title = item.get("title", "")
            content = item.get("content", "")
            
            results.append(f"Title: {title}\nContent: {content}")
            
        if not results:
            return "No research results found for this query."
            
    except Exception as e:
        return f"Search failed with error: {str(e)}"

    return "\n\n".join(results)