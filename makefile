all:
	docker build -t jupyterhub .

run:
	docker run -p 8000:8000 -it --mount source=jupyterHubHomes,target=/home jupyterhub

volume:
	docker volume create jupyterHubHomes
