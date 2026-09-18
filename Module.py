'''#Every Python File --> Module --> import keyword --> __name__ --> 
import DAY4
print(dir(DAY4)) #dir --> dir will return all available methods,attributes
print(type(DAY4.employees))
print(type(DAY4.details))

DAY4.employees("Ekanth",place="vzm",
               grade="A+")
#print(DAY4.details.keys())
print(DAY4.details['Organization'])
DAY4.details.update({'batches':['PFS','JFS','DA'],
                     'employees':240})
print(DAY4.details)

#from keyword
from DAY4 import employees,details
details.update({'batches':['PFS','JFS','DA'],
                     'employees':240})
print(details)
print(DAY4.__doc__) #returns Doc string from the given module
'''
#Built-in modules --> math,random,os,time,datetime

#we download modules --> pypi (python package index)

#Build a QRCode Scanner using Python --> Linkedin URL
#pyqrcode,png

import pyqrcode
import png
#create a QRcode by giving a link
link = "https://www.linkedin.com/in/ekanthvarmaseera/"
qr = pyqrcode.create(link)
#print(qr)
qr.png("mylinkedinqr.png",scale=10)

#personal bussiness card --> Name,Phone number, Email,Website.....

                                
