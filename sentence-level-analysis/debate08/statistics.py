__author__ = 'seven'
count = 0
poscnt = 0
negcnt = 0
neucnt = 0
inFile = open('test.csv', 'r')
for line in inFile.readlines():
    data = line.split('\t')
    count += 1
    sentiment = data[2]
    if sentiment == 'positive':
        poscnt += 1
    elif sentiment == 'neutral':
        neucnt += 1
    elif sentiment == 'negative':
        negcnt += 1

print poscnt, neucnt, negcnt, count