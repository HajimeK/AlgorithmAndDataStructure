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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
d = []

for text in texts:
    if not(text[0] in d):
        d.append(text[0])
    if not(text[1] in d):
        d.append(text[1])

for call in calls:
    if not(call[0] in d):
        d.append(call[0])
    if not(call[1] in d):
        d.append(call[1])

print(f'There are {len(d)} different telephone numbers in the records.')