# AI_Trends_Crewai

Building a crew of AI agents (agentic workflows) using crewai and open-source/local LLMs. This project demonstrates how to compose multiple agents (researcher, writer, etc.), attach tools, and run task pipelines that produce artifacts such as a blog post.

## Highlights
- Small example of an agent "crew" built with crewai primitives.
- Includes example agents, tasks, and tools that show how to coordinate research + writing.
- Produces a sample output (blog_post.md) demonstrating end-to-end execution.

## Project structure
AI_Trends_Crewai/
 .gitignore            
  LICENSE               
  requirements.txt     
  crew/
    agents.py          
    crew.py             
    tasks.py            
    tools.py           
    blog_post.md       

How it fits together:
- agents.py defines Agents (researcher, writer) and the LLM setup (provider, model, temperature, base_url).
- tools.py exposes functions/tools agents can call during tasks (e.g., web search wrappers or other utilities).
- tasks.py creates Task objects (descriptions, expected outputs) used by the crew.
- crew.py composes agents and tasks into a Crew and runs the crew when invoked; the crew runs tasks sequentially (as configured) and returns results.

## Requirements
Install the project requirements:
```bash
pip install -r AI_Trends_Crewai/requirements.txt
```

Files in requirements.txt:
- crewai
- load_dotenv
- langchain_openai
- crewai_tools

## Environment
This repository expects an LLM provider to be available. The code references:
- `OPENAI_API_KEY` — the module reads this environment variable if set.
- The LLM client in agents.py is configured with provider `"ollama"` and base URL `http://localhost:11434/v1` by default (change in crew/agents.py if you use a different provider or endpoint).

Set environment variables before running:
```bash
export OPENAI_API_KEY="your_api_key_here"
# or use .env with load_dotenv
```

If you use a local LLM endpoint (e.g., Ollama), ensure that endpoint is running and the base_url in crew/agents.py matches it.

## Quickstart — run the example
Run the small demo from the package to see a crew kickoff and the printed result:

Example interactive run (from repo root):
```bash
python -c "from AI_Trends_Crewai.crew.crew import crew; print(crew.kickoff({'topic': 'AI Agentic frameworks'}))"
```

Alternatively, open `AI_Trends_Crewai/crew/crew.py` and run it as a script after configuring your env vars and LLM endpoint.

The example will run the research and writing tasks and (in the sample configuration) writes output to `crew/blog_post.md`.

## Example output
- crew/blog_post.md — a sample generated article illustrating how the crew can produce a cohesive blog post from the research + writing pipeline.

## Customization
- Change LLM provider/model/temperature: edit `AI_Trends_Crewai/crew/agents.py`.
- Add or modify tools: edit `AI_Trends_Crewai/crew/tools.py`.
- Add tasks or change flow: edit `AI_Trends_Crewai/crew/tasks.py` and recompose the Crew in `crew/crew.py`.

