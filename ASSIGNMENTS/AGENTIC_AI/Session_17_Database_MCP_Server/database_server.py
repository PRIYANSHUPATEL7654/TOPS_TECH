"""SQLite-backed Flask command server; safe, allow-listed operations."""
from flask import Flask,request,jsonify
import sqlite3
from datetime import datetime,timezone
from pathlib import Path
app=Flask(__name__); app.config['DB_PATH']=str(Path(__file__).with_name('orders.db'))
def connect():
 c=sqlite3.connect(app.config['DB_PATH']);c.row_factory=sqlite3.Row
 c.execute("CREATE TABLE IF NOT EXISTS orders(order_id TEXT PRIMARY KEY,user_id TEXT NOT NULL,amount REAL NOT NULL,created_at TEXT NOT NULL)");c.commit();return c
@app.post('/command')
def command():
 data=request.get_json(silent=True) or {};cmd=data.get('command');p=data.get('params') or {}
 try:
  with connect() as db:
   if cmd=='ADD_ORDER':
    if any(k not in p for k in ['order_id','user_id','amount']):return jsonify(error='order_id, user_id and amount are required'),400
    db.execute('INSERT INTO orders VALUES(?,?,?,?)',(str(p['order_id']),str(p['user_id']),float(p['amount']),datetime.now(timezone.utc).isoformat()))
    return jsonify(ok=True,message='Order added',order_id=p['order_id'])
   if cmd=='GET_USER_ORDERS':
    if not p.get('user_id'):return jsonify(error='user_id is required'),400
    rows=db.execute('SELECT order_id,user_id,amount,created_at FROM orders WHERE user_id=? ORDER BY created_at DESC',(str(p['user_id']),)).fetchall();return jsonify(orders=[dict(r) for r in rows])
   if cmd=='GET_LAST_N_ORDERS':
    if not p.get('user_id'):return jsonify(error='user_id is required'),400
    n=max(1,min(int(p.get('n',5)),50));rows=db.execute('SELECT order_id,user_id,amount,created_at FROM orders WHERE user_id=? ORDER BY created_at DESC LIMIT ?',(str(p['user_id']),n)).fetchall();return jsonify(orders=[dict(r) for r in rows])
   if cmd=='DELETE_ORDER':
    if not p.get('order_id'):return jsonify(error='order_id is required'),400
    cur=db.execute('DELETE FROM orders WHERE order_id=?',(str(p['order_id']),));return (jsonify(ok=bool(cur.rowcount),deleted=str(p['order_id'])),200 if cur.rowcount else 404)
   return jsonify(error='Unsupported command'),400
 except sqlite3.IntegrityError:return jsonify(error='Order ID already exists'),409
 except (TypeError,ValueError):return jsonify(error='Invalid amount or order limit'),400
@app.get('/')
def health():return jsonify(status='Database MCP demo running')
if __name__=='__main__':connect().close();app.run(host='127.0.0.1',port=5001,debug=False)
