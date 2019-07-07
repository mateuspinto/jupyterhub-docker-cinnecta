from oauthenticator.github import LocalGitHubOAuthenticator
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.LocalGitHubOAuthenticator.oauth_callback_url = 'https://localhost:8000/hub/oauth_callback'
c.LocalGitHubOAuthenticator.client_id = 'a8a26087af2fd6b34a8d'
c.LocalGitHubOAuthenticator.client_secret = '6e4ac12c347bebee7b664645087b2e56e4b4306e'

c.LocalGitHubOAuthenticator.create_system_users = True
#c.Authenticator.whitelist = {'peter','kendra'}
c.Authenticator.admin_users = {'mateusps10','leandrolazaro'}
