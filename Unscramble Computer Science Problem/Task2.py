"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

total = []
number = []
maxValue = 0
maxidx = -1

# Go through the calls
for call in calls:
    idx = 0
    # If caller exist in the list number[] with the index idx
    # update the total[idx] += seconds for the caller
    try :
        #    if idx > 0:
        #        currvalue = total[idx]
        # if the receiver exists in the list number[] with the index idx
        # update the total[idx] += seconds for the receiver
        idx = number.index(call[0])
        currTotal = total[idx]
        total[idx] = currTotal + int(call[3])
    except:
        # Add if the number is not in the number[] list
        # add the seconds to the total[]
        # confirm they have the same index, and the list length is also the same.
        number.append(call[0])
        total.append(int(call[3]))
        assert(len(number) == len(total))
        idx = len(number) - 1
    # if the maxvalue is smaller than total[idx]
    # update maxvalue with total[idx]
    # update maxidx with idx
    if total[idx] > maxValue:
        maxValue = total[idx]
        maxidx = idx

# print the result
print(f'{number[maxidx]} spent the longest time, {maxValue} seconds, on the phone during September 2016.')