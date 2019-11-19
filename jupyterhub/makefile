all:
	docker build -t jupyterhub .

run:
	docker run -dit --restart unless-stopped -p 8000:8000 -it --mount source=jupyterHubHomes,target=/home --mount source=jupyterHubShared,target=/shared jupyterhub

volume:
	docker volume create jupyterHubHomes && docker volume create jupyterHubShared
