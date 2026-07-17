from crewai import Crew, Process
from agents import research_agent, writer_agent
from tools import tool
from tasks import research_task, write_task


crew=Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

result = crew.kickoff(inputs={'topic': "AI Agentic frameworks"})
print(result)