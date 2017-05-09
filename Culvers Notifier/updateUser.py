"""
    This file is designed to design a personalized email for each user
    Telling them how far away the newst culvers is from them
"""

import os
import platform

emailList = []

if platform.system() == 'Windows':
    emailListFile = str(os.path.dirname(os.path.abspath(__file__)) + '\emailList.txt')
    recentTweet = str(os.path.dirname(os.path.abspath(__file__)) + '\store.txt')
else:
    emailListFile = str(os.path.dirname(os.path.abspath(__file__)) + '/emailList.txt')
    recentTweet = str(os.path.dirname(os.path.abspath(__file__)) + '/store.txt')

def getSpecialCases():
    casesDict = {}
    #open special Cases file, and get locatios and shit
    #Then add in the emails and their special case to the dictionary
    #Ill make it later
    pass

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
