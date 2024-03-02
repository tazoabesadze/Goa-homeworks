authorized = False
password = 12345

while authorized != True:
    user_input = int(input("enter your password: "))

    if password == user_input:
        print("password is corect")
        authorized = True