from google.adk.agents import Agent
from google.adk.tools import google_search
from hr_agent.prompt import INDUSTRY_RESEARCHER_PROMPT

industry_researcher_agent = Agent(
    model="gemini-2.5-flash",
    name="industry_researcher",
    description=(
        "Provides real-time market and industry research using Google Search. "
        "Retrieves industry-standard skills, validates technologies and companies, "
        "benchmarks job requirements, analyzes salary trends, and provides external "
        "market context to strengthen candidate evaluation and role alignment."
    ),
    instruction=INDUSTRY_RESEARCHER_PROMPT,
    tools=[google_search],
)
