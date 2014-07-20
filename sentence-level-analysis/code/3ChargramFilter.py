__author__ = 'seven'
__author__ = 'seven'
import sys
from replaceExpand import *
from collections import defaultdict

if __name__ == '__main__':

    """create emoticons dictionary"""
    f = open("emoticonsWithPolarity.txt", 'r')
    data = f.read().split('\n')
    emoticonsDict = {}
    for i in data:
        if i:
            i = i.split()
            value = i[-1]
            key = i[:-1]
            for j in key:
                emoticonsDict[j] = value
    f.close()

    #print emoticonsDict

    """create acronym dictionary"""
    f = open("acronym_tokenised.txt", 'r')
    data = f.read().split('\n')
    acronymDict = {}
    for i in data:
        if i:
            i = i.split('\t')
            word = i[0].split()
            token = i[1].split()[1:]
            key = word[0].lower().strip(specialChar)
            value = [j.lower().strip(specialChar) for j in word[1:]]
            acronymDict[key] = [value, token]
    f.close()

    #print acronymDict

    """create stopWords dictionary"""
    stopWords = defaultdict(int)
    f = open("stopWords.txt", "r")
    for line in f:
        if line:
            line = line.strip(specialChar).lower()
            stopWords[line] = 1
    f.close()

    f4CharDict = {}

    f = open(sys.argv[1], 'r')
    for line in f:
        if line:
            line = line.strip('\n').split('\t')
            tweet = line[1].split()
            token = line[2].split()
            label = line[3].strip()
            if tweet:
                # tweet, token, count1, count2 = preprocesingTweet1(tweet, token, emoticonsDict, acronymDict)
                # tweet, token, count3 = preprocesingTweet2(tweet, token, stopWords)
                tweet = [i.strip(specialChar).lower() for i in tweet]
                tweet = [i for i in tweet if i]
                for word in tweet:
                    if len(word) > 3:
                        for i in xrange(len(word)-2):
                            seq = word[i:i+3]
                            if seq not in f4CharDict:
                                f4CharDict[seq] = [0, 0, 0]
                            f4CharDict[seq][eval(label)] += 1
                    # exit(0)

    f.close()
    triModel = []
    for i in f4CharDict.keys():
        count = reduce(lambda x, y: x + y, f4CharDict[i])
        if count >= 10:
            count *= 1.0
            pos = f4CharDict[i][positive] / count
            neg = f4CharDict[i][negative] / count
            neu = f4CharDict[i][neutral] / count
            if pos > 0.9 or neg > 0.9 or neu > 0.9:
            # if pos > 0.8 or neg > 0.8 or neu > 0.8:
            # if pos > 0.7 or neg > 0.7 or neu > 0.7:
                l = [i, pos, neg, neu, count]
                triModel.append(l)

    triModel = sorted(triModel, key=lambda x: x[4], reverse=True)
    outfile = open("f3Chargram1.txt", 'w')
    # outfile = open("f3Chargram_debate08.txt", 'w')
    # outfile = open("f3Chargram_Apoorv.txt", 'w')
    for i in xrange(len(triModel)):
        if i > 0:
            outfile.write('\n')
        outfile.write(triModel[i][0])
