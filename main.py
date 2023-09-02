from functions import *
import re

print("~~    Welcome to BookMyMovieTicket.com    ~~")

str1 = '''Enter : \n 1. Show the seats\n 2. Book Ticket\n 3. Show the Statistics\n 4. Show Booked Tickets Info\n 0. Exit'''

choice = 1              # default value except 0
obj = bookMyShow()
while choice != 0:
    print(str1)
    choice = int(input("Enter your choice : "))

    if choice == 1:
        obj.display_seats()

    elif choice == 2:
        name = input("Enter your name : ")
        gender = input("Enter your gender (F/M): ")

        age = int(input("Enter your age : "))
        if age >= 18 :
            print("You are permitted to get a booking.")
        else:
            print("Sorry ! You are underage and not permitted to get in.")
            break

        phone = input("Enter your mobile number : ")
        res = re.findall("^[1-9]{1}[0-9]{9}$ ", phone) 
        if res: 
            print("Yes! its right no.")
        else: 
            print("Enter correct 10 digit number")

        obj.book_ticket(name, gender, age, phone )


    elif choice == 3:
        obj.statistics()

    elif choice == 4:
        obj.show_booked_tic_info()

    else:
        break

            