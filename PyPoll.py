# Dependencies.
from _typeshed import OpenTextMode
import csv
import os

# dir() : will return all the functions available in the csv module.
#print(dir(csv))

# 1. Open the data file.
## Assign a variable for the file to load and the path.
file_to_load_path = os.path.join("Resources", "election_results.csv")


print(f"""
file_to_load_path:
{file_to_load_path}
""")

# Open the election results and read the file.
with open(file_to_load_path, newline="") as election_data_pointer:

    # Print the file object.
    print(f"""
    election_data_pointer:
    {election_data_pointer}
    """)

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data_pointer)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
        # print(row)

# Create a filename variable to a direct or indirect path to the file.
file_to_save_path = os.path.join("analysis", "election_analysis.txt")

print(f"""
    file_to_save_path:
    {file_to_save_path}
    """)

# Using the with statement open the file as a text file.
with open(file_to_save_path, OpenTextMode="w",newline="" ) as txt_file_pointer:

    

# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.


# RESULT

# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
