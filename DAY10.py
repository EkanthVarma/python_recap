'''
OOP - Encapsulation, Inheritance, Polymorphism, Abstraction


#Abstraction - It is the process of hiding necessary details and display / access relevant  iinformation only
#Module abc

import abc
#print(dir(abc))  #It  returns available methods, classes.......

from abc import ABC, abstractmethod

#Now we will create some base classes to have abstraction applied for all classes
class Content(ABC):
    @abstractmethod
    def upload(self):
        print("******")
        #pass
class Photo(Content):
    """This dervied class will have upload features"""
    def upload(self):
        print("Photo is uploaded successfully")
        print("Photo is compressed and edited as per filters choosen")
        print("Photo is posted")
class Video(Content):
    """This is dervied class will have video upload features"""
    def upload(self):
        print("Encoding the video")
        print("Cmpressed and filters are added")
        print("Edited video is published successfully")
class Reel(Content):
    """This dervied class will have reel uploading features"""
    def upload(self):
        print("Timing and content is choosen")
        print("Reel content is mapped with time and audience")
        print("Reel is edited and uploaded successfully")
    
content_ = [Photo(), Video(), Reel()]
#print(content_)
for content in content_:
    content.upload()



#List Compprohensions - Optimized way of creating and using lists

Syntax - [expression for var in collection / function]




list_ = [1, 2, 3, 4]
for i in range(1, len(list_) +  1):
    l = i ** 2
    list_.append(l)
print(list_)

list_ = [1, 2, 3, 4]
for i in list_:
    l = i ** 2
    list_.append(l)
    print(list_)


#In above it gets into infinite and also limits be exceeded
lst = []
for i in range(10):
    lst.append(i)
    print(lst) #In this case it prints for every iteration
print(lst)

list_ = [i ** 3 for i in range(1, 20)]
print(list_)



#To access desired elements and make change

data = ["ekanth", "varma", "mani", "kalyan"]
new_data = []
#Change every name to uppercase
for i in data:
    new_data.append(i.upper())
print(new_data)

#Using List compression
new_data = [i.title() for i in data]
print(new_data)

#To update each value in a list

marks = [14, 15, 12, 13]
d = [i + 30 for i in marks]
print(d)


#Every list comprehension can be converted to loops, but every loop cannot be converted to list comprehension

#List Comprehension with if clause
#Syntex: [expression for var in collection/function if <condition>]

g = [i for i in range(1,21) if i%2==0]
print(g)
h = [i**2 for i in range(1,21) if i%2==0]
print(h)

#Write above two cases as functions
def even_number():
    g = []
    for i in range(1,21):
        if i%2 == 0:
            g.append(i)
    return g
print(even_number())

def square_of_even_numbers():
    g = []
    for i in range(1,21):
        if i%2 == 0:
            g.append(i**2)
    return g
print(square_of_even_numbers())

#same above case using filter
h = list(filter(lambda i:i%2==0,range(1,21)))
print(h)

names = ['ekanth','manikanth','ramachandra']
k = list(filter(lambda x:len(x)>=7,names))
print(k)

#in below case length of each object is returned in a new list
a = list(map(lambda x:len(x),names))
print(a)

#group of values --> map
j = list(map(int,input('enter values with comma:').split(','))) #comma separated values
print(j)

a,b = map(int,input('enter values with space:').split()) #space separated values
print(f'value of a is {a}, value of b is {b}')

#multiple string values

name,place = input().split()
print(f'Name is {name}, Place is {place}')

#group of names
names = list(map(str,input('enter the name:').split(',')))
print(names)

names = ['ekanth','manikanth','ramachandra']
new_names = list(map(lambda x:x.upper(),names))
print(new_names)

prices = [2500,3500,5000,7500]
#create filtered prices by applying discount of 10% for each price
discount = list(map(lambda x:((x) - (x*0.1)),prices))
print(discount)

#List Comprehension with if-else usage
#Syntax --> [true_value if condition else false_value for exp in collection/func]


#filter even odd values in given range

result = ['even' if i%2==0 else 'odd' for i in range(1,21)]
print(result)

#in below case even number will be squared and odd value will be same numbers as it is
result = [i**2 if i%2==0 else i for i in range(1,21)]
print(result)


#Nested loops with List Comprehension
#Syntax --> [expression for item1 in iter1 for item2 in iter2]

colors = ['Green','Red','Blue']
sizes = ['S','M','L']
matching = [(i,j) for i in colors for j in sizes]
print(matching)

marks = [29,27,30,29]
weekly = [35,30,45,48]
#final = [i+j for i in marks for j in weekly]
final = list(map(lambda i,j:(i+j),marks,weekly))
print(final)
'''

#Nested Comprehension with if-else combination
#Syntax --> [true_value if <condition> else false_value for item1 in iter1 for item2 in iter2]

f = [i+5 if i>=j else i-1 for i in range(1,5) for j in range(1,5)]
print(f)
print(*f) # it unpacks values from collection
for i in f:
    print(i,end=' ')

#TypeError,ValueError --> most common errors











