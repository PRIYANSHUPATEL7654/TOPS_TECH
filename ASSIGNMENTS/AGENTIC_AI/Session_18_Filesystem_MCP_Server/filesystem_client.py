import json,socket,sys
def request(message,host='127.0.0.1',port=5050):
 with socket.create_connection((host,port),timeout=5) as s:s.sendall((message+'\n').encode());return json.loads(s.recv(8192).decode())
if __name__=='__main__':print(request(' '.join(sys.argv[1:]) or 'LIST'))
