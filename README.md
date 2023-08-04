# Obesity Data Automation Program

A program designed to collect, analyze, and visualize obesity data.

## GitHub Repository <a name="github"></a>

You can find the GitHub repository by clicking [here](https://github.com/1Funso/BMI-check).

## Live Deployment <a name="live"></a>

The live deployment of the project can be accessed by clicking [here](https://bmi-check-1-8c96fcfba012.herokuapp.com/).


## Table of Contents

- [Description](#description)
- [Features](#features)
- [Testing](#testing)
- [Bugs and Solutions](#bugs)
- [Validator Testing](#validator)
- [Deployment](#deployment)
- [Credits](#credits)

## Description <a name="description"></a>

The Obesity Data Automation Program is designed to facilitate the collection and analysis of obesity-related data. Users can input their age, gender, height, and weight, and the program calculates their BMI, categorizes their weight, and updates a Google Sheet with this information.

## Features <a name="features"></a>

- Data collection: The program collects user data via the terminal.
- Data analysis: The program calculates the user's BMI and categorizes their weight.
- Data storage: The program updates a Google Sheet with the user's data.
- Data exploration: The program allows the user to explore the data by printing descriptive statistics.

## Testing <a name="testing"></a>

The program has been tested extensively both in a local terminal and in a Heroku terminal. All tests passed successfully.

## Bugs and Solutions <a name="bugs"></a>

1. **Bug:** Data validation did not handle non-numeric input correctly.
    **Solution:** Added a try/except block to convert input to the appropriate numeric type and handle exceptions.

2. **Bug:** The program did not handle missing input correctly.
    **Solution:** Added checks to ensure that all required data fields are provided by the user.

3. **Bug:** Error when trying to update the Google Sheet if the user does not have edit permissions.
    **Solution:** Added error handling to provide a meaningful error message to the user and continue with the program execution.

## Validator Testing <a name="validator"></a>

The Python code in the program has been checked using the Code Institute PEP8 validator and it passed with no issues.

## Deployment <a name="deployment"></a>

The program has been deployed to Heroku. The deployment process is as follows:

1. Fork or clone this repository.
2. Create a new Heroku app.
3. Set the buildpacks to Python and NodeJS in that order.
4. Link the Heroku app to the repository.
5. Click on Deploy.

## Credits <a name="credits"></a>

- Code Institute for providing the deployment guide.
- Kaggle for providing the initial obesity dataset. Credit to  [SUJITH K MANDALA - Obesity Classification Dataset].

