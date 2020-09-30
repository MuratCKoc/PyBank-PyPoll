import csv


#def main():
with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineCounter = 0
    totalAmount = 0
    asd = 0
    for row in csv_reader:
        if lineCounter == 0:
            print(f'Column names are {", ".join(row)}')
            lineCounter += 1
        else:
            print(f'\t{row[0]} --- {row[1]}')
            lineCounter += 1

        # TotalAmount    
        if row[1] != "Profit/Losses":
            totalAmount += int(row[1])
            print(f'Total:\t ${totalAmount}')

     # display(lineCounter)
    print(f'Financial Analysis')
    print(f'------------------')
    print(f'Total Months: {lineCounter-1}')
    print(f'Total:\t ${totalAmount}')
    print(f'Processed {lineCounter} rows.')

# def display(lineCounter):
#     print(f'Financial Analysis')
#     print(f'Total Months: {lineCounter-1}')
#     print(f'Processed {lineCounter} months.')
