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
import pandas as pd
import numpy as np

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
        print("\nPlease enter your age, gender, height, and weight.\n")
        print("Data should be four values, separated by commas.\n")
        print("Example: 25, Male, 180, 80\n")

        data_str = input("\nEnter your data here:\n")

        user_data = [item.strip() for item in data_str.split(",")]

        # Validate user data
        if validate_input(user_data):
            print("\nData is valid! ")
            break

    return user_data

def validate_input(data):
    """
    Validate the input data. The age should be a positive integer, the gender
    should be either 'Male' or 'Female', and the height and weight should be
    positive numbers. If the data is valid, the function returns True;
    otherwise, it prints an error message and returns False.
    """
    try:
        age = int(data[0])
        gender = data[1]
        height = float(data[2])
        weight = float(data[3])

        if age <= 0:
            raise ValueError("Age must be a positive number.")
        if gender not in ['Male', 'Female']:
            raise ValueError("Gender must be 'Male' or 'Female'.")
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")
    except ValueError as e:
        print(f"Invalid input: {e}\n")
        return False

    return True

def calculate_bmi_and_update_sheet(data):
    """
    Calculate BMI and update the Google Sheet with the new data. The function
    calculates the BMI based on the height and weight, determines the weight
    category based on the BMI, and appends a new row to the Google Sheet with
    the age, gender, height, weight, BMI, and weight category. Finally, it
    compares the user's BMI with the median BMI in the Google Sheet.
    """
    age = int(data[0])
    gender = data[1]
    height = float(data[2])
    weight = float(data[3])

    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)
          
    # Determine weight category
    if bmi < 18.5:
        category = 'Underweight'
    elif bmi < 24.9:
        category = 'Normal weight'
    elif bmi < 29.9:
        category = 'Overweight'
    else:
        category = 'Obese'
 

    # Get the ID for the new row
    # Fetch all data from the worksheet
    worksheet_data = obesity.get_all_values() 
    id = len(worksheet_data) + 1

    # Append to Google Sheet with all values as strings
    # Use format() to control number of decimal places
    obesity.append_row([str(id), str(age), gender, format(height, '.0f'), format(weight, '.0f'), format(bmi, '.1f'), category])

    return bmi  # return the calculated bmi

    
def compare_with_median(user_bmi):
    """
    Compare the user's BMI with the median BMI in the Google Sheet. The function
    retrieves the BMI data from the sheet, calculates the median BMI, and prints
    a message indicating whether the user's BMI is below, above, or equal to the
    median.
    """
    # Get the BMI data from the sheet
    data = obesity.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])
    df['BMI'] = pd.to_numeric(df['BMI'], errors='coerce')

    # Check if 'BMI' column is not empty and contains at least one non-NaN value
    if df['BMI'].count() > 0:

        # Calculate the median BMI
        median_bmi = df['BMI'].median()
    
        # Compare the user's BMI with the median and print a message
        if user_bmi > median_bmi:
            print(f"Your BMI is above the median BMI of {median_bmi}.\n")
        elif user_bmi < median_bmi:
            print(f"Your BMI is below the median BMI of {median_bmi}.\n")
        else:
            print(f"Your BMI is equal to the median BMI of {median_bmi}.\n")
    else:
        print("Unable to calculate median BMI because there is no BMI data.\n")

def explore_data():
    """
    Perform data exploration. The function retrieves the data from the Google
    Sheet, calculates and prints descriptive statistics, and allows the user to
    filter the data by gender, age, or weight category.
    """
    # Get the data from the sheet
    data = obesity.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])

    # Convert numerical columns to the proper data type
    df['Age'] = df['Age'].astype(int)
    df['Height'] = df['Height'].astype(float)
    df['Weight'] = df['Weight'].astype(float)
    df['BMI'] = df['BMI'].astype(float)

    return df

def print_descriptive_statistics(df):
    """
    Print descriptive statistics of the Google Sheet data. The function
    retrieves the data from the sheet, calculates several descriptive
    statistics, and prints them.
    """
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
    df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
    df['BMI'] = pd.to_numeric(df['BMI'], errors='coerce')

    count = len(df)
    median_age = df['Age'].median()
    median_height = df['Height'].median()
    median_weight = df['Weight'].median()
    median_bmi = df['BMI'].median()

    
    print("Here are some descriptive statistics of the data:")
    print(f"Number of entries: {count:.0f}")
    print(f"Median age: {median_age:.0f}")
    print(f"Median height: {median_height:.0f}")
    print(f"Median weight: {median_weight:.0f}")
    print(f"Median BMI: {median_bmi:.1f}\n")

 

def main():
    user_data = get_user_data()
    user_bmi = calculate_bmi_and_update_sheet(user_data)
    compare_with_median(user_bmi)
    df = explore_data()
    print_descriptive_statistics(df)
 
    
    
main()
