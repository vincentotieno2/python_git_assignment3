count = 1

while count<10:
    print(count, end="\n")
    count+=1

correct_password="1234"
attempts=3
while attempts>0:
    password=input("Enter your password: ")
    if password==correct_password:
        print("Access granted")
        break
    else:
        attempts-=1
        print("Wrong password. Attempts left:", attempts)
else:
    print("Access locked")

choice=""
while choice!="q":
    print("Menu:")
    print("1. Check balance")
    print("2. Withdraw")
    print("q. Quit")
    choice=input("Enter your choice:")
    if choice=="1":
        print("Your balance is 10000")
    elif choice == "2":
        print("Your withdrawal is successful")
    elif choice == "q":
        print("Goodbye")
    else:
        print("Invalid Option")

numbers= [21, 23,43,45,78, 87, 98]
index=0
while index<len(numbers):
    print(numbers[index], end="\n")
    index+=1

