import csv

# Load the file paths 
input_file = "PyPoll\Resources\election_data.csv"
output_file = "PyPoll\Resources\election_data_output.txt"

# Create a count for the total votes
total_votes = 0

# Candidate list and candidate votes 
candidate_list = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker 
name = ""
winning_votes = 0 

# Convert csv into a list of dictionaries
with open(input_file) as election_data: 
    reader = csv.DictReader(election_data)

    # Create a loop to go through each row into the reader
    for row in reader:

        # Total votes will add by one in each row
        total_votes = total_votes + 1

        # Look if the name is in the name column 
        name = row["Candidate"]
            
        # If statement
        if name not in candidate_list: 
            candidate_list.append(name)
            candidate_votes[name] = 0 
        # Then...
        candidate_votes[name] = candidate_votes[name] + 1
    
# Convert results into a text file and then print the results
with open (output_file, "w") as txt_file:

    # Print the total vote count 
    results = (
        f"\n\nResults\n"
        f"\n"
        f"Total Votes: {total_votes}\n"
        f"\n"
    )
    print(results)

    # Convert the total vote results into a text file 
    txt_file.write(results)

    # Loop through the candidate votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentage = float(votes) / float(total_votes) * 100 
        
        if (votes > winning_votes):
            winning_votes = votes 
            name = candidate
        
        voter_count = f"{candidate}: {percentage:.3f}% ({votes})\n"
        print(voter_count)
        
        txt_file.write(voter_count)

    final_results = (
        f"\n"
        f"Winner: {name}\n"
        f"\n"
    )
    print(final_results)

    txt_file.write(final_results)