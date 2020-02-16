# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total_spam_confidence = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    spam_confidence = float((line[line.find(': ')+2:len(line)]).rstrip())
    total_spam_confidence = total_spam_confidence + spam_confidence
print("Average spam confidence:", total_spam_confidence / count )