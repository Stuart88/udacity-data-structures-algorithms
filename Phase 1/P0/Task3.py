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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Worst case Big-O: 10n + nlogn


def isBangaloreNumber(num):
    return num.startswith('(080)')

def getAreaCodeOrPrefix(num):
    if num[0] == '(':
        # landline
        return getAreaCode(num)
    elif num.startswith('140'):
        # telemarketer
        return '140'
    else:
        # mobile
        return getMobilePrefix(num)

def getAreaCode(num):
    code = ''
    for c in num:
        code += c
        if c == ')':
            break
    return code

def getMobilePrefix(num):
    prefix = ''
    for i in range(4):
        prefix += num[i]
    return prefix

calledNums = []
outgoingBangaloreNumsCount = 0;
calledBangaloreNumsCount = 0;
for c in calls:
    if isBangaloreNumber(c[0]):
        outgoingBangaloreNumsCount+=1
        numCode = getAreaCodeOrPrefix(c[1])
        if isBangaloreNumber(numCode):
            calledBangaloreNumsCount+=1
        if numCode not in calledNums:
            calledNums.append(numCode)

calledNums.sort()

print('The numbers called by people in Bangalore have codes:')
for num in calledNums:
    print(num)

percentBangalore =  100.00 * calledBangaloreNumsCount / outgoingBangaloreNumsCount
formatPercent = "{:.2f}".format(percentBangalore)
print(f'{formatPercent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
