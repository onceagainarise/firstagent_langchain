import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor, load_tools
from langchain import hub
import arxiv

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
research_tool = load_tools(["arxiv"])
# Prompt for ReAct agent
prompt = hub.pull("hwchase17/react")

# Agent creation
agent = create_react_agent(llm=llm, tools=research_tool, prompt=prompt)

# Agent executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=research_tool,
    verbose=True,
    handle_parsing_errors=True
)

# Run agent
response = agent_executor.invoke(
    {"input": "what is the paper 'Self-Adapting Language Models' about?"}
)
print(response)
