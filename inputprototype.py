username = ""
while username=="":
    username = input("Name: ")
print("Good Day "+ username)
print("Good Morning {0}".format(username))

password = ""

while password=="":
    password = input("Password: ")
if password=="L":
    print("Welcome L")
else:
    print("Incorrect Login")
