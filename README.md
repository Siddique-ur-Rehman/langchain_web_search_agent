# AI Agent with Gemini, Web Search & PostgreSQL Memory

A simple AI agent built with **LangChain** and **Google Gemini**. The agent can use tools for calculations and web searches, while conversation history is stored in **PostgreSQL** for session-based memory.

## Features

* Google Gemini 2.5 Flash as the LLM
* LangChain agent using `create_agent`
* Web search tool using DuckDuckGo
* Word-length calculation tool
* PostgreSQL-based conversation history
* Session management using unique session IDs
* Streaming agent responses
* Environment variables for API keys and database credentials

## Technologies

* Python
* LangChain
* Google Gemini
* DuckDuckGo / DDGS
* PostgreSQL
* SQLAlchemy
* Psycopg
* python-dotenv
* uv

## Project Structure

```text
agent_langchain/
│
├── agent.py
├── database.py
├── chat_history.py
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## How It Works

The agent receives a user's question and can decide whether it needs to use one of its available tools.

```text
User
  ↓
LangChain Agent
  ↓
Google Gemini
  ↓
 ┌─────────────────────────┐
 │                         │
 ↓                         ↓
Web Search          Word Length Tool
 │                         │
 └────────────┬────────────┘
              ↓
        Final Response
              ↓
        PostgreSQL
       Chat History
```

## Available Tools

### Web Search

The agent can search the web for up-to-date information using DuckDuckGo.

Example:

```text
Search for the capital of Azerbaijan.
```

The agent can search for the capital and then use the calculation tool if required.

### Word Length Calculator

The agent has a custom tool that calculates the exact number of characters in a word or string.

Example:

```text
How many letters are in Supercalifragilisticexpialidocious?
```

## PostgreSQL Memory

Conversation history is stored in PostgreSQL.

The database uses two main tables:

```text
sessions
    │
    └── messages
```

### Sessions

Stores information about individual conversations.

### Messages

Stores:

* User messages
* Assistant messages
* Session ID
* Message timestamps

This allows the agent to retrieve previous messages belonging to a specific conversation session.

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/agent_db
```

Do not commit `.env` to GitHub.

You can use `.env.example` as a template:

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/agent_db
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd agent_langchain
```

Create the virtual environment and install dependencies.

If using `uv`:

```bash
uv sync
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Create a PostgreSQL database named:

```text
agent_db
```

Then configure the database connection in `.env`:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/agent_db
```

Run the database setup:

```bash
uv run database.py
```

This creates the required tables.

## Running the Agent

Run the agent with:

```bash
uv run agent.py
```

You will receive a session ID when the application starts.

Example:

```text
Session ID: 8f7c2c1e-xxxx-xxxx-xxxx-xxxxxxxxxxxx

Enter your prompt:
```

You can continue asking questions during the same session.

To exit:

```text
quit
```

## Example

```text
Enter your prompt: What is the capital of Azerbaijan?

Enter your prompt: How many letters are in its capital name?

The capital of Azerbaijan is Baku, and it has 4 letters.
```

The conversation is stored in PostgreSQL so that previous messages can be retrieved during the session.

## Security

Never commit sensitive credentials to GitHub.

The following files should remain private:

```text
.env
```

The `.gitignore` file is configured to prevent these files from being committed.

## Future Improvements

Possible improvements for the project include:

* Reusable session IDs
* FastAPI backend
* User authentication
* Better conversation management
* Long-term memory
* LangGraph-based persistence
* PostgreSQL connection pooling
* Conversation deletion and management
* Frontend chat interface
* Deployment to a cloud platform

## Author

**Siddique Ur Rehman**
