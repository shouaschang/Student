# Assignment 3
# Cohort 4
# main.py document for PyPoll analysis

# Resources: election_data.csv
# Data columns: Voter ID[0], County[1], Candidate[2]

# INSTRUCTIONS
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#   Importing dependencies for CSV file
import os
import csv

#   Loading CSV file
csvpath = os.path.join(".", 'Resources', 'election_data.csv')

#   Opening and reading the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #print(csvreader)
    
#   Variables needed for the tasks
    total_votes = 0
    winner = 0
    index = 0

#   Lists needed for the tasks: a list for candidate names, a list for number of votes a candidate received,
#   and a list for the percentage of votes a candidate received
    candidates_list = [] 
    candidate_votes = []
    candidate_percent = []
    
#   Create index for rows
#   index = []

#   Using Sniffer to read header and exclude from analysis.
    if csv.Sniffer().has_header:
        next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #for row in csvreader:
        #print(row)
        
#   Analysis
    for row in csvreader:
        #1.     The total number of votes casted
        total_votes += 1
        
        #2.     A complete list of candidates who received votes. Only append unique values/names
        #       and their votes.
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            index = candidates_list.index(row[2])
            candidate_votes.append(1)
            #print(candidates_list)
        else: #Count the number of votes received for each unique candidate
            index = candidates_list.index(row[2])
            candidate_votes[index] += 1
             
    for row[1] in candidate_votes:
         #3. The percetange of votes each candidate won.
         percent = (row[1] / total_votes) * 100
         percent = round(percent, 3)
         candidate_percent.append(percent)
         
    #4.     Winner result
    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    popular_votes_winner = candidates_list[index]
        
#   Printing outcome
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------") 
#   Iterate through the list to print out details for each candidate.
for i in range(len(candidates_list)):
   print(f"{str(candidates_list[i])}: {str(candidate_percent[i])} {str(candidate_votes[i])}")
print("---------------------------------------")
print(f"Winner {popular_votes_winner}")
    
    
#   Export to PyPoll_output.txt file
file = open('PyPoll_output.txt', 'w')
message1 = "Election Results"
message2 = "-----------------------------"
message3 = str(f"Total Votes: {total_votes}")
message4 = "-----------------------------"
#   Iterate through the list to print out details for each candidate.
file.write('{}\n')
for i in range(len(candidates_list)):
   str(f"{str(candidates_list[i])}: {str(candidate_percent[i])} {str(candidate_votes[i])}")
message5 = "---------------------------------------"
message6 = str(f"Winner {popular_votes_winner}")