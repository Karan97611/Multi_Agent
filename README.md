# 🤖 Multi-Agent Research Assistant

A powerful API-driven AI research assistant built with **FastAPI**, **LangGraph**, and **Ollama**. This system utilizes a multi-agent workflow to autonomously search the web, fact-check information, summarize findings, and write a professional report.

---

## 🏗️ Architecture & Data Flow

The system uses **LangGraph** to manage the state and workflow between four specialized AI agents. 

**Shared State**: All agents read and update a shared `ResearchState` dictionary during execution.

1. **User Request**: User sends a JSON payload with a `question` to the `/research` endpoint.
2. **Research Agent**: 
   * Takes the `question`.
   * Uses the **Tavily API** to search the web for relevant information.
   * Saves raw data to `research_data`.
3. **Verification Agent**: 
   * Reads `research_data`.
   * Uses local LLM (via **Ollama**) to fact-check, identify weak evidence, and provide a confidence score.
   * Saves to `verified_data`.
4. **Summary Agent**: 
   * Reads `verified_data`.
   * Uses LLM to extract only the most important findings.
   * Saves to `summary`.
5. **Writer Agent**: 
   * Reads `summary`.
   * Uses LLM to draft a structured, professional report (Executive Summary, Key Findings, Analysis, Recommendations, Conclusion).
   * Saves to `final_report`.
6. **Output**: 
   * The system saves the output of each agent into a local `/reports` folder as text files with timestamps.
   * Returns a complete JSON response containing all individual reports to the user.

---

## ⚙️ Prerequisites

1. **Python 3.9+** installed.
2. **Ollama** installed and running on your local machine (Download Ollama).
3. A **Tavily API Key** for web searching (Get a free key here).

---

## 🚀 Installation & Setup

### 1. Install Dependencies
Open your terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### 2. Pull the Local LLM
Ensure Ollama is running, then pull the model you intend to use. For example:
```bash
ollama pull llama3:latest
```
*(Note: If you are using a different model like `llama3.1`, run `ollama pull llama3.1` instead).*

### 3. Environment Configuration
In the root of your project, locate (or create) the `.env` file. You **must** update this file with your specific model name and API key:

```dotenv
# The exact name of the model you pulled in Ollama (e.g., llama3:latest or llama3.1)
MODEL_NAME=llama3:latest

# Your Tavily API key for the Search Tool
TAVILY_API_KEY=your_actual_tavily_api_key_here
```

---

## 💻 Running the Application

Start the FastAPI server using Uvicorn:
```bash
uvicorn app:app --reload
```

### Using the API
1. Open your web browser and navigate to the interactive API docs: **http://localhost:8000/docs**
2. Expand the `POST /research` endpoint and click **"Try it out"**.
3. Enter your question in the request body and click **Execute**.

*Note: Processing takes a few moments depending on your hardware, since the local LLM processes three separate prompts sequentially. Keep an eye on the terminal for live status updates!*

### Viewing the Results
* **API Response**: The Swagger UI will display a JSON response containing the outputs from all four agents.
* **Local Files**: Check the dynamically generated `reports/` folder in your project directory. It will contain `.txt` files of each agent's output, neatly timestamped for your records.