from oauthenticator.github import LocalGitHubOAuthenticator
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.LocalGitHubOAuthenticator.oauth_callback_url = 'http://localhost:8000/hub/oauth_callback'
c.LocalGitHubOAuthenticator.client_id = 'a631fd9a2b3fa83bcaf2'
c.LocalGitHubOAuthenticator.client_secret = '5d4fce13e4b45edb64c7cfa3d2cf84b5ba2dd014'

c.LocalGitHubOAuthenticator.create_system_users = True
#c.Authenticator.whitelist = {'peter','kendra'}
c.Authenticator.admin_users = {'mateusps10','leandrolazaro'}
