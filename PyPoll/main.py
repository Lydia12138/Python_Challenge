import os
import csv


election_data = os.path.join("election_data.csv")

# Set the empty list and variable
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline = "", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#The total number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1 
        '''
        Create a complete list of candidates who received votes
        If the candidate is not on our list, add his/her name to our list, along with a vote in his/her name. If he/she is already on our list, we will simply add a vote in his/her name 
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to the percentage of votes each candidate won
    for votes in num_votes:
        percentage = "{:.3%}".format(votes/total_votes)
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


# Write the content into the txt
print("Election Results", file=open("PyPoll.txt", "a"))
print("--------------------------",file=open("PyPoll.txt", "a"))
print(f"Total Votes: {str(total_votes)}",file=open("PyPoll.txt", "a"))
print("--------------------------",file=open("PyPoll.txt", "a"))
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})",file=open("PyPoll.txt", "a"))
print("--------------------------",file=open("PyPoll.txt", "a"))
print(f"Winner: {winning_candidate}",file=open("PyPoll.txt", "a"))
print("--------------------------",file=open("PyPoll.txt", "a"))