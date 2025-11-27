from google.adk.agents import Agent
from google.adk.tools import load_artifacts
from hr_agent.prompt import SUMMARIZER_PROMPT

summarizer_agent = Agent(
    model="gemini-2.5-flash",
    name="resume_summarizer_agent",
    description="Agent that summarizes resumes to extract key information such as skills, experience, and education.",
    instruction=SUMMARIZER_PROMPT,
    tools=[load_artifacts]
)