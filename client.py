from pdb import run
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from typing import Any

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    connections: Any = {
        "math": {
            "command": "python",
            "args": ["/Users/lakshmianand/Desktop/mcpserver/mathserver.py"],
            "transport": "stdio",
        },
        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    }
    
    client = MultiServerMCPClient(connections)

    import os
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key

    tools=await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"whats(3 + 5) x 12 ?"}]}
    )
    print("math response:", math_response["messages"][-1].content)

asyncio.run(main())