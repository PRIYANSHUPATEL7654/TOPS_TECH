"""Local GitHub webhook example; validates HMAC SHA-256 signatures."""
import hashlib
import hmac
import os
from pathlib import Path
from flask import Flask, jsonify, request

app = Flask(__name__)
LOG = Path(__file__).with_name("github_events.log")

def post_thank_you_comment(owner, repo, issue_number, token, http_post=None):
    """Post only when explicitly called with a token; injectable client supports offline testing."""
    if not token:
        return {"skipped": True, "reason": "GitHub token missing"}
    if http_post is None:
        import requests
        http_post = requests.post
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    response = http_post(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
        json={"body": "Thanks for opening this issue! We will review it soon."},
        timeout=15,
    )
    response.raise_for_status()
    return {"posted": True, "url": response.json().get("html_url")}

def valid_signature(body, header, secret):
    expected = "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    return bool(header) and hmac.compare_digest(expected, header)

@app.post("/webhook")
def webhook():
    secret = os.getenv("GITHUB_WEBHOOK_SECRET", "local-demo-secret")
    if not valid_signature(request.get_data(), request.headers.get("X-Hub-Signature-256", ""), secret):
        return jsonify(error="Invalid signature"), 401
    event = request.headers.get("X-GitHub-Event", "")
    data = request.get_json(silent=True) or {}
    action = data.get("action")
    if event == "issues" and action == "opened":
        issue = data.get("issue", {})
        text = f"New issue #{issue.get('number')}: {issue.get('title')}"
        with LOG.open("a", encoding="utf-8") as stream:
            stream.write(text + "\n")
        comment_result = None
        if os.getenv("ENABLE_AUTO_COMMENT", "false").lower() == "true":
            repo = os.getenv("GITHUB_REPOSITORY", "").split("/", 1)
            token = os.getenv("GITHUB_TOKEN")
            if len(repo) == 2 and token:
                comment_result = post_thank_you_comment(repo[0], repo[1], issue.get("number"), token)
        return jsonify(message=text, manual_comment="Thanks for opening this issue! We will review it soon.", comment_result=comment_result), 200
    if event == "pull_request" and action in {"opened", "reopened", "synchronize"}:
        pr = data.get("pull_request", {})
        labels = {item.get("name", "").casefold() for item in pr.get("labels", [])}
        if "bug" in labels:
            return jsonify(title=pr.get("title"), author=pr.get("user", {}).get("login")), 200
        return jsonify(ignored="Pull request does not have bug label"), 200
    return jsonify(ignored="Event/action not configured"), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=False)
