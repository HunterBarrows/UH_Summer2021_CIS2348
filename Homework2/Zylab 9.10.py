# Hunter Barrows 1550107

# Zylab 9.10

import csv

input_value = input()

# open and read input files
with open(input_value, 'r') as words:
    words1 = csv.reader(words)

# Assigns each word to a row
    for row in words1:
        words2 = row

# Counts the number of times word appears and prevents duplicates
duplicates = list(dict.fromkeys(words2))
dup_list = len(duplicates)
for i in range(dup_list):
    print(duplicates[i], words2.count(duplicates[i]))
