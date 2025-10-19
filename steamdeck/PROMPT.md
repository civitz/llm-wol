
Write a bash script for a steamdeck using arch.

We want to be sure that haproxy and xvfb are installed.

Check whether they are installed by:
```bash
pacman -Qi haproxy
```

If haproxy is not present, assume pacman is disabled, and use these commands to enable it:

```bash
#!/bin/bash
sudo steamos-readonly disable
sudo pacman-key --init
sudo pacman-key --populate archlinux
sudo pacman-key --populate holo

```

Then install haproxy and xvfb via:
```bash
sudo pacman -S --noconfirm  haproxy xorg-server-xvfb
```

Finally, enable haproxy config by doing
```bash
sudo cp /home/deck/haproxy.cfg /etc/haproxy/haproxy.cfg
```