import csv
import os
import operator

vote_csv = os.path.join("Resources","test.csv")
# Declare global variables
voteDict = {}
totalVotes = 0


# Display and write to a file
# Percentage calculator function

# Sort the dictionary
def sortDict(e):
    return 

def byVoteCount(elem):
    return elem[1]

def printResults(l):
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")
    for iter in l:
        print(f"{iter[0]}: {iter[2]}% ({iter[1]})")
    print("-------------------------")
    print(f'Winner: {l[0][0]}')
    print("-------------------------")

def exportReport(fileName):
    with open(fileName,"w") as fileX:
        fileX = open(fileName,"w+")

        fileX.write("Election Results\n")
        fileX.write("-------------------------\n")
        fileX.write(f"Total Votes: {totalVotes}\n")
        fileX.write("-------------------------\n")
        for iter in l:
            fileX.write(f"{iter[0]}: {iter[2]}% ({iter[1]})\n")
        fileX.write("-------------------------\n")
        fileX.write(f'Winner: {l[0][0]}\n')
        fileX.write("-------------------------")

# Main Loop
# Read file
with open(vote_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    # Skip the header row
    header = next(csvreader)
    
    for row in csvreader:
        print (row)

        # Increment the vote counter
        totalVotes += 1
        # Check if candidate exist
        if row[2] in voteDict :
            voteDict[row[2]] += 1
        # If not exist create a new record
        else:
            voteDict[row[2]] = 1
    print (totalVotes)
    print (voteDict)

    # Sort the dictionary by voteCount 
    
    # Calculate Percentage 
    voteCandidates = voteDict.keys()
    voteCounts = voteDict.values()
    votePercentage = []
    for val in voteCounts:
        votePercentage.append(round((val/totalVotes)*100,3))
    print(f'Percentage {votePercentage}')

    # Zip list of values and sort them by number of votes
    l = list(zip(voteCandidates,voteCounts,votePercentage))
    l.sort(key=byVoteCount,reverse=True)
    print (f'list: -- {l}')

    #new_dict = {k: dict(zip(voteCandidates,v)) for k, v in zip(voteCandidates, zip(voteCounts,votePercentage))}
    #print (new_dict)
    # sorted_dict = sorted(new_dict.items(), key=lambda kv: kv[1], reverse=True)
    # Destructure dictionary
    printResults(l)
    exportReport("test.txt")
    print(f'keys {voteCandidates}')
    print(f'values {voteCounts}')
    #print (x)
