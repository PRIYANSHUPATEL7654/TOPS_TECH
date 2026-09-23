"""Restricted JSON-lines TCP server supporting LIST, GET, DELETE inside server_files."""
import json,socket
from pathlib import Path
ROOT=Path(__file__).with_name('server_files').resolve();ROOT.mkdir(exist_ok=True)
def resolve_name(name):
 path=(ROOT/name).resolve()
 if ROOT not in path.parents:raise ValueError('Path must remain inside server_files')
 return path
def handle_command(message):
 parts=message.strip().split(maxsplit=1);cmd=parts[0].upper() if parts else ''
 if cmd=='LIST':return {'ok':True,'files':sorted(p.name for p in ROOT.iterdir() if p.is_file())}
 if cmd in {'GET','DELETE'}:
  if len(parts)!=2:return {'ok':False,'error':'Filename required'}
  try:path=resolve_name(parts[1])
  except ValueError as e:return {'ok':False,'error':str(e)}
  if not path.is_file():return {'ok':False,'error':'File not found'}
  if cmd=='GET':return {'ok':True,'filename':path.name,'content':path.read_text(encoding='utf-8')}
  path.unlink();return {'ok':True,'deleted':path.name}
 return {'ok':False,'error':'Use LIST, GET filename, or DELETE filename'}
def serve(host='127.0.0.1',port=5050):
 with socket.create_server((host,port)) as server:
  print(f'Filesystem demo server listening on {host}:{port}')
  while True:
   conn,addr=server.accept()
   with conn:conn.sendall((json.dumps(handle_command(conn.recv(8192).decode()))+'\n').encode());print('Client connected:',addr)
if __name__=='__main__':serve()
