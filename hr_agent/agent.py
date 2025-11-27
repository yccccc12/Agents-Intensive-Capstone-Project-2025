
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from google.adk.apps import App
from google.adk.plugins.save_files_as_artifacts_plugin import SaveFilesAsArtifactsPlugin
from google.adk.memory import InMemoryMemoryService
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.adk.tools import load_memory
from hr_agent.prompt import ROOT_PROMPT

# Import sub-agents
from hr_agent.sub_agents.summarizer.agent import summarizer_agent
from hr_agent.sub_agents.comparator.agent import comparator_agent
from hr_agent.sub_agents.question_generator.agent import question_generator_agent
from hr_agent.sub_agents.industry_researcher.agent import industry_researcher_agent

# Initialize memory and session services
memory_service = InMemoryMemoryService()
session_service = InMemorySessionService()

# Auto-save session after each agent interaction
async def auto_save_session(callback_context):
    await callback_context._invocation_context.memory_service.add_session_to_memory(
        callback_context._invocation_context.session
    )

# Define the orchestrating root agent
root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_hr_agent",
    description="An HR Assistant leveraging multiple sub-agents for resume parsing, comparison, and interview preparation.",
    instruction=ROOT_PROMPT,
    sub_agents=[
        summarizer_agent,
        comparator_agent,
        question_generator_agent,
    ],
    tools=[
        agent_tool.AgentTool(agent=industry_researcher_agent),
        load_memory,
    ],
    after_agent_callback=auto_save_session
)

# Application setup
app = App(
    name='hr_agent',
    root_agent=root_agent,
    plugins=[SaveFilesAsArtifactsPlugin()],
)

# Runner setup
runner = Runner(app=app, session_service=session_service, memory_service=memory_service)
