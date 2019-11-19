from oauthenticator.github import LocalGitHubOAuthenticator
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.LocalGitHubOAuthenticator.oauth_callback_url = 'http://3.80.140.38:8000/hub/oauth_callback'
c.LocalGitHubOAuthenticator.client_id = 'a8a26087af2fd6b34a8d'
c.LocalGitHubOAuthenticator.client_secret = '6e4ac12c347bebee7b664645087b2e56e4b4306e'

c.LocalGitHubOAuthenticator.create_system_users = True
c.Authenticator.whitelist = {'LeonardoJAlves','gcoimbra','RaissaPapinii','wandella'}
c.Authenticator.admin_users = {'matelementalista','fabaguiarsilva'}
