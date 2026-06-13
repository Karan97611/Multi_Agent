from langgraph.graph import StateGraph

from models.state import ResearchState

from agents.research_agent import research_agent
from agents.verification_agent import verification_agent
from agents.summary_agent import summary_agent
from agents.writer_agent import writer_agent


def build_graph():

    workflow = StateGraph(
        ResearchState
    )

    workflow.add_node(
        "research",
        research_agent
    )

    workflow.add_node(
        "verification",
        verification_agent
    )

    workflow.add_node(
        "summary",
        summary_agent
    )

    workflow.add_node(
        "writer",
        writer_agent
    )

    workflow.set_entry_point(
        "research"
    )

    workflow.add_edge(
        "research",
        "verification"
    )

    workflow.add_edge(
        "verification",
        "summary"
    )

    workflow.add_edge(
        "summary",
        "writer"
    )

    workflow.set_finish_point(
        "writer"
    )

    return workflow.compile()