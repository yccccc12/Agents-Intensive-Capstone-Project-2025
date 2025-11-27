from google.adk.agents import Agent
from hr_agent.prompt import COMPARATOR_PROMPT

comparator_agent = Agent(
    model="gemini-2.5-flash",
    name="candidate_comparator",
    description="Compares candidates across skills, experience, and job fit.",
    instruction=COMPARATOR_PROMPT,
)
