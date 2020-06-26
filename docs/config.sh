sudo apt install python3 nginx
python_path=$(which python3)
mkdir file_server/
cd file_server/
virtualenv .venv -p $python_path
source .venv/bin/activate
#git clone pytohn project
#cd pytohn project  
pip install -r requierments.txt
touch .env
echo "export FILE_SERVER_PATH='/home/vahid/file-server/'" > .env
python3 .ask_username.py
source .env
sudo touch /etc/nginx/sites-available/file-server
sudo touch /etc/nginx/sites-enabled/file-server
sudo chown $FILE_SERVER_OWNER /etc/nginx/sites-available/file-server
sudo chown $FILE_SERVER_OWNER /etc/nginx/sites-enabled/file-server
chmod 644 /etc/nginx/sites-available/file-server 
chmod 644 /etc/nginx/sites-enabled/file-server 

echo "All done:))"

