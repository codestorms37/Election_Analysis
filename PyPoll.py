# Dependencies
import csv
import os

# dir() : will return all the functions available in the csv module.
#print(dir(csv))

# 1. Open the data file.
## Assign a variable for the file to load and the path.
file_to_load_path = os.path.join("Resources", "election_results.csv")

# print(f"""
# file_to_load_path:
# {file_to_load_path}
# """)

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate options array
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load_path, newline="") as election_data_pointer:

    # Print the file object.
    # print(f"""
    # election_data_pointer:
    # {election_data_pointer}
    # """)

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data_pointer)

    # Print the header row.
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # print(row)

        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    # 3. Print the total votes.
    print(total_votes)

    # Print the candidate list.
    print(candidate_options)

    # Print the candidate vote dictionary.
    print(candidate_votes)


# RESULT

# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received

# 4. Percentage of votes each candidate won
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
candidate_results = ""

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {round(vote_percentage,2)}% of the vote.")
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results = (f"{candidate_results}"
    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name


# 5. The winner of the election based on popular vote
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
# print(winning_candidate_summary)

# Create a filename variable to a direct or indirect path to the file.
file_to_save_path = os.path.join("analysis", "election_analysis.txt")

# print(f"""
#     file_to_save_path:
#     {file_to_save_path}
#     """)

# Using the with statement open the file as a text file.
with open(file_to_save_path, "w", newline="" ) as txt_file_pointer:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file_pointer.write(election_results)

    # Print each candidate, their voter count, and percentage to the terminal.
    print(candidate_results)
    #  Save the candidate results to our text file.
    txt_file_pointer.write(candidate_results)

    # Save the winning candidate's name to the text file.
    txt_file_pointer.write(winning_candidate_summary)
