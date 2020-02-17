fname = input('Enter file name: ')

# if no input set default file name
if len(fname) < 1 : fname = "mbox-short.txt"

# open file
fhandle = open(fname)

# initialise a dictionary that is supposed to hold senders and number of emails received
hours_dict = {}

# read file line by line and add build up senders dict
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        time = line.split()[5]
        hour = time.split(':')[0]
        # build the histogram uisng dict get function
        hours_dict[hour] = hours_dict.get(hour, 0) + 1    

hours_list = sorted([(hour, count) for hour, count in hours_dict.items()])    

for hour, count in hours_list:
    print(hour, count)
