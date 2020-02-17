fname = input('Enter file name: ')
fhandle = open(fname)
wordlist = []

for line in fhandle:
    line = line.rstrip()
    for word in line.split():
        if word not in wordlist:
            wordlist.append(word)

wordlist.sort()
print(wordlist)
