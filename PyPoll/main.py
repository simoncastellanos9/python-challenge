import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    candidates = []
    votes = []
    perVotes = []
    electionresults = []
    maxVotes = 0

    #Create unique list for candidates, and initial list for votes and percentage according to number of candidates
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)
            perVotes.append(0)
        electionresults.append(row[2])
    

    totalVotes = (int(len(electionresults)))

    #Print to terminal
    print("Election Results\n-------------------------")
    print(f"Total Votes: {totalVotes}\n-------------------------")

    for i in range(len(candidates)):
        for candidate in electionresults:
            if candidate == candidates[i]:
                votes[i] = votes[i] + 1       
        perVotes[i] = "{:.3%}".format(votes[i]/totalVotes)         
        print(f"{candidates[i]}: {perVotes[i]}  ({votes[i]})")
        if votes[i] > maxVotes:
            maxVotes = votes[i]
            winner = candidates[i]

    print(f"-------------------------\nWinner: {winner}\n-------------------------")


candidatesZip = zip(candidates,perVotes,votes)


output_path = os.path.join("analysis", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['Total Votes: ',totalVotes])
    for w in range(len(candidates)):
        csvwriter.writerows(candidatesZip)
    csvwriter.writerow(['Winner: ',winner])