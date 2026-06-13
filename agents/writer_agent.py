from llm.llm_provider import get_llm

llm = get_llm()


def writer_agent(state):

    print("🤖 [Writer Agent] Drafting the final professional report...")

    summary = state["summary"]

    prompt = f"""
Create professional report.

Sections:

1. Executive Summary
2. Key Findings
3. Analysis
4. Recommendations
5. Conclusion

DATA:

{summary}
"""

    response = llm.invoke(prompt)

    return {
        "final_report": response.content
    }