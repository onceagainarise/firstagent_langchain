# Firstagent Langchain

This project demonstrates how to build a simple AI agent using [Langchain](https://python.langchain.com/) and the Groq LLM API. The agent can answer questions using a language model and perform web searches using DuckDuckGo.

## Features
- Integrates with Groq LLM via API key
- Uses Langchain's agent framework
- Performs web search with DuckDuckGo

## Requirements
- Python 3.8+
- `langchain`, `langchain-groq`, `langchain_community`, `python-dotenv`, `arxiv`

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/onceagainarise/firstagent_langchain.git
   cd firstagent_langchain
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set your `GROQ_API_KEY` in a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. Run the agent:
   ```sh
   python main.py
   ```

## Usage
The agent will answer questions and perform web searches as needed. You can modify the prompt or tools in `main.py` to customize its behavior.

## License
MIT
