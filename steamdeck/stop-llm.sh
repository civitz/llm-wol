#!/bin/bash
set -x
set -e

# Stop and remove the open-webui container
if podman ps -a --format '{{.Names}}' | grep -q open-webui; then
    podman stop open-webui
fi

# Kill the LM-Studio process
if pgrep -f "LM-Studio.*AppImage" > /dev/null; then
    pkill -f "LM-Studio.*AppImage"
fi

# Stop haproxy
#sudo systemctl stop haproxy

kill -USR1 $(pgrep haproxy)

echo "Servers terminated successfully"