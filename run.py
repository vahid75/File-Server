import socket , os


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

local_ip = get_local_ip()
nginx_server_block_config = ("server {\n"
    "listen 80 ;\n"
    "listen [::]:80;\n"
    f"server_name {local_ip};\n"

    "location /  {\n"
        "proxy_pass http://127.0.0.2:8000/;\n"
        "proxy_set_header X-Real-IP $remote_addr;\n"
    "}\n"
    "location =/  {"
        "proxy_pass http://127.0.0.2:8000/register;\n"
        "proxy_set_header X-Real-IP $remote_addr;\n"
    "}\n"
    
    "location /download {\n"
        "alias /home/vahid/;\n"
        "autoindex on;\n"
    "}\n"
       
    "client_max_body_size 200M;\n"
"}")

with open('/etc/nginx/sites-available/file-server', 'w+') as nginx_server_block_file:
    nginx_server_block_file.write(nginx_server_block_config)



os.environ['DEBUG'] = 'True'
os.environ['ALLOWED_HOSTS'] = f'127.0.0.2,{local_ip}'
os.system('python3 manage.py migrate')
os.system('python3 manage.py runserver 127.0.0.2:8000')