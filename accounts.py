accounts = {}
#Stores user account details

def add_account(name, password):
#adds user details to accounts


    name = input("Enter New User name: ")
    password = input("Enter new user password: ")

    accounts[password] = name

    return accounts


def login(name, password):
    
    key, value = password, name

    if key in accounts and value == accounts[key]:
        print("Login Accepted: Welcome")
        return True

    else:
        print("You are not registered!")
        return False