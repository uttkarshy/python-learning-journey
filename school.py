from getpass import getpass
username="admin"
password="admin123"
user=input("Enter your username:")
pass21=getpass("Enter your password:")
if user==username and pass21==password:
    print("Login successful!")
else:
    print("Invalid username or password.")