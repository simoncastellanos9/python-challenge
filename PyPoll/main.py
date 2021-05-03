import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    votes = 0

    for row in csvreader:
        votes = votes+1
        if row[2] == 'Khan':
            khan = khan + 1
        elif row [2] == 'Correy':
            correy = correy + 1
        elif row[2] == 'Li':
            li = li + 1
        elif row[2 == "O'Tooley"]:
            otooley = otooley + 1
    
    khanper = round((khan/votes)*100,3)
    correyper = round((correy/votes)*100,3)
    liper = round((li/votes)*100,3)
    otooleyper = round((otooley/votes)*100,3)
    

    print("Election Results\n-------------------------")
    print(f"Total Votes: {votes}")
    print("-------------------------")
    print(f"Khan: {khanper}% ({khan})")
    print(f"Correy: {correyper}% ({correy})")
    print(f"Li: {liper}% ({li})")
    print(f"O'Tooley: {otooleyper}% ({otooley})")

#output_path = os.path.join("analysis", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(["Financial Analysis"])

    #Write the second row

    #for w in range(5):
        #csvwriter.writerows(rows)
    
