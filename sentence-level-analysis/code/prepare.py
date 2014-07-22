from replaceExpand import *
from collections import defaultdict
from getDependency import *

def loadDictionary():
    """create emoticons dictionary"""
    f = open("..//code//emoticonsWithPolarity.txt", 'r')
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
    f = open("..//code//acronym_tokenised.txt", 'r')
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
    f = open("..//code//stopWords.txt", "r")
    for line in f:
        if line:
            line = line.strip(specialChar).lower()
            stopWords[line] = 1
    f.close()

    return acronymDict, stopWords, emoticonsDict

def loadNgram():
    """create Unigram Model"""
    print "Creating Unigram Model......."
    uniModel = []
    f = open('..//code//unigram1.txt', 'r')
    # f = open('..//code//unigram_debate08.txt', 'r')
    # f = open('..//code//unigram_Apoorv.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            uniModel.append(line)
    uniModel = list(set(uniModel))
    uniModel.sort()

    print "Unigram Model Createdm total %s" % len(uniModel)

    print "Creating Bigram Model......."
    biModel = []
    f = open('..//code//bigram1.txt', 'r')
    # f = open('..//code//bigram_debate08.txt', 'r')
    # f = open('..//code//bigram_Apoorv.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            biModel.append(line)
    biModel = list(set(biModel))
    biModel.sort()
    print "Bigram Model Created, total %s" % len(biModel)

    print "Creating Trigram Model......."
    triModel = []
    f = open('..//code//trigram1.txt', 'r')
    # f = open('..//code//trigram_debate08.txt', 'r')
    # f = open('..//code//trigram_Apoorv.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            triModel.append(line)
    triModel = list(set(triModel))
    triModel.sort()
    print "Trigram Model Created, total %s" % len(triModel)

    print "Creating F4gram Model......."
    f4Model = []
    f = open('..//code//f4gram1.txt', 'r')
    # f = open('..//code//f4gram_debate08.txt', 'r')
    # f = open('..//code//f4gram_Apoorv.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            f4Model.append(line)
    f4Model = list(set(f4Model))
    f4Model.sort()
    print "F4gram Model Created, total %s" % len(f4Model)

    print "Creating 3 Characters gram Model......."
    Char3Model = []
    f = open('..//code//f3Chargram1.txt', 'r')
    # f = open('..//code//f3Chargram_debate08.txt', 'r')
    # f = open('..//code//f3Chargram_Apoorv.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            Char3Model.append(line)
    Char3Model = list(set(Char3Model))
    Char3Model.sort()
    print "3 Characters gram Model Created, total %s" % len(Char3Model)

    print "Creating 4 Characters gram Model......."
    Char4Model = []
    f = open('..//code//f4Chargram1.txt', 'r')
    # f = open('..//code//f4Chargram_debate08.txt', 'r')
    # f = open('..//code//f4Chargram_Apoorv.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            Char4Model.append(line)
    Char4Model = list(set(Char4Model))
    Char4Model.sort()
    print "4 Characters gram Model Created, total %s" % len(Char4Model)

    print "Creating 5 Characters gram Model......."
    Char5Model = []
    f = open('..//code//f5Chargram1.txt', 'r')
    # f = open('..//code//f5Chargram_debate08.txt', 'r')
    # f = open('..//code//f5Chargram_Apoorv.txt', 'r')
    for line in f:
        if line:
            line = line.strip('\r\t\n ')
            Char5Model.append(line)
    Char5Model = list(set(Char5Model))
    Char5Model.sort()
    print "5 Characters gram Model Created, total %s" % len(Char5Model)
    return uniModel, biModel, triModel, f4Model, Char3Model, Char4Model, Char5Model

def loanNRCLexicon():

    inFile = open(
        '../../NRC-Canada/NRC-Hashtag-Sentiment-Lexicon-v0.1/NRC-Hashtag-Sentiment-Lexicon-v0.1/unigrams-pmilexicon.txt',
        'r')
    unigram = {}
    for line in inFile.readlines():
        raw = line.split('\t')
        phrase = raw[0]
        score = float(raw[1])
        unigram[phrase] = score
    inFile.close()

    inFile = open(
        '../../NRC-Canada/NRC-Hashtag-Sentiment-Lexicon-v0.1/NRC-Hashtag-Sentiment-Lexicon-v0.1/bigrams-pmilexicon.txt',
        'r')
    bigram = {}
    for line in inFile.readlines():
        raw = line.split('\t')
        phrase = raw[0]
        score = float(raw[1])
        bigram[phrase] = score
    inFile.close()

    inFile = open(
        '../../NRC-Canada/NRC-Hashtag-Sentiment-Lexicon-v0.1/NRC-Hashtag-Sentiment-Lexicon-v0.1/pairs-pmilexicon.txt',
        'r')
    pairgram = {}
    for line in inFile.readlines():
        raw = line.split('\t')
        phrase = raw[0]
        score = float(raw[1])
        pairgram[phrase] = score
    inFile.close()

    return unigram, bigram, pairgram

def loadS140Lexicon():
    inFile = open(
        '../../NRC-Canada/Sentiment140-Lexicon-v0.1/Sentiment140-Lexicon-v0.1/unigrams-pmilexicon.txt',
        'r')
    unigram = {}
    for line in inFile.readlines():
        raw = line.split('\t')
        phrase = raw[0]
        score = float(raw[1])
        unigram[phrase] = score
    inFile.close()

    inFile = open(
        '../../NRC-Canada/Sentiment140-Lexicon-v0.1/Sentiment140-Lexicon-v0.1/bigrams-pmilexicon.txt',
        'r')
    bigram = {}
    for line in inFile.readlines():
        raw = line.split('\t')
        phrase = raw[0]
        score = float(raw[1])
        bigram[phrase] = score
    inFile.close()

    inFile = open(
        '../../NRC-Canada/Sentiment140-Lexicon-v0.1/Sentiment140-Lexicon-v0.1/pairs-pmilexicon.txt',
        'r')
    pairgram = {}
    for line in inFile.readlines():
        raw = line.split('\t')
        phrase = raw[0]
        score = float(raw[1])
        pairgram[phrase] = score
    inFile.close()

    return unigram, bigram, pairgram

def loadLiuBingLexicon():
    dict = {}
    inFile = open('../../LiuBingLexicon/positive-words.txt', 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = 1

    inFile = open('../../LiuBingLexicon/negative-words.txt', 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = -1

    return dict

def loadMPQALexicon():
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

    return dict

def loadNRCEmoticonLexicon():
    dict = {}
    inFile = open('../../NRC-Canada/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-v0.92/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt', 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t').split('\t')
        word = line[0]
        category = line[1]
        assoFlag = line[2]
        score = 1
        if assoFlag == '1':
            if category == 'anger' or category == 'fear' or category == 'sadness' \
                    or category == 'disgust' or category == 'negative':
                score = -1
            dict[word] = score

    return dict

def loadPosNegWords():
    dict = {}
    inFile = open('../dataset/pos_mod.txt', 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = 1

    inFile = open('../dataset/neg_mod.txt', 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t')
        dict[line] = -1

    return dict

def loadAFINNLexicon():
    dict = {}
    inFile = open('./AFINN-111.txt', 'r')
    for line in inFile.readlines():
        line = line.strip('\n\t').split('\t')
        dict[line[0]] = int(line[1])

    return dict

def loadSentenceDependency():
    # trainFile = "../Apoorv/Apoorv_dependency_train.txt"
    # trainFile = "../Apoorv/extended1_dependency_train.txt"
    # trainFile = "../Apoorv/extended2_dependency_train.txt"
    # trainFile = "../Apoorv/extendedAll_dependency_train.txt"
    # testFile = "../Apoorv/Apoorv_dependency_test.txt"

    # trainFile = "../debate08/debate08_dependency_train.txt"
    # trainFile = "../debate08/extended1_dependency_train.txt"
    # trainFile = "../debate08/extended2_dependency_train.txt"
    # trainFile = "../debate08/extendedAll_dependency_train.txt"
    # testFile = "../debate08/debate08_dependency_test.txt"

    # trainFile = "../dataset/dependency_train.txt"
    # trainFile = "../dataset/extended1_dependency_train.txt"
    trainFile = "../dataset/extended3_dependency_train.txt"
    # trainFile = "../dataset/extendedAll_dependency_train.txt"
    # testFile = "../dataset/dependency_test.txt"
    testFile = "../dataset/sms_dependency_test.txt"
    trainDpds = getDependency(trainFile)
    testDpds = getDependency(testFile)
    return trainDpds, testDpds

def loadIntersifier():
    intensifiers = []
    infile = open('./intensifier.txt', 'r')
    for word in infile.readlines():
        word = word.strip('\n\t')
        intensifiers.append(word)
    return intensifiers