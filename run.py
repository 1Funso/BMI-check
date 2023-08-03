"""
Obesity Data Automation Program

This program asks the user to input their age, gender, height, and weight.
It then calculates the user's BMI, determines their weight category, and
updates a Google Sheet with this information. Additionally, it allows the
user to explore the data by printing descriptive statistics and filtering
the data by gender, age, or weight category.
"""

import gspread
from google.oauth2.service_account import Credentials


# Google Sheets authentication
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Obesity')

# Open 'Obesity' worksheet
obesity = SHEET.worksheet('Obesity')

def get_user_data():
    """
    Get user data input from the terminal. The user is prompted to enter
    their age, gender, height, and weight, separated by commas. The function
    continues to prompt the user until valid data is entered.
    """
    while True:
        print("Please enter your age, gender, height, and weight.")
        print("Data should be four values, separated by commas.")
        print("Example: 25, Male, 180, 80\n")

        data_str = input("Enter your data here: ")

        user_data = data_str.split(",")

        # Validate user data
        if validate_input(user_data):
            print("Data is valid!")
            break

    return user_data
    