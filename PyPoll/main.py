import os
import csv

csvpath = os.path.join('..','..','Downloads','election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    candidates = []
    votes = []

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)

    print(candidates)
    print(votes)

    for i in range(len(votes)):
        for row in csvreader:
            if row[2] == candidates[i]:
                votes[i] = votes[i] + 1
        print(f"{candidates[i]} {votes[i]}")
    
       


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