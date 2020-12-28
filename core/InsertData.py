# This Module has the Functions to Insert the Data in the MySQL Tables

# Importing Required Modules

import csv
import mysql.connector as con

# Functions


def InsertDataTrain():
    """
    InsertDataTrain() -> Inserts all the Train details in the train_info Table

    Parameters -> None
    """

    mn = con.connect(host="localhost",
                     user="root",
                     password="aryan",
                     database="railway")

    cur = mn.cursor()

    # Iterating through all the values and insert's them in the table
    # Replace the path below with the relative path of the file on your computer
    try:
        # Change the Location of the File here
        with open("C:\Railway\Assets\Train_details.csv") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                cur.execute(
                    'INSERT INTO train_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not or try changing the Location in Other.py")
    finally:
        mn.commit()  # Important: Commiting the Changes
        cur.close()
        mn.close()
