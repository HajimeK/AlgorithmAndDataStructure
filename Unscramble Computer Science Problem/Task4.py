"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os

cwd = os.path.dirname(__file__)

with open(cwd + '/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(cwd + '/calls.csv', 'r') as f:
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

numbersInTexts = set()
for line in texts:
    numbersInTexts.add(line[0])
    numbersInTexts.add(line[1])

callers = set()
receivers = set()
for caller, receiver, _ , _ in calls:
    callers.add(caller)
    receivers.add(receiver)

suspects = sorted(callers - (receivers | numbersInTexts))
print("These numbers could be telemarketers: ")
print(*suspects, sep='\n')