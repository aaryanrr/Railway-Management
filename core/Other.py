# This Module has some Other Commonly used Functions

# Importing Required Modules

import os
import time


# Functions

def About():
    """
    About() -> Prints the About Information on the Terminal

    Parameters -> None
    """
    # Change the path given here to the absolute path of the README file
    with open(FULL_PATH_TO_THE_README_FILE) as file:
        data = file.read()
        print(data)


def ClearScreen():
    """
    ClearScreen() -> Clears the Terminal Screen

    Parameters -> None
    """

    print("Clearing..")
    time.sleep(2)
    os.system("cls")


def Menu(answer="Yes"):
    """
    Menu() -> Displays the Menu

    Parameters -> Answer (User's Choice on Displaying the Menu, by default it is set to True)
    """

    if answer in ["Yes", "Y"]:
        print("  WELCOME TO RAILWAY RESERVATION SYSTEM")
        print("1. Book a Ticket")
        print("2. Cancel a Booking")
        print("3. Check Fares")
        print("4. Show my Bookings")
        print("5. Show Available Trains")
        print("6. Clear Screen")
        print("7. Menu")
        print("8. About")
        print("9. Exit")
    else:
        pass
