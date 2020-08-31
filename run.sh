#!/bin/bash

# NOTE
# Run this script as root


# Shutdown the server and copy the file since the database will be locked if the emby server is running.
systemctl stop emby-server
cp /var/lib/emby/data/library.db .
systemctl start emby-server

# Wait until the server is back running again.
sleep 5
while ! httping -qc1 http://127.0.0.1:8096/web/index.html ; do sleep 1 ; done

/home/lukas/.local/share/virtualenvs/embyAutoRemoverPython-HdWG67Lm/bin/python remove.py
