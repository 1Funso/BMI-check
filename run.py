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
Obesity = SHEET.worksheet('Obesity')

data = Obesity.get_all_values()

print(data)