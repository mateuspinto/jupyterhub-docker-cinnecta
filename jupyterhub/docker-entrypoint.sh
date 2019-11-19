#!/bin/bash

for f in /home/*/; do adduser -q --gecos '""' --disabled-password ${f:6:-1}; done
for f in /home/*/; do chown -R ${f:6:-1} "$f"; done
chmod -R 0777 /home
chmod -R 0777 /shared
jupyterhub --ip 0.0.0.0
