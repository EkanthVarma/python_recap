'''
Python --> Automation --> Email Automation
Simple Mail Automation
Mail OTP
mail with subject & attachments
Bult mail

usfx srrr cjkl yzkw - app password

#simple mail automation
#SMTP - Simple mail transfer protocol

import smtplib
#first lets make server connection
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("ekanthvarma2005@gmail.com","usfx srrr cjkl yzkw")
msg= "vunava poyava bhai"
server.sendmail("ekanthvarma2005@gmail.com",
                "deepikabarnikala0410@gmail.com",msg)
#close the connection
server.quit()
print("Mail Sent")


#Now lets send OTP to mail and vlaidate the script
import math
import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
otp = random.randint(1000,9999)
server.login("ekanthvarma2005@gmail.com","usfx srrr cjkl yzkw")
msg= f"your 4 digit OTP is {otp}"
server.sendmail("ekanthvarma2005@gmail.com",
                "ksankar8096@gmail.com",msg)

server.quit()
print("Mail Sent")
otp2 = int(input("enter OTP to access:"))
if otp2 == otp:
    print("you succesfully login")
else:
    print("disabled")
'''

#another approach
import math
import random
import smtplib

#in the case i will use math and random modules together
digits = '1234567890'
OTP = ""
for i in range(4):
    OTP += digits[math.floor(random.random()*10)]
msg = f'your OTP is {OTP}'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("ekanthvarma2005@gmail.com","usfx srrr cjkl yzkw")
server.sendmail("ekanthvarma2005@gmail.com",
                "ksankar8096@gmail.com",msg)
server.quit()
print("Mail Sent")
otp2 = input("enter OTP to access:")
if otp2 == OTP:
    print("you succesfully login")
else:
    print("disabled")

