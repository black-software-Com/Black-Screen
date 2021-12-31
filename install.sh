#!/bin/sh
# Black-Screen v1.0
#

if [[ "$(id -u)" -ne 0 ]];
then
  echo "
Please, Run This Program as Root!
"
  exit
fi
function Main() {
    printf '\033]2;Bllack-Screen\a'
    clear
    echo "Installing :)"
    chmod +x black.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    python3 -m pip3 install --upgrade pip
    python3 -m pip3 install -r requirments.txt
    sleep 1
    echo "
Usage:
      python black.py
    "
    sleep 0.50
    echo "
Thanks For Using :)
"
    echo "Have Nice Day :-)"
    exit 
}
Main