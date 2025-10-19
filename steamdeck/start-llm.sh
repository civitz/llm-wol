#!/bin/bash
set -x
set -e

podman run -d \
 --add-host=host.docker.internal:host-gateway \
 --rm -p 3000:8080 \
 -v $(pwd)/openwebui:/app/backend/data \
 --name open-webui \
 ghcr.io/open-webui/open-webui:main

nohup xvfb-run --auto-servernum ~/programs/LM-Studio-0.3.28-2-x64.AppImage &

haproxy -f ~/haproxy.cfg -D

sleep 10

lms server start --cors