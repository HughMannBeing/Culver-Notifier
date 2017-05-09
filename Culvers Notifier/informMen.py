from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import updateUser
from math import sqrt
import geoLocation

masterList = []
specialCases = {}


def getDistTo(testCords, newLocation):
    #Getting the two coordinates becase they're together
    latitude = str(testCords)[0:5]
    longitude = str(testCords)[5:len(testCords)]
    #newLocation might have to use something alittle more complicated, but we'll cross that brige later
    newLocation = getLocation.getCords(newLocation)
    difLat = abs(latitude - newLocation[0])
    difLong = abs(longitude - newLocation[1])
    totalDist = sqrt(difLat ** 2 + difLong ** 2)
    return totalDist

def createMail(newLocation):
    masterList = updateUser.updateList()
    specialCases = updateUser.getSpecialCases()
    #All the setup for the login to gmail
    fromaddr = "hughmannguy@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "") #generally the pass word goes here...
    for i in masterList:
        if i in specialCases:
            #Do something fancy to get the distance, and be fancy
            #should probably also remove these duplicates from the masterList...
            #In fairness, it's not a masterList then...
            masterList.remove(i)

        else:
            #Pass, and loop through at the end
            pass
    for key, value in specialCases:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = str(key)
        msg['Subject'] = "A new Culver's has opened!"
        body = "A new Culver's has opened in " + str(newLocation) + "! Thats only: " + str(getDistTo(value, newLocation) + " Miles from you!")
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(fromaddr, str(i), text)
    for i in masterList:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = str(i)
        msg['Subject'] = "A new culvers has opened!"
        body = "A new culver's has opened in "+ str(newLocation) + "! Can you believe it? Another one!"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(fromaddr, str(i), text)
    server.quit()
    print "Men have been informed..."
