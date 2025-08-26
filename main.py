import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# LLM setup
llm = ChatGroq(
    api_key=groq_api_key,
    model="deepseek-r1-distill-llama-70b",
    temperature=0.7
)

# Tool setup
search = DuckDuckGoSearchRun()

# Prompt for ReAct agent
prompt = hub.pull("hwchase17/react")

# Agent creation
agent = create_react_agent(llm=llm, tools=[search], prompt=prompt)

# Agent executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search],
    verbose=True,
    handle_parsing_errors=True
)

# Run agent
response = agent_executor.invoke(
    {"input": "what is today's date in India and time in New Delhi?"}
)
print(response)
