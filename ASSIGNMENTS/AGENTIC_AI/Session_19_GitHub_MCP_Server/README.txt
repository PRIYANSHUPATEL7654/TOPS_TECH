GITHUB ACCOUNT STEPS (manual)
1. Install Git and GitHub CLI, authenticate with gh auth login.
2. Install the official GitHub MCP Server using its current official installation instructions; it is a separate Go service and can run as an official binary or Docker container.
3. Create playlist-manager using GitHub, add a README.txt describing a Spotify-style playlist feature, then commit and push.
4. Run webhook_app.py locally on port 5002. GitHub needs a reachable endpoint; use an approved tunnel or deploy it. In repository Settings > Webhooks, configure endpoint ending /webhook, strong secret as GITHUB_WEBHOOK_SECRET, application/json, events Issues and Pull requests. Never commit the secret.
5. Create an issue to test notification. Open a pull request labeled bug to test title and author output.
6. The code returns a thank-you comment draft. Actually posting a comment requires your credentials and a deliberately granted write scope; verify repository and event before enabling automation.

Repository creation, authentication, official server installation, public endpoint, webhook registration, and live event screenshots require your own GitHub account and are not performed by this local archive.
