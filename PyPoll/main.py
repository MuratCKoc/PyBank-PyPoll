import csv
import os

vote_csv = os.path.join("Resources","test.csv")
# Declare global variables
voteDict = {}
voteCounter = 0
# Function to create new record
# Function to increment vote count
# Display and write to a file
# Percentage calculator function

# Main Loop
# Read file
with open(vote_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    # Skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        print (row)

    # Check if candidate exist
    # If not exist create a new record
    # If candidate exists then increment the vote count


