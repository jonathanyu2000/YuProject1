# Jonathan Yu
# ComputingID: jxy7du

# Imports
import json
import csv
import pandas as pd

# Functions
def validCSV():
    '''
    Determines if CSV file is valid for data processing also retrieves CSV from either local directory or URL
    :return: returns a valid csv file either retrieved locally or from URL
    '''
    validcsv = False
    csvboolean = False
    validurl = False
    csvfile = input("Please type CSV filename you would like to open with CSV extension. "
                    "If you would like to access a CSV file from a url please leave blank and press enter: ")
    # If user decides to retrieve from URL...
    if (len(csvfile) == 0):
        url = input("Please paste a valid url containing CSV file: ")
        csvfile = input("Please type CSV filename ending with '.csv' that you would like to save this file as: ")
        # Checks if name of CSV File is valid and acceptable
        while (csvboolean == False):
            if csvfile[len(csvfile) - 4:] != '.csv' or '/' in csvfile:
                csvfile = input("This is not a valid CSV filename. Please name one ending with '.csv': ")
            else:
                csvboolean = True
        # Checks if URL is valid
        while(validurl == False):
            try:
                URLtoCSV(url, csvfile)
                validurl = True
            except:
                url = input("Please paste a valid url containing CSV file: ")
    # If user decides to retrieve local CSV...
    else:
        # Checks if CSV file is valid
        while(validcsv == False):
            try:
                open(csvfile)
                validcsv = True
            except:
                csvfile = input("Please choose valid CSV file from same directory as Python File: ")
    return csvfile

def CSVtoJSON(csvfile, jsonfile):
    '''
    Converts CSV file into JSON file
    :param csvfile: name of csv file
    :param jsonfile: name of json file
    :return: saves csv file as a json file and prints CSV file has been converted to JSON
    '''
    csvboolean = False
    jsonboolean = False
    # Checks if CSV file and JSON filename is acceptable
    while(csvboolean == False or jsonboolean == False ):
        # Checks for correct CSV file extension
        if csvfile[len(csvfile)-3:] != 'csv':
            csvfile = input("This is not a CSV file. Please type name of file ending with '.csv' and is in local folder: ")
        # Checks to see if CSV file is valid through Try and Except
        else:
            try:
                open(csvfile)
                csvboolean = True
            except:
                csvfile = input("This is not a CSV file. Please type name of file ending with '.csv' and is in local folder: ")
        # Checks to see if JSON filename is acceptable
        if jsonfile[len(jsonfile)-4:] != 'json' or '/' in jsonfile:
            jsonfile = input("This is not a JSON filename. " +
                            "Please type valid JSON filename you would like to save with '.json' extension: ")
        else:
            jsonboolean = True
    templist = []
    # Opens CSV File
    file = open(csvfile)
    dictcsv = csv.DictReader(file)
    # Writes CSV into Python Dictionary
    for row in dictcsv:
        templist.append(row)
    # Turns Python Dictionary into JSON String Format
    jsonString = json.dumps(templist, indent = 4)
    # Writes JSON file
    with open(jsonfile, 'w', encoding = 'utf-8') as jsonf:
        jsonf.write(jsonString)
    print("CSV File has been converted to JSON. ")

def URLtoCSV(url, csvfile):
    '''
    Saves CSV file locally in same directory from URL
    :param url: url of link containing csv file
    :param csvfile: name of csvfile that you want to save retrieved file as
    :return: does not return anything
    '''
    # Reads URL and turns it into dataframe using Pandas Package
    df = pd.read_csv(url)
    # Saves dataframe as CSV file
    df.to_csv(csvfile, index = False)

def SummaryFileCSV(csvfile):
    '''
    Gives summary of rows and columns present in the CSV file
    :param csvfile: Name of CSV File
    :return: prints the number of rows (not including the header) and the number of columns
    '''
    # Checks to see if CSV file is valid
    csvboolean = False
    while (csvboolean == False):

        if csvfile[len(csvfile) - 3:] != 'csv':
            csvfile = input("This is not a CSV file. Please find file ending with '.csv' ")
        else:
            try:
                open(csvfile)
                csvboolean = True
            except:
                csvfile = input("This is not a CSV file. Please find file ending with '.csv' ")
    # Opens CSV File
    file = open(csvfile)
    # Initializing CSV Reader
    reader = csv.reader(file)
    # Reads the header
    header = next(reader)
    # Counts Number of rows excluding header in CSV file
    lines = len(list(reader))
    # Counts Number of columns in CSV file
    columns = len(list(header))
    print("Number of rows (not including header):", lines, "\n" + "Number of columns: ", columns)

def AllColumnsCSV(csvfile):
    '''
    Lists out all columns in CSV file
    :param csvfile: Name of CSV file
    :return: returns a list with the names of each of the columns in the CSV file
    '''
    csvboolean = False
    # Checks if CSV file is valid
    while (csvboolean == False):
        # Checks if CSV file extension is correct
        if csvfile[len(csvfile) - 4:] != '.csv':
            csvfile = input("This is not a valid CSV filename. Please name one ending with '.csv': ")
        # Checks if CSV file is valid
        else:
            try:
                open(csvfile)
                csvboolean = True
            except:
                csvfile = input("File cannot be found. Please name one ending with '.csv' and is in local folder. ")
    # Saves CSV file as Pandas data frame
    df = pd.read_csv(csvfile)
    # List of Column Names
    column_names = list(df.columns)
    print("Column Names List: ", (column_names))

def DropAColumnCSV(csvfile, column):
    '''
    Drops specified column from CSV file
    :param csvfile: Name of CSV file to drop column from
    :param column: Column Name
    :return: Prints out which column has dropped and gives summary of CSV file
    '''
    csvboolean = False
    validcolumn = False
    # Read CSV file as data frame
    data = pd.read_csv(csvfile)
    # If no column input, exit function
    if len(column) == 0:
        return
    # Checks if column name is valid
    while(validcolumn == False):
        try:
            data.drop(column, inplace = True, axis = 1)
            validcolumn = True
        except:
            column = input("Please input valid column title: ")
            if len(column) == 0:
                return
    # Input New File Name for Deleted Column CSV file
    newfilename = input("Please type CSV filename you would like to save with CSV extension: ")
    # Checks if CSV filename is acceptable
    while(csvboolean == False):
        if newfilename[len(newfilename)-3:] != 'csv' or '/' in newfilename:
            newfilename = input("This is not a valid CSV filename. Please name it ending with '.csv' ")
        else:
            csvboolean = True
    # Saves Data as CSV format
    data.to_csv(newfilename, index = False)
    print("Final CSV File Summary: ")
    # Summary of CSV File post Column Drop
    SummaryFileCSV(newfilename)
    print(column + " has been dropped")


# Main

# Stores valid CSV file
csvfile = validCSV()
# List of Column Names in CSV File
AllColumnsCSV(csvfile)
# Initial CSV File Summary (rows + columns)
print("Initial CSV File Summary: ")
SummaryFileCSV(csvfile)
# Choosing which column to drop
column = input("Please type column you would like to drop. Leave blank and press enter if you would like to not remove a column: ")
DropAColumnCSV(csvfile, column)
# Converting CSV file to JSON file
csvfile = input("Please type CSV filename with CSV extension you would like to convert into JSON file: ")
jsonfile = input("Please type JSON filename with JSON extension you would like to convert original CSV file into:  ")
CSVtoJSON(csvfile, jsonfile)


























