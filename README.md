# MCPServer

MCPServer is a Python-based project that demonstrates the use of Multi-Server MCP (Multi-Client Protocol) for creating modular and distributed tools. It includes servers for mathematical operations and weather information, along with a client that interacts with these servers using LangChain MCP adapters.

## Features

- **Math Server**: Provides tools for basic mathematical operations such as addition, subtraction, multiplication, division, and exponentiation.
- **Weather Server**: Provides weather information for a given city.
- **Client**: Connects to the servers and uses LangChain and LangGraph to create an AI agent capable of invoking tools.

## Requirements

- Python 3.13 or higher
- The following Python packages:
  - `langchain-groq`
  - `langchain-mcp-adapters`
  - `langgraph`
  - `mcp`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcpserver