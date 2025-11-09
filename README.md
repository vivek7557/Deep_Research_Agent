# Deep Research Agent — Planning Agent for Deep Research & Structured Report Generation

This repository contains a notebook that builds a Planning Agent for deep research and structured report generation using LangGraph + LangChain and web-search (Tavily). The agent plans a wiki-style report, runs parallel web research for sections, drafts each section with LLMs, and composes a final Markdown report.

IMPORTANT: The agent runs many web searches. If you use Tavily on a free tier you may exhaust your API limits quickly — use carefully.

## Contents
- Build_a_Planning_Agent_for_Deep_Research_&_Structured_Report_Generation.ipynb — primary notebook that:
  - installs dependencies
  - defines the agent state schema
  - implements utility functions for Tavily search
  - builds a LangGraph StateGraph agent and subagents
  - demonstrates running sample topics
- README.md — this file
- requirements.txt — Python packages used by the notebook
- .gitignore — recommended ignores for local / GitHub pushes

## Goals
- Generate a planned report structure for an input topic
- Run parallel web research per section (Tavily)
- Use an LLM to write structured 150–200 word sections
- Compose introduction & conclusion from completed sections
- Output a consolidated Markdown final report

## Quickstart (Colab / Jupyter)
1. Clone this repo (or directly open the notebook in Colab / GitHub).
2. Create and activate a Python 3.11+ environment (recommended).
3. Install Python dependencies:
   - pip install -r requirements.txt
4. Set environment variables (or enter via interactive prompt in notebook):
   - OPENAI_API_KEY — your OpenAI API key
   - TAVILY_API_KEY — your Tavily Search API key
   - (Optionally) any other keys you use (LangSmith etc.)
5. Open and run the notebook cells in order. Follow the prompts in the notebook (it requests the API keys interactively).

Example (local):
```bash
git clone https://github.com/vivek7557/Deep_Research_Agent.git
cd Deep_Research_Agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# export your keys, then
jupyter notebook Build_a_Planning_Agent_for_Deep_Research_&_Structured_Report_Generation.ipynb
```

Notes:
- The notebook uses `ChatOpenAI` (gpt-4o in the example) — change model_name or LLM configuration to one you have access to.
- Tavily calls can be costly or limited — reduce the number of queries or results if you hit limits.
- The notebook writes temporary state in-memory; if you add persistence, do not commit sensitive files.

## Security & sensitive data
- Do NOT commit API keys, .env files, or other secrets to the repository.
- The included .gitignore prevents common key/IDE/venv files from being committed.

## Contributing
- Feel free to open issues, raise PRs with improvements (better prompts, error handling, retries, persistence, observability).
- If adding new major dependencies, update requirements.txt.

## Troubleshooting
- If the notebook errors when importing packages, confirm you installed the pinned versions in requirements.txt.
- For Tavily errors, verify TAVILY_API_KEY and network connectivity.
- If LLM calls fail, check OpenAI quota and model permissions.

## License
This project does not include an explicit license file. If you want to publish this repo publicly, add a LICENSE (e.g., MIT) or confirm the desired license with the maintainer.
