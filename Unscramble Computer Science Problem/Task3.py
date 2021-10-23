"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os
import re

cwd = os.path.dirname(__file__)

with open(cwd + '/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(cwd + '/calls.csv', 'r') as f:
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

# Part A: Find all of the area codes and mobile prefixes called by people
# in Bangalore. In other words, the calls were initiated by "(080)" area code
# to the following area codes and mobile prefixes:

def getPattern(phone, pattern):
  mo = pattern.match(phone)
  if mo:
    return mo.group()
  else:
    return None

calledByBangalore = []
bangaloreCallCount = 0
fixedLineCount = 0
# Bangalore number
patternBangalore = re.compile(r'\(080\)')
#  - Fixed lines start with an area code enclosed in brackets. The area
#    codes vary in length but always begin with 0.
patternFixedLine = re.compile(r'\(0\d{1,}\)')
#  - Mobile numbers have no parentheses, but have a space in the middle
#    of the number to help readability. The prefix of a mobile number
#    is its first four digits, and they always start with 7, 8 or 9.
patternMobile = re.compile(r'[7,8,9]\d{1,} {,1}')
#  - Telemarketers' numbers have no parentheses or space, but they start
#    with the area code 140.
patternTeleMarketer = re.compile(r'140')


for call in calls:
  # called from bangalore? if true it starts with (080)
  mo = getPattern(call[0], patternBangalore)
  if mo:
    bangaloreCallCount += 1

    mobile = getPattern(call[1], patternMobile)
    fixed = getPattern(call[1],patternFixedLine)
    marketer = getPattern(call[1],patternTeleMarketer)

    if mobile:
        calledByBangalore.append(mobile[:-2])
    elif fixed:
      fixedLineCount += 1
      calledByBangalore.append(fixed)
    elif marketer:
      calledByBangalore.append(marketer)
    else:
      print("other pattern")

# print out the result of Part A
print("The numbers called by people in Bangalore have codes:")
print(*sorted(set(calledByBangalore)), sep='\n')

# Part B: What percentage of calls from fixed lines in Bangalore are made
# to fixed lines also in Bangalore? In other words, of all the calls made
# from a number starting with "(080)", what percentage of these calls
# were made to a number also starting with "(080)"?

#Print the answer as a part of a message::
#The percentage should have 2 decimal digits
percentage = 0.0
if(bangaloreCallCount > 0):
  percentage = float(fixedLineCount) / bangaloreCallCount
print(f"{percentage:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
