from getpass import getpass
counter=3
username="admin"
password="password"
while counter > 0:
    username1=input("Enter the username ")
    password1=getpass("Enter the password ")
    if username1==username and password1==password:
        print("Access granted")
        break
    else:
        counter-=1
        print("Access denied. You have", counter, "attempts left.")
print("Account Locked.")