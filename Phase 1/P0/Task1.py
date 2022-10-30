"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Worst case Big-O: 2n^2


numbers = []

for t in texts:
    if t[0] not in numbers:
        numbers.append(t[0])
    if t[1] not in numbers:
        numbers.append(t[1])

for c in calls:
    if c[0] not in numbers:
        numbers.append(c[0])
    if c[1] not in numbers:
        numbers.append(c[1])

print(f'There are {len(numbers)} different telephone numbers in the records.')
