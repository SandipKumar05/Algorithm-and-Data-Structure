# Using any programming language, read an innate file and parse the strings to count how many times an email address is found

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
