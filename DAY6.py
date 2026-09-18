'''
oops--->object oriented programming -->objects

pop--->proodure oriented programming -->Fuctions

#chair(object) -->Wood (materials.Desgin (Dimesions),person

A chair is a blueprint of a object

A object is a real world eninty which contains --> Attributes (varibles)

A object is a real world entity which contanis -->Attributes(Fuctions)

class keyword

Flipkart --> Products --> laptops,moblies,gadgets....

Features -->Encapsulation,Interitance,Polymorphism

class keyword

Flipkart --> Products --> laptop,mobiles,gadgets........

Features --> Emcapsulation,Inheritance,Polymorphism

#function --> house
#class --> Power House

class ClassName:
    """docstring"""
    #attributes (define the data)
    .......
    .......
    def fname(self): #behaviour
        statement(s)...
        ...............
obj = ClassName()


#Students --> name,age
class Students:
    """Students details"""
    name = "Ekanth"
    age = 21
    place = "Vizianagaram"

    def details(self):
        print(f'{self.name} is in {self.place} have age of {self.age} years')
stu = Students()
print(stu)
print(dir(stu))
print(stu.name,stu.age,stu.place)
#print(stu.details()) # type error
#print(stu.details()) # name error
stu.details()
st2 = Students()
st2.details()

#in above case how many objects u create the result will be same
class Students:
    """Student details for multiple students"""
    def details(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    #now to access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
#name = input("enter your name:")
#age = int(input("enter your age:"))
#place = input("enter your place:")
st1 = Students()
st1.details("ekanth",21,"Vizianagaram")
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)
st2 = Students()
st1.details("manikanth",20,"vizag")
st1.display()

#In this case we want objects to be intialized --> __init__()
class Students:
    """Student details for multiple students"""
    def __init__(self,name,age,place):
        self.name = name #instance variables
        self.age = age
        self.place = place
    #now to access those details
    def display(self): #instance method
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1 = Students("Dileep",24,"Bbs")
st1.display()
st2 = Students("Sankar",21,"Gjw")
st2.display()
print(st2.__dict__)

#Create a cars class with attributes as brand,name,price
#create mutliple objects

class Cars:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def display(self):
        print(f'car brand is {self.brand} and its name is {self.name} and have price is {self.price}')
        
c1 = Cars("Maruti","swift",400000)
c1.display()
c2 = Cars("Audi","A3",900000)
c2.display()
c3 = Cars("BMW","M5",800000)
c3.display()

#Encapsulation --> How the methods and the attributes are binded to single class,
#in similar way how we can access the data --> public,proteted,private

#public attributes --> can be created and modified even outside the class

class Users:
    """usage of public attributes"""
    def __init__(self,username):
        self.user = username #public attriibute
    def display(self):
        print(f'Username is {self.user}')
u1 = Users("john")
print(u1.user)
u1.user = "sam" #we can modify the public attribute
print(u1.user)
u1.display()
     
#Protected Attribute --> These can also be modified outside the class, its
#mainly useful as a hint/coding convetion for other users/developers
#to create a protected attribute we use underscore --> _otp

class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp):
        self.user = username #public attribute
        self._otp = _otp #protected attribute
    def display(self):
        print(f'username is {self.user}')
        print(f'OTP is {self._otp}')
        
u1 = Users("saketh",4352)
u1.display()
u1._otp = 5435
u1.display()

#private attribute - restrict the usage and cannot be directly accessed
#we have the usage or notation as double leading underscore --> __password

class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user = username #public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attribute
    def display(self):
        print(f'username is {self.user}')
        print(f'OTP is {self._otp}')

u1 = Users("Ekanth",9105,"ekanth143")
print(u1.user,u1._otp)
#print(u1.__password)
#in above case password cant be accessed directly --> NameMangling
print(u1._Users__password)

#usage of getter(),setter() methods
'''
class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user = username #public attribute
        self._otp = _otp #protected attribute
        self.__password = __password #private attribute
    #usage of getter() or get() method fro password
    def get_password(self):
        """getter method for password"""
        #return "******"
        return self.__password
    #usage of setter() to modify the data
    def set_password(self,new_password):
        """setter method for password"""
        if len(new_password) < 6:
            return 'Password length is not matching'
        else:
            self.__password = new_password
            return 'Updated password'
u1 = Users("admin",5423,"admin")
print(u1.get_password())
print(u1.set_password("admin"))
print(u1.set_password("admin123"))
print(u1.get_password())
print(u1.__dict__)






        
