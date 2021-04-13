# This Module has the Functions that Verify the Requirements of the Project

# Importing Required Modules

import mysql.connector as con
from mysql.connector.errors import ProgrammingError, Error
import core.InsertData as Insert

# Functions


def CheckDatabase():
    """
    CheckDatabase() -> Checks if the Database required Exists or not

    Parameters -> None
    """

    print("Checking Database Requirements..")

    db = con.connect(host="localhost", user=YOUR_USERNAME,
                     database="", password=YOUR_PASSWORD)
    cur = db.cursor()
    result = None

    try:
        cur.execute("use railway;")
    except ProgrammingError:
        print("Database does not Exist!")
        result = False
    else:
        result = True

    if result is True:
        print("Database exists!")
    else:
        print("Creating Database with the Required Tables..")
        print("Please be Patient!")
        cur.execute("create database railway;")
        cur.execute("use railway;")
        CreateTables()
        print("Database and Tables Created!")

    cur.close()
    db.close()


def CreateTables():
    """
    CreateTables() -> Creates all the Required Tables

    Parameters -> None
    """

    db = con.connect(host="localhost", user=YOUR_USERNAME,
                     database="railway", password=YOUR_PASSWORD)
    cur = db.cursor()

    cur.execute(
        "create table train_info (Train_No varchar(10) NOT NULL, Station_Code varchar(20) NOT NULL, Station_Name varchar(30) NOT NULL, Arrival_Time varchar(20) NOT NULL, Departure_Time varchar(20) NOT NULL, Distance varchar(10) NOT NULL, Source_Station_Code varchar(20) NOT NULL, Source_Station_Name varchar(70) NOT NULL, Destination_Station_Code varchar(20) NOT NULL, Destination_Station_Name varchar(60) NOT NULL);")

    cur.execute("create table bookings (Train_No int NOT NULL, Passenger_Name varchar(30) NOT NULL, Mobile_No varchar(10) NOT NULL, Passenger_Adhaar varchar(12) NOT NULL, Date_Of_Booking varchar(20) NOT NULL, Booking_ID int NOT NULL, Class varchar(20) NOT NULL);")

    Insert.InsertDataTrain()

    cur.close()
    db.close()


def CheckConnection():
    """
    CheckConnection() -> Tests the Connection with the Mysql Server

    Parameter -> None
    """

    try:
        print("Checking the Connection to the MySQL Server..")
        connection = con.connect(host='localhost',
                                 database='',
                                 user=YOUR_USERNAME,
                                 password=YOUR_PASSWORD)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server Version", db_Info)

    except Error:

        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True
