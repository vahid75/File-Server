sudo apt install python3 nginx
python_path=$(which python3)
virtualenv .venv -p $python_path
source .venv/bin/activate
pip install -r requierments.txt
touch .env
echo "export FILE_SERVER_PATH='/home/vahid/file-server/'" > .env
mkdir /home/vahid/file-server/
python3 .ask_username.py
source .env
sudo touch /etc/nginx/sites-available/file-server
sudo touch /etc/nginx/sites-enabled/file-server
sudo chown $FILE_SERVER_OWNER /etc/nginx/sites-available/file-server
sudo chown $FILE_SERVER_OWNER /etc/nginx/sites-enabled/file-server
chmod 644 /etc/nginx/sites-available/file-server 
chmod 644 /etc/nginx/sites-enabled/file-server 

echo "All done:))"

