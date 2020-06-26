import pwd

def ask_username():
    while True:
        input_user = input('this prompt is persistent until you type the right user name.\ntype your login user name: ')
        for pass_entry in pwd.getpwall():
            if input_user == pass_entry[0]:     
                return input_user


print(ask_username())
