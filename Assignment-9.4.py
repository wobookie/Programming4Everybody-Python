fname = input('Enter file name: ')

# if no input set default file name
if len(fname) < 1 : fname = "mbox-short.txt"

# open file
fhandle = open(fname)

# initialise a dictionary that is supposed to hold senders and number of emails received
senders = {}

# read file line by line and add build up senders dict
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        sender = line.split()[1]
        # build the histogram uisng dict get function
        senders[sender] = senders.get(sender, 0) + 1    

max_count = None

for sender, count in senders.items():
    if (max_count is None) or (count > max_count): 
        max_count = count
        max_sender = sender
    
print(max_sender, max_count)
