__author__ = 'seven'
import sys
from replaceExpand import *

if __name__ == '__main__':
    dict = {}
    inFile = open('../../MPQALexicon/MPQALexicon/subjclueslen1-HLTEMNLP05.tff', 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t').split(' ')
        type = line[0][5:]
        word = line[2][6:]
        polarity = line[5][14:]
        score = 1
        if type == 'strongsubj':
            score = 2
        if polarity == 'negative':
            score *= -1
        dict[word] = score

    # exit(0)

    index = 0
    poscrc = 0
    negcrc = 0
    poscount = 0
    negcount = 0
    pospre = 0
    negpre = 0
    count = 0
    f = open('../dataset/final_test-gold-B_Input.txt', 'r')
    for line in f:
        if line:
            index += 1
            # print line
            line = line.strip('\n').split('\t')
            tweet = line[1].split()
            # token = i[2].split()
            label = line[3].strip()
            if tweet and not label == 'neutral':
                posscore = 0
                negscore = 0
                count += 1
                # tweet, token, count1, count2 = preprocesingTweet1(tweet, token, emoticonsDict, acronymDict)
                # tweet = [i.strip(specialChar).lower() for i in tweet]
                tweet = [i for i in tweet if i]
                #unigram score

                for i in range(len(tweet)):
                    phrase = tweet[i]
                    phrase = phrase.lower()
                    if phrase in dict:
                        score = dict[phrase]
                        if score > 0:
                            posscore += score
                        if score < 0:
                            negscore += score

                total = posscore+negscore
                print "Index: %d, Positive Score: %f, Negtive Score: %f, Total Score: %f, Label: %s" % (
                    index, posscore, negscore, total, label)

                if label == 'positive':
                    poscount += 1
                elif label == 'negative':
                    negcount += 1

                if total > 0:
                    pospre += 1
                    if label == 'positive':
                        poscrc += 1
                elif total < 0:
                    negpre += 1
                    if label == 'negative':
                        negcrc += 1
    print poscrc, pospre, poscount
    print "Positive, Precision: %f, Recall: %f, " % ( float(poscrc)/pospre, float(poscrc)/poscount )
    print negcrc, negpre, negcount
    print "Negative, Precision: %f, Recall: %f, " % ( float(negcrc)/negpre, float(negcrc)/negcount )
    f.close()