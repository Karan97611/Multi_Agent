from llm.llm_provider import get_llm

llm = get_llm()


def summary_agent(state):

    print("🤖 [Summary Agent] Summarizing verified data...")

    verified_data = state["verified_data"]

    prompt = f"""
Create concise summary.

Keep only important findings.

DATA:

{verified_data}
"""

    response = llm.invoke(prompt)

    return {
        "summary": response.content
    }