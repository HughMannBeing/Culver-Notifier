from bs4 import BeautifulSoup
import urllib2
from time import sleep
import smtplib
import os
import platform
import informMen
import updateUser

#Approved by #5

if platform.system() == 'Windows':
    recentTweet = str(os.path.dirname(os.path.abspath(__file__)) + '\store.txt')
else:
    recentTweet = str(os.path.dirname(os.path.abspath(__file__)) + '/store.txt')

def getCity():
    store = []
    with open(recentTweet) as target:
        for i, line in enumerate(target):
            store.append(line)
    target.close()
    return store[0]

def checkOpenings():
    page = urllib2.urlopen("https://twitter.com/culvers")
    soup = BeautifulSoup(page, "html.parser")

    tweets = soup.find_all('p', 'js-tweet-text')
    checkCity = getCity()

    if "Culver's" in str(tweets[0])[104:116] and ((str(checkCity)[0:4] in str(tweets[0])[117:128]) == False):
        print "Found new opening!"
        newCity = str(tweets[0])[117:128]
        informTheMen(newCity)
        updateCity(newCity)
    else:
        print "No new opening found..."

def updateCity(city):
    print "City updated..."
    target = open(recentTweet, 'w+')
    target.truncate()
    target.write(str(city))
    target.close()

while True:
    checkOpenings()
    sleep(5)
