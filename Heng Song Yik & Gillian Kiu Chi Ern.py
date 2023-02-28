# Heng Song Yik
# TP064053
# Gillian Kiu Chi Ern
# TP064022
def admin():
    while True:
        username = input("Username= ")
        password = input("Password= ")
        if username == "Admin012" and password == "0123":
            print("Hello Admin012")
            while True:
                function = input("Please Select Number of Function \n 1. Add event \n 2. Modify event record \n 3. "
                                 "Display all records \n 4. search record \n 5. Log Out \n")
                if function == "1":
                    category = input("Enter the Event Category: \n")
                    event_name = input("Name of the event = \n")
                    event_date = input("Date of the event = \n")
                    event_location = input("Location of the event= \n")
                    event_Fee = input("Payment of event= \n")
                    f1 = open("Event.txt", "a")
                    f1.write(category + ", " + event_name + ", " + event_date + ", " + event_location + ", " +
                             event_Fee + "\n")
                    f1.close()
                elif function == "2":
                    temp = open("Event.txt", "r")
                    file = temp.readlines()
                    new = file
                    temp.close()
                    edit = input("Enter the record name that you want to edit: \n ")
                    for i in file:
                        if edit in i:
                            print(i)
                            while True:
                                DC = input("Is this the record that you want to edit? \n 1. Yes \n 2. No \n")
                                if DC == "1":
                                    record = file.index(i)
                                    db = open("Event.txt", "w")
                                    category = input("Enter the Event Category = \n")
                                    event_name = input("Name of the event = \n")
                                    event_date = input("Date of the event = \n")
                                    event_location = input("Location of the event = \n")
                                    event_Fee = input("Payment of event = \n")
                                    new[record] = (category + ", " + event_name + ", " + event_date + ", " +
                                                   event_location + ", " + event_Fee + "\n")
                                    for i in new:
                                        db.write(i)
                                    print("You have successfully edit your record")
                                    db.close()
                                    break
                                elif DC == "2":
                                    break
                                else:
                                    print("Please reselect")
                                    break
                elif function == "3":
                    print("Event List")
                    db = open("Event.txt", "r")
                    for i in db:
                        print(i.strip())
                    db.close()
                    print("Payment List")
                    db = open("Payment.txt", "r")
                    for i in db:
                        print(i.strip())
                    db.close()
                elif function == "4":
                    while True:
                        search = input("What to you want to search? \n 1. Event \n 2. Payment \n 3. Exit \n")
                        if search == "1":
                            db = open("Event.txt", "r")
                            key = input("Enter the keyword \n")
                            for i in db:
                                if key in i:
                                    print(i.strip())
                            break
                        elif search == "2":
                            db = open("Payment.txt", "r")
                            key = input("Enter the keyword")
                            for i in db:
                                if key in i:
                                    print(i.strip())
                            break
                        elif search == "3":
                            break
                        else:
                            print("Please reselect")
                elif function == "5":
                    exit()
                else:
                    print("Please reselect")
        else:
            print("Invalid username or password")


def register():
    register_list = open("List.txt", "r")
    while True:
        name = input("Username:")
        password = input("password:")
        CP = input("Please enter again your password:")
        if password != CP:
            print("The password doesn't match! Please try again")
        else:
            if len(CP) <= 8:
                print("The password should longer than 8 character")
            elif name in register_list:
                print("The username is used!")
            else:
                List = open("List.txt", "a")
                List.write(name + ", " + password + "\n")
                print("Register Success!")
                break


def login():
    list = []
    while True:
        list01 = open("List.txt")
        name = input("Enter your username \n")
        password = input("Enter your password \n")
        for i in list01:
            list.append(i)
        if name + ", " + password + "\n" in list:
            print("Log in successful")
            print("Welcome " + name)
            break
        else:
            print("Incorrect username or password")


def Registered_Customer():
    while True:
        function = input("Please Select Number of Function \n 1. View Event \n 2. Add Event to the cart and make "
                         "payment \n 3. Log Out \n")
        if function == "1":
            db = open("Event.txt", "r")
            for i in db:
                print(i.strip())
            db.close()
        elif function == "2":
            db = open("Event.txt", "r")
            print("Event")
            for i in db:
                print(i.strip())
            db.close()
            item = input("Enter the event name that you want to add to cart \n")
            price = (input("Enter the price of the event \n"))
            print("The event in the cart is", item, "and the price is RM", price)
            attendee = input("Please Enter your username \n")
            number = input("Please enter your phone number, our customer service department will call you to do the "
                           "payment\n")
            db = open("Payment.txt", "a")
            db.write(attendee + ", " + number + ", " + item + ", " + price + "\n")
            print("Successful, Customer service will call you shortly")
        elif function == "3":
            break
        else:
            print("Please reselect")


print("Welcome To Asian Event Management Service")
while True:
    role = input("Please select your role \n 1. Admin \n 2. Registered Customer \n 3. Not Registered Customer \n Role=")
    if role == "1":
        admin()
    elif role == "2":
        login()
        Registered_Customer()
    elif role == "3":
        res = input("Do you want to register as a register customer? \n 1. Yes \n 2. No \n")
        if res == "1":
            register()
        elif res == "2":
            db = open("Event.txt", "r")
            print("Event")
            for i in db:
                print(i.strip())
            db.close()
    else:
        print("Please reselect")
