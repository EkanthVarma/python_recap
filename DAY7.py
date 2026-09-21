'''
Inheritance --> It is one of the key properties of OOP

we can acquire properties (features) from one class to another class

Single Inheritance      --> Finger Print --> one child inheriting properties from one parent 
Multiple Inheritance    --> Parents --> Kids --> one child class can take properties from both parents
Multilevel Inheritance  --> level by level --> Family Tree
Hierarchal Inheritance  --> multiple child can inheriting properties from single parent
Hybrid Inheritance      --> Its a combination of diff types of inheritance

Single Inheritance

class Baseclass: #Parent class
    statement(s).......
    ...................
class Derivedclass(Baseclass):
    statement(s).......
    ...................


#updating usernames in a profile page

class Users:
    """Users class with basic details"""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        return f'{self.fname + self.lname}'
    
#u1 = Users('ekanth','seera')
#print(u1.fullname())
#Now we want to extend by updating username
class Update_Users(Users):
    #pass
    def update(self):
        return f'{self.fname.title()+" "+self.lname.title().strip()}'
#u1 = Update_Users('ekanth','seera')
#print(u1.fullname())
u1 = Update_Users('ekanth varma',' seera')
#print(dir(u1))
print(u1.fullname())
print(u1.update())

#Usage of class attribute and class methods in Inheritance

#class attributes --> They can be accessed directly with class name

#class method --> @classmethod

#banking scenario --> RBI Bank (Base class) --> SBI,HDFC

class RBI:
    """Base class with amount"""
    cash = 10000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        return f'Available cash with RBI is {RBI.cash}'
#r1 = RBI()
#print(r1.cash)
#print(r1.rbi_cash())
#print(RBI.cash)
#print(RBI.rbi_cash())
class SBI(RBI):
    pass
s1 = SBI()
#print(s1.cash)
#print(s1.rbi_cash())
#the same case we will access with classnames
class HDFC(RBI):
    cash = 5000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total Accessible cash is {cls.cash+RBI.cash}')
h1 = HDFC()
print(h1.cash)
print(h1.rbi_cash())
h1.hdfc_cash()

# In the same way what if we have different class attributes
class RBI:
    """Base class with amount"""
    cash = 10000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        return f'Available cash with RBI is {RBI.cash}'
class HDFC(RBI):
    amount = 5000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.amount}')
        print(f'Total Accessible cash is {cls.amount+cls.cash}')
h1 = HDFC()
print(h1.cash)
print(h1.amount)
print(h1.rbi_cash())
h1.hdfc_cash()
'''

#Single Inheritance usage --> Base class and Derived class with constructors
#Kid,Father --> Property scenario

class Father:
    """Father class with base property amount"""
    def __init__(self):
        self.fproperty = 2500000
    def father_prop(self):
        print(f'Father Propery is {self.fproperty}')

#f1 = Father()
#f1.father_prop()
'''
class Kid(Father):
    pass
k1 = Kid()
k1.father_prop()

#In above case its as it is not change in method and attribute usage
class Kid(Father):
    """Kid satrted earning"""
    def __init__(self):
        self.property = 500000
    def kid_prop(self):
        print(f'kid Propery is {self.property}')
        print(f'kid and father combined property is {self.property+self.property}')

u1 = Kid()
u1.father_prop()
u1.kid_prop()

#In this case --> Constructor Overriding as parent and child classes is having
#constructor , child class constructor will override parent class constructor

we have the usage of super() --> derived classes
--> Super class constructor --> super().__init__()
--> super class constructor with args --> super().__init__(args)
--> super class method (Method overriding) --> super().method()
'''
class Kid(Father):
    """Kid satrted earning"""
    def __init__(self):
        super().__init__() #calling superclass constructor
        self.kproperty = 500000
    def kid_prop(self):
        print(f'kid Propery is {self.kproperty}')
        print(f'kid and father combined property is {self.kproperty+self.fproperty}')

u1 = Kid()
u1.kid_prop()
u1.father_prop()

#in above case we have modified the attributes kproperty for kid and
#fproperty for father with super keyword
