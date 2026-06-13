from typing import TypedDict


class ResearchState(TypedDict):
    """
    Shared state used by all agents.

    Every agent reads and updates
    this object.
    """

    question: str

    research_data: str

    verified_data: str

    summary: str

    final_report: str