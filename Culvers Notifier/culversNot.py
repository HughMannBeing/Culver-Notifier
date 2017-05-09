from bs4 import BeautifulSoup
import urllib2
from time import sleep
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import os
import platform

#Approved by #5

if platform.system() == 'Windows':
    emailListFile = str(os.path.dirname(os.path.abspath(__file__)) + '\emailList.txt')
    recentTweet = str(os.path.dirname(os.path.abspath(__file__)) + '\store.txt')
else:
    emailListFile = str(os.path.dirname(os.path.abspath(__file__)) + '/emailList.txt')
    recentTweet = str(os.path.dirname(os.path.abspath(__file__)) + '/store.txt')

emailList = []

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

def informTheMen(city):
    updateList()
    print "Informing the men..."
    fromaddr = "hughmannguy@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Zntx-172942")
    for i in range(0, len(emailList)):
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = str(emailList[i])
        msg['Subject'] = "A new culvers has opened!"
        body = "A new culver's has opened in "+ str(city) + "! Can you believe it? Another one!"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(fromaddr, str(emailList[i]), text)
    server.quit()
    print "Men have been informed..."

def updateList():
    if os.path.exists(recentTweet):
        pass
    else:
        target = open(recentTweet, "w+")
        target.close()
    if os.path.exists(emailListFile):
        with open(emailListFile) as target:
            for i, line in enumerate(target):
                emailList.append(str(line))
        target.close()
    else:
        target = open(emailListFile, "w+")
        target.write("hughmannguy@gmail.com")
        target.close()
    print "Email List has been updated..."

while True:
    checkOpenings()
    sleep(5)
