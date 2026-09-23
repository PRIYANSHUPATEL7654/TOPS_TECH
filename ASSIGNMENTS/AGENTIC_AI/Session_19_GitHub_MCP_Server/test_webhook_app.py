import hashlib,hmac,json
from webhook_app import app
secret='local-demo-secret';c=app.test_client()
def signed(body):return 'sha256='+hmac.new(secret.encode(),body,hashlib.sha256).hexdigest()
body=json.dumps({'action':'opened','issue':{'number':7,'title':'Playlist bug'}}).encode()
r=c.post('/webhook',data=body,content_type='application/json',headers={'X-Hub-Signature-256':signed(body),'X-GitHub-Event':'issues'});assert r.status_code==200 and 'Playlist bug' in r.json['message']
assert c.post('/webhook',data=body,content_type='application/json',headers={'X-Hub-Signature-256':'sha256=bad','X-GitHub-Event':'issues'}).status_code==401
body2=json.dumps({'action':'opened','pull_request':{'title':'Fix playlist','user':{'login':'student'},'labels':[{'name':'bug'}]}}).encode()
r=c.post('/webhook',data=body2,content_type='application/json',headers={'X-Hub-Signature-256':signed(body2),'X-GitHub-Event':'pull_request'});assert r.json=={'title':'Fix playlist','author':'student'}
print('Webhook checks passed: issue event, signature rejection, bug-labelled PR filter.')
