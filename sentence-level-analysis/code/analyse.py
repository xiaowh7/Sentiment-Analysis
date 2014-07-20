__author__ = 'seven'
goldFile = open("../dataset/test-gold-B.csv", 'r')
gold = []
for line in goldFile.readlines():
    gold.append(line.strip('\r\n').split('\t'))

predfile = open("./ans.txt", 'r')
pred = []
for line in predfile.readlines():
    pred.append(line.strip('\r\n').split('\t'))

cnt = 0
for i in range(len(gold)):
    goldSentiment = gold[i][2]
    predSentiment = pred[i][2]
    if not goldSentiment == predSentiment:
        cnt += 1
        print "\nid: %d\n%s -> %s" % (i,goldSentiment, predSentiment)
        print gold[i][3]

print cnt