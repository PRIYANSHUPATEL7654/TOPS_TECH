"""Manual JSON-RPC-over-HTTP client for an MCP 2025-era Streamable HTTP server."""
import requests
URL='http://127.0.0.1:8000/mcp'
HEAD={'Accept':'application/json, text/event-stream','Content-Type':'application/json'}
def post(payload,extra=None):
 headers=HEAD| (extra or {});r=requests.post(URL,json=payload,headers=headers,timeout=15);r.raise_for_status();return r
def main():
 init={'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-11-25','capabilities':{},'clientInfo':{'name':'course-http-client','version':'1.0'}}}
 response=post(init);session=response.headers.get('Mcp-Session-Id');print('Initialize:',response.text)
 headers={'MCP-Protocol-Version':'2025-11-25'}
 if session:headers['Mcp-Session-Id']=session
 post({'jsonrpc':'2.0','method':'notifications/initialized'},headers)
 result=post({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'server_status','arguments':{}}},headers)
 print('Tool response:',result.text)
if __name__=='__main__':main()
