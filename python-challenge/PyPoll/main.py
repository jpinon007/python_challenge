# Import necessary modules
import os
import csv

# Create path for CSV file

election_data_csv = r"C:\Users\jasmi\OneDrive\Documents\python-challenge\PyPoll\Resources\election_data.csv.csv"

# Initialize variables to store election data
election_data = 0
ballots = 0
list_of_candiates = 0
total_candidates = 0
candidates = 0
total_votes = 0
percentage_votes_won = 0
vote_percentage = 0

# Open and read the CSV file

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip header row and count the total number of votes recorded

    next(csvreader)
    election_data = list(csvreader)
    row_count = len(election_data)

# Create a list of candidates who obtained votes

    list_of_candidates = list()
    ballots = list()
    for i in range (0,row_count):
        candidates = election_data[i][2]
        ballots.append(candidates)
        if candidates not in list_of_candidates: 
            list_of_candidates.append(candidates)
    total_candidates = len(list_of_candidates)

# Ballot total and percentage that candidates gained 

    total_votes = list()
    percentage_votes_won = list()
    for v in range (0,total_candidates):
        name = list_of_candidates[v]
        total_votes.append(ballots.count(name))
        vote_percentage = total_votes[v]/row_count
        percentage_votes_won.append(vote_percentage)

# Winner by popular vote

    winner = total_votes.index(max(total_votes))    

# Print data results in terminal

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,total_candidates): 
        print(f"{list_of_candidates[k]}: {percentage_votes_won[k]:.3%} ({total_votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {list_of_candidates[winner]}")
    print("----------------------------")

# Create variable for "results.txt" file

    results_txt = r"C:\Users\jasmi\OneDrive\Documents\python-challenge\PyPoll\analysis\results.txt"

#Print data results in terminal  

    print("Election Results", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))
    print(f"Total Votes: {row_count:,}", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))
    for t in range (0,total_candidates): 
        print(f"{list_of_candidates[t]}: {percentage_votes_won[t]:.3%} ({total_votes[t]:,})", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))
    print(f"Winner: {list_of_candidates[winner]}", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))
    
