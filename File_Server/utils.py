from django.conf import settings
import os


def saving_file(file_object):
    input_file_name = file_object.name
    file_name , file_extenstion = naming_file(input_file_name)  
    file_server_path = os.environ.get('FILE_SERVER_PATH')
    if not file_server_path:
        raise ValueError('You should specify the directory path you wish to store files in it.')
    
    if file_extenstion:
        with open(
            f"{file_server_path}{file_name}.{file_extenstion}", "wb"
        ) as des_file:
            for chunk in file_object.chunks():
                des_file.write(chunk)
    else:
        with open(
            f"{file_server_path}{file_name}", "wb"
        ) as des_file:
            for chunk in file_object.chunks():
                des_file.write(chunk)


def naming_file(input_file_full_name):
    if '.' in input_file_full_name:
        name_parts = input_file_full_name.split(".")[:-1]
        file_name =  ''
        for name_part in name_parts:
            file_name += name_part
        file_extenstion = input_file_full_name.split(".")[-1]
    else:
        file_name , file_extenstion  = input_file_full_name , None

    return (file_name , file_extenstion)


def ip_list_generator(ip_file_object):
    ip_list = [ip.strip('\n') for ip in ip_file_object.readlines()]
    return ip_list


def authorize_with_ip(client_ip_address):
    with open(settings.CLIENT_IP_ADDRESS_FILE , 'r') as registered_ip_file:
        with open(settings.PERMITTED_CLIENT_IP_ADDRESS_FILE , 'r') as permitted_ip_file:
            registered_ip =ip_list_generator(registered_ip_file)
            permitted_ip = ip_list_generator(permitted_ip_file)
            if client_ip_address  in (registered_ip and permitted_ip):
                return True
    
    return False