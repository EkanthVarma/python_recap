'''
In this case we need to add subject and to address for email

we will use email package
'''
import email
import smtplib
#MIME - Multipurpose Interner Mail Extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#now we will provide the details
From = "ekanthvarma2005@gmail.com"
To = "knsknsk10@gmail.com"
subject = "hi guyyys!"
#now we will check all the details and throw it to Muli=tipart
msg = MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From'] = From
msg['To'] = To
msg['Subject'] = subject
msg['body'] = "narasimha bhai bhai bhai bhai bhai bhai bhai ............."
msg.attach(MIMEText(msg['body'],'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(From,"usfx srrr cjkl yzkw")
server.sendmail(From,To,text)
server.quit()
print("Mail Sent")


