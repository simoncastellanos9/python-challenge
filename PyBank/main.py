import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    total = 0
    i = 0
    length = 0
    prevRow = 0
    change = 0
    changeCnt = 0
    greatInc = 0
    greatDec = 0

    for row in csvreader:
        total = total + int(row[1])
        length = length + 1
        if length>1:
            change = int(row[1])-prevRow
            if change > greatInc:
                greatInc = change
                greatIncMonth = row[0]
            if change < greatDec:
                greatDec = change
                greatDecMonth = row[0]
            changeCnt = changeCnt + change
        prevRow = int(row[1])
    aveChange = int(changeCnt/(length-1))    
    print("\nFinancial Analysis")
    print("----------------------------")
    print(f"Total Months: {length}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${aveChange}")
    print(f"Greatest Increase in Profits: {greatIncMonth} (${greatInc})")
    print(f"Greatest Decrease in Profits: {greatDecMonth} (${greatDec})")