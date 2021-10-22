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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
textLine = texts[0]
callLine = calls[-1]
print(f'First record of texts, \"{textLine[0]}\" texts \"{textLine[1]}\" at time \"{textLine[2]}\"')
print(f'Last record of calls, \"{callLine[0]}\" calls \"{callLine[1]}\" at time \"{callLine[2]}\", lasting \"{callLine[3]}\" seconds')
