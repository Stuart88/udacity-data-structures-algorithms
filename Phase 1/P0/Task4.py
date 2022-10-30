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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Worst case Big-O: n^2 + nlogn

possibleTelemarketers = []
hasSentText = False
hasReceivedCall = False

for c in calls:
    if c[0] in possibleTelemarketers:
        continue
    hasSentText = False
    hasReceivedCall = False
    for t in texts:
        # check if number has sent or received texts
        if c[0] == t[0] or c[0] == t[1]:
            hasSentText = True
            break

    if hasSentText == False:
        # if no texts, check if recieved calls
        for subC in calls:
            if c[0] == subC[1]:
                hasReceivedCall = True
                break
    if hasReceivedCall == False and hasSentText == False:
        possibleTelemarketers.append(c[0])

print('These numbers could be telemarketers: ')
possibleTelemarketers.sort()
for t in possibleTelemarketers:
    print(t)

