"""
    This file is designed to design a personalized email for each user
    Telling them how far away the newst culvers is from them
"""

import os
import platform

emailList = []

if platform.system() == 'Windows':
    emailListFile = str(os.path.dirname(os.path.abspath(__file__)) + '\emailList.txt')
    specialCaseFile = str(os.path.dirname(os.path.abspath(__file__)) + '\specialCases.txt')
else:
    emailListFile = str(os.path.dirname(os.path.abspath(__file__)) + '/emailList.txt')
    specialCaseFile = str(os.path.dirname(os.path.abspath(__file__)) + '/specialCases.txt')

def getSpecialCases():
    casesDict = {}
    data = []
    #open special Cases file, and get locatios and shit
    #Then add in the emails and their special case to the dictionary
    #Ill make it later
    with open(specialCaseFile) as target:
        for line in enumerate(target):
            #this is where formatting might be a little important
            data.append(line)
    target.close()
    #Im just going to say that each user has 3 lines
    #Line 1 is email, 2 is their latitude, and 3 is their longitude
    if (data % 3) == 0:
        #Something went wrong
        pass
    else:
        for i in range(0, len(data)):
            casesDict[data[i]] = str(data[i + 1])[:5] + str(data[i + 2])[:5]
            i = i + 2
    return casesDict

def updateList():
    returnList = []
    if os.path.exists(recentTweet):
        pass
    else:
        target = open(recentTweet, "w+")
        target.close()
    if os.path.exists(emailListFile):
        with open(emailListFile) as target:
            for i, line in enumerate(target):
                returnList.append(str(line)[:len(line) - 1])
        target.close()
    else:
        target = open(emailListFile, "w+")
        target.write("hughmannguy@gmail.com")
        target.close()
    return returnList
