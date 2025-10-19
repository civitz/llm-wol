#!/bin/bash
# Check if haproxy is installed
pacman -Qi haproxy &>/dev/null
if [ $? -ne 0 ]; then
    # If haproxy is not present, enable pacman
    sudo steamos-readonly disable
    sudo pacman-key --init
    sudo pacman-key --populate archlinux
    sudo pacman-key --populate holo

    # Install haproxy and xvfb and utilities
    sudo pacman -S --noconfirm haproxy xorg-server-xvfb nvtop ethtool

    # download lmstudio for linux
fi
