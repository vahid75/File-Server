import pwd

def ask_username():
    while True:
        input_user = input('this prompt is persistent until you type the right user name.\ntype your login user name: ')
        for pass_entry in pwd.getpwall():
            if input_user == pass_entry[0]:     
                return input_user


with open('.env' , 'a+') as env_file:
    env_file.write(f'export FILE_SERVER_OWNER="{ask_username()}"')
