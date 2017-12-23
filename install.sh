#!/usr/bin/env bash
mkdir ~/.math
chmod +x math.py
mv math.py ~/.math
ln -s ~/.math/math.py /usr/sbin/math
