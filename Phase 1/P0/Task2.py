"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Worst case Big-O: 5n



callsDict = {}

for c in calls:
    if c[0] not in callsDict:   #Add if does not exist
        callsDict[c[0]] = int(c[3])
    else:                       # else increment
        callsDict[c[0]] += int(c[3])

    if c[1] not in callsDict:   #Add if does not exist
        callsDict[c[1]] = int(c[3])
    else:                       # else increment
        callsDict[c[1]] += int(c[3])

key = next(iter(callsDict))

for d in callsDict:
    if callsDict[d] > callsDict[key]:
        key = d

print(f'{key} spent the longest time, {callsDict[key]} seconds, on the phone during September 2016.')
