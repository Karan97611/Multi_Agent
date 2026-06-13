from llm.llm_provider import get_llm

llm = get_llm()


def verification_agent(state):
    """
    Fact checking agent.

    Tries to identify:

    - unsupported claims
    - weak evidence
    - confidence score
    """

    print("🤖 [Verification Agent] Fact-checking research data...")

    research_data = state["research_data"]

    prompt = f"""
You are a senior fact checker.

Verify information below.

Provide:

1. Verified facts
2. Suspicious facts
3. Confidence score

DATA:

{research_data}
"""

    response = llm.invoke(prompt)

    return {
        "verified_data": response.content
    }