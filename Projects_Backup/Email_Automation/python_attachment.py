'''
Now we are adding an attachment along with subject to send email..
'''

import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

From = "ekanthvarma2005@gmail.com"
To = "ksankar8096@gmail.com"
subject = "Python Full Stack"
body = "We have understand how to send automated emails using python"
attach = "ekanthmail.py" #in same folder
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = subject
msg.attach(MIMEText(body))
#now we need to add attachment to our mail
part = MIMEBase('application','octet-stream')
print(part)
part.set_payload(open(attach).read())
encoders.encode_base64(part)
#lets add the header to our filename
part.add_header('Content-Disposition',
                f'attachment;filename={os.path.basename(attach)}')
msg.attach(part)
#finally convert this to string
text = msg.as_string()
#include your smtplib code
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("ekanthvarma2005@gmail.com","usfx srrr cjkl yzkw")
server.sendmail(From,To,text)
server.quit()
print("Mail Sent")
