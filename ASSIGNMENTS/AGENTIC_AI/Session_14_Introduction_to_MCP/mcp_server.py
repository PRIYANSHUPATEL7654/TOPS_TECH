"""MCP SDK v2 server for static status and random song recommendations."""
import random
from mcp.server import MCPServer
mcp=MCPServer("TOPS Course Demo")
SONGS=["Golden Hour - JVKE","Levitating - Dua Lipa","Kesariya - Arijit Singh"]
@mcp.tool()
def server_status()->str:
    """Return a static confirmation that the course MCP server is running."""
    return "MCP Server Running"
@mcp.tool()
def get_song_recommendation()->dict:
    """Return one randomly selected sample trending song."""
    return {"title":random.choice(SONGS),"source":"sample trending list"}
@mcp.prompt()
def get_movie_showtimes(movie:str,city:str,date:str)->str:
    """Draft a request to look up showtimes; integrate with a cinema API as a tool."""
    return f"Find available showtimes for {movie} in {city} on {date}. Return cinema, time, seats, and price; do not reserve without user confirmation."
if __name__=="__main__": mcp.run()
