import csv
import os

vote_csv = os.path.join("Resources","test.csv")
# Declare global variables
voteDict = {}
voteCounter = 0
founde = 0
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

        # Increment the vote counter
        voteCounter += 1
        # Check if candidate exist
        if row[2] in voteDict :
            voteDict[row[2]] += 1
        # If not exist create a new record
        else:
            voteDict[row[2]] = 1
    print (voteCounter)
    print (voteDict)
    voteCandidates = voteDict.keys()
    voteCounts = voteDict.values()
    print (f'keys {voteCandidates}')
    print (f'values {voteCounts}')
    votePercentage = []
    for val in voteCounts:
        votePercentage.append(round((val/voteCounter)*100,3))
    print(f'Percentage {votePercentage}')

    


