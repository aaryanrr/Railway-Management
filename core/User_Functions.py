# This Module has the Functions that allow a User to do Certain Task's

# Importing Required Modules

import mysql.connector
import os
import datetime
import time
from mysql.connector import DataError
import random

# Defining the per/km Charge of each Class
sleeper_charge = int(1.5)
third_ac_charge = int(2)
second_ac_charge = int(3)
first_ac_charge = int(4)

# Defining Some Initial Variables
current_date = datetime.date.today()

# A Ticket can be Booked 4 Months before the Actual Trip
max_date = current_date + datetime.timedelta(days=120)


# Functions


def AvailableTrains():
    """
    AvailableTrains() -> Shows the List of Available Trains according to the User Requirement

    Parameters -> None   
    """

    mn = mysql.connector.connect(host="localhost", user=YOUR_USERNAME,
                                 password=YOUR_PASSWORD, database="railway")
    cur = mn.cursor()

    print("Search by Entering the Station Codes!")
    start_opt = input("From: ")
    final_opt = input("To: ")
    date = input("Date(YYYY-MM-DD): ")
    date_user = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    while date_user < current_date or date_user > max_date:
        print("Please enter a Valid Date!")
        date = input("Date(DD/MM/YYYY): ")
        date_user = datetime.datetime.strptime(date, "%Y-%m-%d")
        date_user = date_user.date()

    cur.execute(
        'SELECT Train_No, Source_Station_Name, Destination_Station_Name, Arrival_Time, Departure_Time from train_info where Source_Station_Code="{}" AND Destination_Station_Code="{}";'.format(
            start_opt, final_opt))
    result = cur.fetchall()
    os.system("cls")
    time.sleep(1)
    head = ["Train_No", "Source_Station_Name",
            "Destination_Station_Name", "Arrival_Time", "Departure_Time"]
    if len(result) >= 10:
        try:
            print("Total of", len(result), "Records Found!")
            ask = int(input("Enter the Number of Records you want to See: "))
        except ValueError:
            print("Please Enter a Valid Integer!")
        else:
            print(head)
            print(" ")
            for x in range(ask):
                print(result[x], "\n")
    elif len(result) == 0:
        print("No Trains Available!")
    else:
        print(head)
        print(" ")
        for x in result:
            print(x, "\n")

    cur.close()
    mn.close()


def CheckFare():
    """
    CheckFare() -> Calculates the Fare based on the Distance

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user=YOUR_USERNAME,
                                 password=YOUR_PASSWORD, database="railway")
    cur = mn.cursor()

    print("Search by Entering the Station Code!")

    header = [("Train_No", "Distance", "Sleeper",
               "Third_AC", "Second_AC", "First_AC")]
    start_opt = input("From: ")
    final_opt = input("To: ")

    cur.execute(
        'SELECT Train_No, Distance from train_info where Source_Station_Code="{}" AND Destination_Station_Code="{}";'.format(
            start_opt, final_opt))
    result_fare = cur.fetchall()
    time.sleep(1)
    os.system("cls")
    if len(result_fare) >= 10:
        try:
            print("Total of", len(result_fare), "Records Found!")
            ask = int(input("Enter the Number of Records you want to See: "))
        except ValueError:
            print("Please Enter a Valid Integer!")
        else:
            print(header)
            print(" ")
            for x in range(ask):
                y = result_fare[x]
                print(result_fare[x], "Rs.", int(y[1]) * sleeper_charge, "Rs.", int(y[1]) * third_ac_charge, "Rs.",
                      int(y[1]) * second_ac_charge, "Rs.", int(y[1]) * first_ac_charge, "\n")
    elif len(result_fare) == 0:
        print("No Available Trains!")
    else:
        print(header)
        print(" ")
        for x in result_fare:
            print(x, "Rs.", int(x[1]) * sleeper_charge, "Rs.", int(x[1]) * third_ac_charge, "Rs.",
                  int(x[1]) * second_ac_charge, "Rs.", int(x[1]) * first_ac_charge, "\n")

    cur.close()
    mn.close()


def ShowBookings():
    """
    ShowBookings() -> Shows the Bookings Made by an User

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user=YOUR_USERNAME,
                                 password=YOUR_PASSWORD, database="railway")
    cur = mn.cursor()

    mobile_no = input("Please Enter your 10 Digit Mobile Number: ")

    cur.execute('SELECT * FROM bookings where Mobile_No="{}"'.format(mobile_no))

    result = cur.fetchall()
    if len(result) == 0:
        print("No Records Found!")
    else:
        booking_no = 1
        print(["Train_No", "Passenger_Name", "Mobile_No",
               "Passenger_Adhaar", "Time_Of_Booking", "Booking_ID", "Class"])
        for x in result:
            print("BOOKING NO", booking_no, ":", x, "\n")
            booking_no += 1

    cur.close()
    mn.close()


def BookTrain():
    """
    BookTrain() -> Let's a User Book a Train

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user=YOUR_USERNAME,
                                 password=YOUR_PASSWORD, database="railway")
    cur = mn.cursor()
    while True:
        try:
            train_no = int(input("Train Number: "))
        except ValueError:
            print("Please Enter a Valid Train Number!")
            continue
        else:
            break

    while True:
        Name = input("Enter your Name: ")
        if len(Name) == 0:
            print("Please Enter a Name!")
        elif len(Name) > 30:
            print("Name too Long!")
        else:
            break

    while True:
        try:
            Mobile = int(input("Enter your Mobile Number: "))
        except ValueError:
            print("Please Enter a Valid Mobile Number!")
            continue
        else:
            if len(str(Mobile)) == 10 and Mobile != 0000000000:
                break
            elif len(str(Mobile)) > 10 or len(str(Mobile)) < 10:
                print("Please Enter a Valid 10 Digit Mobile Number!")
            else:
                print("Please Enter a Valid Phone Number!")

    while True:
        try:
            adhaar = int(input("Enter you Adhaar Number: "))
        except ValueError:
            print("Please Enter a Valid Adhaar Number!")
            continue
        else:
            if len(str(adhaar)) == 12 and adhaar != 000000000000:
                break
            elif len(str(adhaar)) > 12 or len(str(adhaar)) < 12:
                print("Please Enter a Valid 12 Digit Adhaar Number!")
            else:
                print("Please Enter a Valid Adhaar Number!")

    Time_of_Booking = datetime.datetime.now()
    date = Time_of_Booking.date()
    date = date.strftime("%d-%m-%y")

    # Creating Unique ID for each Booking
    id = random.randint(1, 10000)
    cur.execute("SELECT Booking_ID FROM BOOKINGS")
    result = cur.fetchall()
    Used_ID = []
    for x in result:
        for y in x:
            Used_ID.append(y)
    while True:
        if id in Used_ID:
            id = random.randint(1, 10000)
        else:
            break

    print(["Sleeper", "AC-1", "AC-2", "AC-3"])
    Class = None
    while True:
        ask = input("Please Enter a Class from the one's given above: ")
        if ask == "Sleeper":
            Class = "Sleeper"
            break
        elif ask == "AC-1":
            Class = "AC-1"
            break
        elif ask == "AC-2":
            Class = "AC-2"
            break
        elif ask == "AC-3":
            Class = "AC-3"
            break
        else:
            print(["Sleeper", "AC-1", "AC-2", "AC-3"])
            print("Please Choose an Option from Above!")

    while True:
        ask = input("Are you Sure you want to Book(Y/N): ")
        if ask in ["Y", "y"]:
            print("Booking...")
            try:
                query = "INSERT INTO bookings values({}, '{}', '{}', '{}', '{}', {}, '{}')".format(
                    train_no, Name, Mobile, adhaar, date, id, Class)
                cur.execute(query)
            except DataError:
                print("Error in Booking!")
            else:
                print("Successfully Booked!")
                mn.commit()
                cur.close()
                mn.close()
                break
        elif ask in ["N", "n"]:
            print("Stopping Booking...")
            time.sleep(0.5)
            os.system("cls")
            break
        else:
            print("Please Enter Y (Yes) or N (No)!")


def CancelBooking():
    """
    CancelBooking() -> Allows a User to Cancel Booking

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user=YOUR_USERNAME,
                                 password=YOUR_PASSWORD, database="railway")
    cur = mn.cursor()

    print("Please use the Show my Bookings Option\n to get the Unique ID of the Booking you want to Cancel!")

    while True:
        try:
            unique_id = int(input("Enter the Unique ID: "))
        except ValueError:
            print("Please Enter a Valid ID!")
        else:
            if len(str(unique_id)) == 0:
                print("Invalid ID!")
            elif unique_id < 1:
                print("ID Out of Range!")
            elif unique_id > 10000:
                print("ID Out of Range!")
            elif len(str(unique_id)) != 0 and unique_id >= 1 and unique_id <= 10000:
                cur.execute(
                    "SELECT * FROM bookings WHERE Booking_ID={}".format(unique_id))
                result = cur.fetchall()
                if len(result) == 0:
                    print("No Records Found!")
                    break
                print(["Train_No", "Passenger_Name", "Mobile_No",
                       "Passenger_Adhaar", "Time_Of_Booking", "Booking_ID"])
                for x in result:
                    print(x)
                while True:
                    ask = input("Are you Sure you want to Cancel this(Y/N): ")
                    if ask in ["Y", "y"]:
                        cur.execute(
                            "DELETE FROM bookings WHERE Booking_ID={}".format(unique_id))
                        print("Deleted!")
                        mn.commit()
                        cur.close()
                        mn.close()
                        break
                    elif ask in ["N", "n"]:
                        break
                    else:
                        print("Please Enter either Y (Yes) or N (No)!")
                break
            else:
                print("Please Enter a Valid ID!")
