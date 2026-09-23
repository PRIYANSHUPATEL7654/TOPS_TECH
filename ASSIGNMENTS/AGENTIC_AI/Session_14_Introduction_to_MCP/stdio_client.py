"""Call the local MCP server over stdio, with the official v2 client."""
import asyncio,sys
from mcp import Client,StdioServerParameters
async def main():
    async with Client(StdioServerParameters(command=sys.executable,args=["mcp_server.py"])) as client:
        print(await client.call_tool("server_status",{})); print(await client.call_tool("get_song_recommendation",{}))
if __name__=="__main__": asyncio.run(main())
