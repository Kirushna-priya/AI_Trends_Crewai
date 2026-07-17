from crewai import Agent
from dotenv import load_dotenv
from crewai.llms.providers.openai_compatible.completion import OpenAICompatibleCompletion
from tools import tool
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key

llm = OpenAICompatibleCompletion(
    provider="ollama",
    model="qwen3:8b",
    temperature=0.5,
    base_url="http://localhost:11434/v1"
)


research_agent = Agent(
    role="Chief Researcher",
    goal="research on significant updates in {topic}",
    llm=llm,
    verbose=True,
    memory=True,
    backstory=("You are highly vigilant researcher who has a keen eye for detail and is skilled at analyzing complex information and sharing it in a clear and concise manner."),
    tools=[tool],
    allow_delegation=True
    )

writer_agent = Agent(
    role="Content Writer",
    goal="write a comprehensive blog post on {topic} based on the research findings",
    llm=llm,
    verbose=True,
    memory=True,
    backstory=("You are a skilled content writer who can transform complex research findings into engaging and informative blog posts."),
    tools=[tool],
    allow_delegation=False
)