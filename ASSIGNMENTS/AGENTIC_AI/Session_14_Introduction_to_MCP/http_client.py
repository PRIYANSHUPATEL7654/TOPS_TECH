"""MCP SDK client for Streamable HTTP; SDK performs JSON-RPC negotiation."""
import asyncio
from mcp import Client
async def main(url="http://127.0.0.1:8000/mcp"):
    async with Client(url) as client:
        print("Tools:",await client.list_tools())
        print("Status:",await client.call_tool("server_status",{}))
        print("Song:",await client.call_tool("get_song_recommendation",{}))
if __name__=="__main__": asyncio.run(main())
