import json

class bookMyShow:
    def __init__(self):
        self.rows = 10
        self.cols = 8
        self.total = self.rows * self.cols
        self.price = 10

        try:
            with open("user_data.json", "a+") as file:
                self.data = json.load(file)
                self.user_data = self.data
        except:
            self.user_data = {}                             # all users data stored here


    def display_seats(self):
        for i in range (self.rows + 1):
            for j in range(self.cols + 1):
                if i == 0:
                    if j == 0:
                        print(" ", end = ' ')               # empty space for 1st block
                    else:
                        print(j, end = ' ')            # for 1st line print nos from 1 to 8
                else:
                    if j == 0:
                        print(i, end = ' ')
                    else:
                        seat = str(i) + str(j)
                        if seat in self.user_data.keys():
                            print("B", end = ' ')              # occupied seats 
                        else:
                            print("S", end = ' ')              # vacant seats
            print()

    
    def book_ticket(self, name, gender, age, phone):
        user = {}                                                # temp dict for 1 user at a time
        row = input("Enter the row number >> ")
        col = input("Enter the seat in selected row >> ")
        seat_no = row + col

        if self.is_available(row, col):
            if self.total > 60:
                if int(row) > self.rows//2:
                    self.price = 8
                else:
                    self.price = 10
            else:
                self.price = 10

            print("Price of this seat is : ", self.price) 
            print("Do you want to continue ? : ")
            ask = input("Enter Y to continue and N to exit : ")
            if ask.lower() == 'y':
                user['Name'] = name
                user['Gender'] = gender
                user['Age'] = age
                user['PhoneNo'] = phone
                user['Price'] = self.price

                self.user_data[seat_no] = user             # seat_no as unique key, & details as value in USER_DATA

                with open("user_data.json", "w") as file:
                    json.dump(self.user_data, file)
                    print("------ Ticket Booked Successfully !! ------")        
        else:
            print("------ Seat not Available!! Please select another Seat. ------ ")


    def is_available(self, row, col):
        seat = row + col
        if seat in self.user_data.keys():
            return False                                    # already taken by someone
        else:
            return True                                     # available


    def statistics(self):
        purchased_ticks = len(self.user_data.keys())
        percent_purchased = (purchased_ticks / self.total)*100

        current_income = 0
        for k,v in self.user_data.items():
            current_income += v['Price']

        if self.total > 60:
            half = self.rows//2
            total1 = half * self.cols * 10
            total2 = (self.rows - half) *self.cols * 8
            total_income = total1 + total2
        else:
            total_income = 10 * self.total

        stats = f" Purchased Tickets : {purchased_ticks}\n Percent of purchased tickets : {percent_purchased}\n Current Income : {current_income}\n Total Income : {total_income}"
        print(stats)


    def show_booked_tic_info(self):
        for k,v in self.user_data.items():
            print("Seat No. : ", k, end = "--> ")   
            print("User_Info : ", v)


    def exit(self):
        pass
