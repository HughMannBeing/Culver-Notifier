from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import updateUser

masterList = []
specialCases = {}


def createMail(newLocation):
    masterList = updateUser.updateList()
    specialCases = updateUser.getSpecialCases()
    #All the setup for the login to gmail
    fromaddr = "hughmannguy@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Zntx-172942")
    for i in masterList:
        if i in specialCases:
            #Do something fancy to get the distance, and be fancy
            #should probably also remove these duplicates from the masterList...
            #In fairness, it's not a masterList then...
            masterList.remove(i)

        else:
            #Pass, and loop through at the end
            pass
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
