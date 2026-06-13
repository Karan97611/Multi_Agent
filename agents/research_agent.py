from tools.search_tool import search_tool


def research_agent(state):
    """
    Research Agent

    Uses search tool
    to gather information.
    """

    print("🤖 [Research Agent] Searching the web for information...")

    question = state["question"]

    research_results = search_tool(
        question
    )

    return {
        "research_data": research_results
    }