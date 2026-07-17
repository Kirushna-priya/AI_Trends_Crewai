from crewai import Task
from tools import tool
from agents import research_agent, writer_agent

research_task = Task(
    description=( "Identify the latest trend in {topic}."
                 "Find it's use case, how is it different from already excisting solutions"
                 "Pros and cons of it"
                 "market opportunities and potential risks."
                 ),
    expected_output="A consise two paragraph to the point blog post on the {topic}.",
    tools=[tool],
    agent=research_agent
    )

write_task = Task(
    description=( "write a concise blog post on {topic}."
                 "write it in a engaging storytelling manner"
                 "write as if an human is writting this post"
                 ),
    expected_output="A consise two paragraph to the point blog post on the {topic} written in markdown.",
    tools=[tool],
    agent=writer_agent,
    async_execution=False,
    output_file="blog_post.md"
    )

              
          
