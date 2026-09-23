"""Manual MCP JSON-RPC request outline for an initialized Streamable HTTP session.
Use stdio_client.py/http_client.py for complete negotiation; this small function
shows the JSON-RPC request envelope required by the assignment.
"""
import json

def make_tools_call_request(tool_name,arguments,request_id=2):
    return {"jsonrpc":"2.0","id":request_id,"method":"tools/call","params":{"name":tool_name,"arguments":arguments}}
if __name__=="__main__":
    print(json.dumps(make_tools_call_request("server_status",{}),indent=2))
    print("The official SDK HTTP client sends JSON-RPC over Streamable HTTP and manages initialization/session headers.")
