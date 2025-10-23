#!/bin/bash
set -x

HOST="hostname or ip"
MAC_ADDRESS="mac address"
USER="username"
REMOTE_SCRIPT='~/llm-wol/steamdeck/start-llm.sh'

# check if $HOST is up (use ping -c 1)
# if not up, launch wake on lan with wakeonlan $MAC_ADDRESS
# once online, ssh into $USER@$HOST and run ~/llm-wol/steamdeck/start-llm.sh

# Wait for the device to come online
while ! ping -c 1 $HOST &> /dev/null; do
    wakeonlan $MAC_ADDRESS
    sleep 5
done

# SSH into the device and run the script
ssh $USER@$HOST $REMOTE_SCRIPT