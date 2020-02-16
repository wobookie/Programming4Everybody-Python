# Import required libraries
import re
import sys

# initialise variables
total = 0

#read filename as command line parameter, in case no paramater is provided use a default
try:
    fname = sys.argv[1]
except:
    fname = 'regex_sum_370201.txt'

# open the file
try:
    fhandler = open(fname)
except:
    print(f'Could not open file {fname} - please check whether it exists!')
    exit()

# read the file content and do the processing
for line in fhandler :
    line = line.rstrip()

    #find integer numbers in a single line
    numbers = re.findall('([0-9]+)', line)

    # in case no numbers in line - continue
    if len(numbers) == 0 :
        continue

    # maybe there are multiple numbers in one line. So we loop through the list
    for number in numbers:
        total = total + int(number)

print(total)