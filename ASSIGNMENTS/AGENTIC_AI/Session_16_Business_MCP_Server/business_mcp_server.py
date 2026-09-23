"""Flask server for business-style MCP exercises (REST simulation)."""
from flask import Flask,request,jsonify
from pathlib import Path
app=Flask(__name__); LOG=Path(__file__).with_name("notifications.log")
ORDERS={"FD1001":"In Transit","FD1002":"Delivered","FD1003":"Cancelled"}
PROFILES={"U100":{"name":"Aarav Patel","email":"aarav@example.test","phone":"000-000-0100"}}
@app.get("/")
def status():return "MCP Server Running"
@app.post("/order-status")
def order_status():
    data=request.get_json(silent=True) or {}; order=data.get("order_id")
    if not order:return jsonify(error="order_id is required"),400
    return jsonify(order_id=order,status=ORDERS.get(order,"In Transit"))
@app.post("/notify")
def notify():
    data=request.get_json(silent=True) or {}
    if not data.get("user_id") or not data.get("message"):return jsonify(error="user_id and message are required"),400
    with LOG.open("a",encoding="utf-8") as f:f.write(f"{data['user_id']} | {data['message']}\n")
    return jsonify(ok=True,message="Notification logged")
@app.get("/user-profile/<user_id>")
def user_profile(user_id):
    profile=PROFILES.get(user_id)
    if not profile:return jsonify(error="User not found"),404
    return jsonify(profile)
if __name__=="__main__":app.run(host="127.0.0.1",port=5000,debug=False)
