# Using any programming language, read an innate file and parse the strings to count how many times an email 
# address is found

import re

def count_email(filename):
    count = 0
    # [\w\.-]+ w-alphanumeric char and . and -, and plus indicate it should be more than 1 char
    regex = r"[\w\.-]+@[\w\.-]+\.[\w]{2,4}"
    with open(filename, 'r') as f:
        for line in f:
            count += len(re.findall(regex, line))
    return count
# Eliminate email addresses from the given HTML file.
# Filter logs with some python script and create a structure for it
# I was asked to obfuscate local parts of email addresses found in all HTML files under a folder (also subfolders).
# RegEx: Eliminate email addresses from the given HTML file.
# Using any programming language, read an innate file and parse the strings to count how many times an email address is found
# How would you design a system that manipulates content sent from a client (e.g. clean bad words in a comment post)?

# Write a function to sort a list of integers that looks like this [5,2,0,3,0,1,6,0] -> [1,2,3,5,6,0,0,0] in the most efficient way.
# Battleship game: write a function that finds a ship and return its coordinates.
# Write a script that connects to 100 hosts, looks for a particular process and sends an email with a report.
# reimplement 'tail' in a scripting language
# Find top n words on some text?
# Send packets to remote machines and try to upgrade the packet remotely.
# Filter logs with some python script and create a structure for it
# Write some code that lists the top 10 most frequent words in a file. 
# Write some code that create a randomized minesweeper board on every iteration.
# Find a fast way to extract patterns from a 2d matrix

# import os
# folder_path='/home/sandip/Algorithm-and-Data-Structure/python/'
# for root, dirs, files in os.walk(folder_path):
#     # print(root)
#     # # for d in dirs:
#     # #     print(d)
#     for f in files:
#         print(f)

import re

# Regular expression pattern with capturing groups
email_pattern = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

# Example email string
email_string = 'user@example.com'

# Perform the match
match = re.search(email_pattern, email_string)

if match:
    print('Full match:', match.group(0))   # 'user@example.com'
    print('Local part:', match.group(1))   # 'user'
    print('Domain part:', match.group(2))  # 'example.com'
