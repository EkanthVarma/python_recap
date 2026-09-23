'''
Usage of super()
#super with arguments --> super().__init__(args)

class Father:
    """Father class with base fproperty argument"""
    def __init__(self,fproperty):
        self.fproperty = fproperty
    def father_prop(self):
        print(f'Father Propery is {self.fproperty}')
class Kid(Father):
    """Kid class with kproperty argument"""
    def __init__(self,kproperty,fproperty):
        super().__init__(fproperty) #calling superclass constructor with args
        self.kproperty = kproperty
    def kid_prop(self):
        print(f'kid Propery is {self.kproperty}')
        print(f'kid and father combined property is {self.kproperty+self.fproperty}')
k1 = Kid(500000,250000)
k1.father_prop()
k1.kid_prop()
print(k1.__dict__)

class Square:
    """Area of square"""
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f'Area of square is {self.x * self.x}')
class Rectangle(Square):
    """derived class"""
    def __init__(self,y,x):
        self.y = y
        super().__init__(x) #caling superclass constructor with args
    def area(self):
        super().area() #calling superclass with method
        print(f'Area of square is {self.x * self.y}')
a1 = Rectangle(7,8)
a1.area()
x,y = map(int,input("enter the values").split(','))
a2 = Rectangle(x,y)
a2.area()
#a2 = Square(5) #as we are creating different objects its possible
#print(a2.area())
'''

#Multiple Inheritance --> Whatsapp Scenario --> Users ,Bussiness Users,Premium Users
'''
Multiple base classes with single derived class

class base1:
    statement(s).........
class base2:
    statement(s).........
class derived(base1,base2):
    statement(s).........

class Users:
    """Users class with basic features"""
    def voice_call(self):
        print("User can make voice calls")
class Notifications:
    """Notifications reaching out"""
    def send_notifications(self):
        print("User can get pop-up notifications")
class PremiumUsers(Users,Notifications):
    """Extra feature added"""
    def verification_badge(self):
        print("User is  verified and bluetick added")
u1 = PremiumUsers()
u1.verification_badge()
u1.voice_call()
print(dir(u1))
'''
#Multilevel Inheritance
'''
class base1:
    statement(s).........
class base2(base1):
    statement(s).........
class base3(base2):
    statement(s).........


class Users:
    """Users class with basic features"""
    def send_messages(self):
        print("user can send messages")
    def voice_call(self):
        print("User can make voice calls")
class BussinessUsers(Users):
    """first derived class"""
    def create_catalog(self):
        print("Details are added successfully")
class PremiumUsers(BussinessUsers):
    """second derived added"""
    def verification_badge(self):
        print("account is verified")
u1 = PremiumUsers()
u1.verification_badge()
u1.create_catalog()
u1.send_messages()
u1.voice_call()

#Heirarchical Inheritance

class Users:
    """Users class (base class)"""
    def send_messages(self):
        print("user can send messages")
    def voice_call(self):
        print("User can make voice calls")
    def ads(self):
        print("User can publish ads")
class NormalUsers(Users):
    """first child class"""
    def register(self):
        super().send_messages()
        print("registered successfully")
class PremiumUsers(Users):
    """second child class"""
    def verification_badge(self):
        super().voice_call()
        print("account is verified")
class BussinessUsers(Users):
    """second child class"""
    def publish(self):
        super().ads()
        print("bussiness account is verified")
        
n1 = NormalUsers()
n1.register()
print()
p1 = PremiumUsers()
p1.verification_badge()
print()
b1 = BussinessUsers()
b1.publish()

#Hybrid Inheritance
'''
#Polymorphism --> Method Overloading, Method Overriding, Operator Overloading
#poly -> Many
#morph -> forms

#HotStar --> Free Users, Premium Users, VIP Users

class HotStar:
    """Understanding polymorphism"""
    def watch(self):
        print("User logged in and surfing basic content")
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
u1 = HotStar()
u1.watch("Vaarnasi")





