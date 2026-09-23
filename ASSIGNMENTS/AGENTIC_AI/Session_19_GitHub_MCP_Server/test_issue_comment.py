from webhook_app import post_thank_you_comment
class FakeResponse:
 def raise_for_status(self):pass
 def json(self):return {'html_url':'https://github.example/test'}
calls=[]
def fake_post(url,**kwargs):calls.append((url,kwargs));return FakeResponse()
r=post_thank_you_comment('owner','playlist-manager',12,'fake-token',fake_post)
assert r['posted'] and calls[0][1]['json']['body'].startswith('Thanks')
assert post_thank_you_comment('owner','repo',1,'')['skipped']
print('Issue comment helper checks passed with a fake HTTP client; no real comment was posted.')
