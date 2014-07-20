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

    triDict = {}

    f = open(sys.argv[1], 'r')
    for i in f:
        if i:
            i = i.split('\t')
            tweet = i[1].split()
            token = i[2].split()
            label = i[3].strip()
            if tweet:
                # tweet, token, count1, count2 = preprocesingTweet1(tweet, token, emoticonsDict, acronymDict)
                # tweet, token, count3 = preprocesingTweet2(tweet, token, stopWords)
                tweet = [i.strip(specialChar).lower() for i in tweet]
                tweet = [i for i in tweet if i]
                for i in range(len(tweet) - 3):
                    phrase = tweet[i] + ' ' + tweet[i + 1] + ' ' + tweet[i + 2] + ' ' + tweet[i+3]
                    if phrase not in triDict:
                        triDict[phrase] = [0, 0, 0]
                    triDict[phrase][eval(label)] += 1

                    phrase = tweet[i] + ' ' + '*' + ' ' + tweet[i + 2] + ' ' + tweet[i+3]
                    if phrase not in triDict:
                        triDict[phrase] = [0, 0, 0]
                    triDict[phrase][eval(label)] += 1

                    phrase = tweet[i] + ' ' + tweet[i + 1] + ' ' + '*' + ' ' + tweet[i+3]
                    if phrase not in triDict:
                        triDict[phrase] = [0, 0, 0]
                    triDict[phrase][eval(label)] += 1

    f.close()
    triModel = []
    for i in triDict.keys():
        count = reduce(lambda x, y: x + y, triDict[i])
        if count >= 10:
            count *= 1.0
            pos = triDict[i][positive] / count
            neg = triDict[i][negative] / count
            neu = triDict[i][neutral] / count
            if pos > 0.9 or neg > 0.9 or neu > 0.9:
            # if pos > 0.8 or neg > 0.8 or neu > 0.8:
            # if pos > 0.7 or neg > 0.7 or neu > 0.7:
                l = [i, pos, neg, neu, count]
                triModel.append(l)

    triModel = sorted(triModel, key=lambda x: x[4], reverse=True)
    outfile = open("f4gram1.txt", 'w')
    # outfile = open("f4gram_debate08.txt", 'w')
    # outfile = open("f4gram_Apoorv.txt", 'w')
    for i in xrange(len(triModel)):
        if i > 0:
            outfile.write('\n')
        outfile.write(triModel[i][0])
