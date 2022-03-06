# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popluar vote.

# Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis
    print(election_data)

# close the file.
election_data.close()

from distutils import text_file
import os
import csv
 
# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# open the election results and read the file.
with open(file_to_load) as election_data:
    print(election_data)

# create a filename variable to a directd or indirectd path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")

# create a filename variable to direct or indeirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some date to the file.
outfile.write("Hello World")

# close the filie
outfile.close()

# write three counties to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # read and print the header row.
    headers = next(file_reader)
    print(headers)
    



