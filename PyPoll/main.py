import csv

# File paths
input_file = 'Resources/election_data.csv'
output_file = 'analysis.txt'

# Initializing variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the input file
with open(input_file, 'r') as file:
    csvreader = csv.DictReader(file)

    # Storing the header row
    header = csvreader.fieldnames
    
    # Loop through each row of the input file
    for row in csvreader:
        # Increase total months by 1 each loop
        total_votes += 1

        # Count the votes for each candidate
        candidate = row["Candidate"]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won and figure out the winner
results = []
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Formatting results to output to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Exporting the resultes to a text file
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, percentage, votes in results:
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")