from business_mcp_server import app
client=app.test_client()
assert client.get('/').text=='MCP Server Running'
assert client.post('/order-status',json={}).status_code==400
assert client.post('/order-status',json={'order_id':'FD1001'}).json['status']=='In Transit'
assert client.post('/notify',json={'user_id':'U1','message':'Test'}).status_code==200
assert client.get('/user-profile/U100').json['email']=='aarav@example.test'
print('Business server checks passed: root, required-field validation, order status, notification, profile.')
