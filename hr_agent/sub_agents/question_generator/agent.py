from google.adk.agents import Agent
from hr_agent.prompt import QUESTION_GEN_PROMPT

question_generator_agent = Agent(
    model="gemini-2.5-flash",
    name="interview_question_generator",
    description="Generates interview questions from resumes.",
    instruction=QUESTION_GEN_PROMPT,
)
