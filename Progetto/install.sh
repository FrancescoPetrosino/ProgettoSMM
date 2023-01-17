#!/bin/sh

cd requirements
sudo /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 -m pip install --default-timeout=300 --upgrade -r requirements-upgrade.txt
sudo /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 -m pip install --default-timeout=300 -r requirements.txt