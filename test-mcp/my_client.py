import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tools(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result.content[0].text)


asyncio.run(call_tools("Yue Da"))