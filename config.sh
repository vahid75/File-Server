#!/usr/bin/env bash

PYTHON_PATH=$(which python3)
FILE_SERVER_OWNER=$USER
PKGS=("nginx" "python3" "virtualenv" "pip3")

function detect_pkg() {
        CK_PKGS=("$@")
        for i in "${CK_PKGS[@]}";do
                echo -n "Detecting $i package: "
                if [ ! which $i > /dev/null 2>&1 ];then
                        echo "FAILD."
                        echo "Hint: Install '$i' with your own package manager and try again."
                        exit -1
                else
                        echo "DONE."
                fi
        done
}

detect_pkg "${PKGS[@]}"

virtualenv .venv -p $PYTHON_PATH
source .venv/bin/activate
pip install -r requierments.txt
touch .env
echo "export FILE_SERVER_PATH='/home/$USER/file-server/'" > .env
mkdir /home/$USER/file-server/
python3 .ask_username.py
source .env
sudo touch /etc/nginx/sites-available/file-server
sudo touch /etc/nginx/sites-enabled/file-server
sudo chown $FILE_SERVER_OWNER /etc/nginx/sites-available/file-server
sudo chown $FILE_SERVER_OWNER /etc/nginx/sites-enabled/file-server
chmod 644 /etc/nginx/sites-available/file-server 
chmod 644 /etc/nginx/sites-enabled/file-server 

echo "Done."
