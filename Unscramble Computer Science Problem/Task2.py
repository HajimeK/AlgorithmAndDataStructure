"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import os
from collections import defaultdict

cwd = os.path.dirname(__file__)

with open(cwd + '/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(cwd + '/calls.csv', 'r') as f:
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

numberTotal = defaultdict(int)
maxValue = 0
maxidx = -1

# Go through the calls
for callFrom, callTo, date, duration in calls:
    numberTotal[callFrom] += int(duration)
    numberTotal[callTo] += int(duration)

max_kv = max(numberTotal.items(), key=lambda x: x[1])
# print the result
print(f'{max_kv[0]} spent the longest time, {max_kv[1]} seconds, on the phone during September 2016.')