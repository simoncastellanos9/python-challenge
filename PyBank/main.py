import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

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

    #Calculate info from csv file
    for row in csvreader:
        total = total + int(row[1])
        #has to start counting change at second row
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
        #place holder to calculate difference
        prevRow = int(row[1])
    
    #Format to currency
    total = "${:.0f}".format(total)
    aveChange = "${:.2f}".format(int(changeCnt/(length-1)))
    greatInc = "${:.0f}".format(greatInc)
    greatDec = "${:.0f}".format(greatDec)

    #Print to terminal
    print("\nFinancial Analysis\n----------------------------")
    print(f"Total Months: {length}")
    print(f"Total: {total}")
    print(f"Average  Change: {aveChange}")
    print(f"Greatest Increase in Profits: {greatIncMonth} ({greatInc})")
    print(f"Greatest Decrease in Profits: {greatDecMonth} ({greatDec})")


index = ["Total Months","Total","Average Change", "Greatest Increase in Profits","Greatest Decrease in Profits"]
var = [length,total,aveChange,greatInc,greatDec]
mont = ["","","",greatIncMonth,greatDecMonth]

rows = zip(index, var, mont)

output_path = os.path.join("analysis", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis", "QTY", "Month"])

    #Write the second row
    for w in range(5):
        csvwriter.writerows(rows)
    
