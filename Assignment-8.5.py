fname = input('Enter file name: ')

# if no input set default file name
if len(fname) < 1 : fname = "mbox-short.txt"

# open file
fhandle = open(fname)
count = 0

# read file line by line
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        count += 1
        email = line.split()[1]
        print(email)

print("There were", count, "lines in the file with From as the first word")
