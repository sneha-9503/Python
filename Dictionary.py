#Dictionary storing username and password
users={"Alice":"password123","Bob":"secure456","David":"qwerty789"}
#simulate the login
username_input=input("Enter Username:")
password_input=input("Enter Password:")
#check the login
if username_input in users:
    if users[username_input]==password_input:
        print("Login Successful")
    else:
        print("Incorrect password!")
else:
    print("Users not found!")
