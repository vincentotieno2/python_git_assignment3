correct_password= "1234"

for attempt in range (3):
    password= input("Enter your  bank password: ")
    if password == correct_password:
        print("Access granted")
        break
    else :
        print("wrong password")
else:
    print("Account locked. Too many attempts")
#hhhhyyyy