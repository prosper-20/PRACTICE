import smtplib

to = input("Enter the email of recipient: \n")

content = input('Enter the content for mail: \n')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("edwardprosper001@gmail.com", "EddiePdgr8")
    server.sendmail("edwardprosper001@gmail.com", to, content)
    server.close()

sendEmail(to, content)