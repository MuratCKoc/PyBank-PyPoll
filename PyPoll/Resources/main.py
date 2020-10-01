import csv


#def main():
with open('election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineCounter = 0

    voters = {
        "Candidate": "",
        "County": "",
        "voteCount": 0
    }

    for row in csv_reader:
        if lineCounter == 0:
            print(f'Column names are {", ".join(row)}')
            lineCounter += 1
        else:
            print(f'\t{row[0]} --- {row[1]} --- {row[2]}')
            lineCounter += 1

        # TotalAmount    
        #if row[1] != "County":
            

            

    # display(lineCounter)
    print(f'Election Results')
    print(f'-----------------------')
    print(f'Total Votes: {lineCounter-1}')
    print(f'-----------------------')



# def display(lineCounter):
#     print(f'Financial Analysis')
#     print(f'Total Months: {lineCounter-1}')
#     print(f'Processed {lineCounter} months.')
