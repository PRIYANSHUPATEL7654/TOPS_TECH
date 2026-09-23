import tempfile,os
from database_server import app
with tempfile.TemporaryDirectory() as d:
 app.config['DB_PATH']=os.path.join(d,'test.sqlite');c=app.test_client()
 assert c.post('/command',json={'command':'ADD_ORDER','params':{'order_id':'O1','user_id':'U1','amount':12.5}}).status_code==200
 assert c.post('/command',json={'command':'ADD_ORDER','params':{'order_id':'O2','user_id':'U1','amount':20}}).status_code==200
 assert len(c.post('/command',json={'command':'GET_LAST_N_ORDERS','params':{'user_id':'U1','n':1}}).json['orders'])==1
 assert len(c.post('/command',json={'command':'GET_USER_ORDERS','params':{'user_id':'U1'}}).json['orders'])==2
 assert c.post('/command',json={'command':'DELETE_ORDER','params':{'order_id':'O1'}}).json['ok']
 assert c.post('/command',json={'command':'ADD_ORDER','params':{'user_id':'U1'}}).status_code==400
print('Database checks passed: add, per-user lookup, recent-N order, delete, validation.')
