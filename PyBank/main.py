# jeff simonson, 5/4/19 python homework

# If I had more time I realize that I would need to do a better job of setting up the key-value dictionaries
# to iterate and update the vote counts based on the candidate key search, get the vote count associated with that key and add to the vote.
# Once I got that then the rest would be relatively easy and I could loop through the dictionary to calculate the percentages of total vote,
# find a max and declare the winner. Oh well... Pandas will likely solve this for me. :)

#project objectives
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#--------------------------------------------------

# modules
import os
import csv

#declare and set variables equal to 0
vote_counter = 0
total_votes = 0


#name of cvs file
myfile = "election_data.csv"
#provide path (i was having legit trouble with resource so I had to hard code it, but it works!)
csvpath = os.path.join('C:\\dumbass_sandbox',myfile)

with open(csvpath, newline="") as csvfile:
    #initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=",")

    #acknowledge headers in first row, skip them
    file_header = next(csvreader)

    #loop rows
    for r in csvreader:

        if vote_counter == 0:
            # add candidate & votes to dictionary
            c_name = r[2]
            votes_by_candidate = {'c_name': c_name, 'c_votes': 1}
        else:
            # does candidate already exist?                 
            for c_name, c_votes in votes_by_candidate.items():
                #candidate exists
                if c_name == r[2]:
                    # update the candidate-vote tally pair
                    add_to_old_votes = votes_by_candidate['c_votes'].values() + 1
                    votes_by_candidate = {'c_name': c_name, 'c_votes': add_to_old_votes}
                else:
                    # add a new name to the dictionary votes = 1
                    votes_by_candidate = {'c_name': r[2], 'c_votes': 1}

        #count all votes
        vote_counter += 1

#out of the loop, verify values from above

#count votes but subtract 1 for headers
total_votes = vote_counter -1
print(total_votes)

#print out vote tallies by candidate


       
