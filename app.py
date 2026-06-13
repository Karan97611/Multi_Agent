from fastapi import FastAPI

from pydantic import BaseModel

from workflow.graph import build_graph

app = FastAPI(
    title="Multi Agent Research Assistant"
)

graph = build_graph()


class ResearchRequest(BaseModel):
    question: str


@app.post("/research")
def research(request: ResearchRequest):

    print(f"\n🚀 Starting research for: '{request.question}'")

    result = graph.invoke(
        {
            "question": request.question
        }
    )

    print("✅ Research complete!\n")

    print(f"📄 Final Report Preview:\n{result['final_report']}\n")

    return {
        "question": request.question,
        "report": {
            "research_agent_report": result.get("research_data", ""),
            "verification_agent_report": result.get("verified_data", ""),
            "summary_agent_report": result.get("summary", ""),
            "writer_agent_report": result.get("final_report", "")
        }
    }