import csv


#def main():
with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineCounter = 0
    totalAmount = 0
    oldAmount = 0
    newAmount = 0
    monthlyChange = 0
    averageChange = 0
    greatestIncrease = {
        "date": "",
        "amount": 0
    }
    greatestDecrease = {
        "date": "",
        "amount": 0
    }
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
            newAmount = int(row[1])

            #if newAmount != oldAmount :
            averageChange += monthlyChange
            monthlyChange = newAmount-oldAmount
            print(f'\t{averageChange} , :::: {monthlyChange}')
            if monthlyChange > greatestIncrease.get("amount"):
                greatestIncrease["date"] = row[0]
                greatestIncrease["amount"] = monthlyChange
                
            if monthlyChange < greatestDecrease.get("amount"):
                greatestDecrease["date"] = row[0]
                greatestDecrease["amount"] = monthlyChange

            oldAmount = int(row[1])

     # display(lineCounter)
    print(f'Financial Analysis')
    print(f'------------------')
    print(f'Total Months: {lineCounter-1}')
    print(f'Total:\t ${totalAmount}')
    #print(f'Average Change: ${averageChange/(lineCounter-2)}')
    print(f'Greatest Increase in Profits: ${greatestIncrease["date"]} (${greatestIncrease["amount"]})')
    print(f'Greatest Decrease in Profits: ${greatestDecrease["date"]} (${greatestDecrease["amount"]})')
    print(f'Processed {lineCounter} rows.')

# def display(lineCounter):
#     print(f'Financial Analysis')
#     print(f'Total Months: {lineCounter-1}')
#     print(f'Processed {lineCounter} months.')
