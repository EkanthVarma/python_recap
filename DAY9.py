'''
Polymorphism --> Method Overloading, Method Overriding, Operator Overloading

#Method Overloading --> Default arguments,Variable length arguments, Type of args

#Method Overloading(Compile time Polymorphism) --> Default arguments

class HotStar:
    """default args usage"""
    def watch(self,movie=None):
        self.movie = movie
        if self.movie == None:
            print(f'Welcome to Hotstar')
        elif self.movie == movie:
            print(f'User watching {self.movie}')
u1 = HotStar()
u1.watch() #in this case we made movie as default
u1.watch("Vaaranasi")
a = u1.watch("ekanth","varma")

#scenario of adding movie to watchlist --> using variable length arguments

class HotStar:
    """*args usage"""
    def watch(self,movie=None):
        print("welcome to hotstar")
    def add_list(self,*movies):
        print(movies)
        for movie in movies:
            print(movie)

u1 = HotStar()
u1.watch()
u1.add_list("vaarnasi","bharath ane nenu","srimanthudu")

#method overloading with type of arguments (isinstance())
#Hotstar --> one movie,mutliple movies

class HotStar:
    """Usage of type of args"""
    def watch(self,movie=None):
        print(f'welcome to Hotstar')
    def movies_list(self,content):
        self.content = content
        if isinstance(content,str):
            print(f'User watching {self.content}')
        elif isinstance(content,list):
            print(content)
            for movie in content:
                print(movie)
        elif isinstance(content,tuple):
            print(content)
            for movie in content:
                print(movie)
u1 = HotStar()
u1.watch()
u2 = HotStar()
u2.movies_list("vaaranasi")
u2.movies_list(["ultimate:alien x","ultimate:garo","ultimate:india war"])
u2.movies_list(("ultimate:alien x","ultimate:garo","ultimate:india war"))

#Method Overriding --> Inheritance usage
#when the same method name is used in base class and aslo in derived class
#super()

#free user --> [can watch free content with advertisements]
#Premium User --> [can watch premium content withoutadvertisements]
#VIP User --> [can watch premium content alon =g with devices count,streaming]

class HotStar:
    def watch(self):
        print("welcome to HotStar")
class Free_User(HotStar):
    def watch(self):
        super().watch()
        print("you can see free content with advertisement")
class Premium_User(Free_User):
    def watch(self):
        super().watch()
        print("you can see premium content without advertisement")
class VIP_User(Premium_User):
    def watch(self):
        super().watch()
        print("you can see premium content without advertisement and devices count and streaming is also available ")
#u1 = Free_User()
#u1.watch()
#u2 = Premium_User()
#u2.watch()
u3 = VIP_User()
u3.watch()

#Operator Overloading --> (Magic methods/dunder methods) __init__(),__add__()

a =13;b=24
print(a+b)
print(a.__le__(b))
print(a.__add__(b))
print('codegnan '.__add__('python'))
print([1,2,].__add__([3,4,5]))

#in above case same __add__() is performing different cases (Addition,concatenation,merging)

a = [1,2,3,4]
print(a.__len__())
'''

#now linking above operators scenario to Hotstar

class WatchHistory:
    """Duration of watching content"""
    def duration(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
        print(f'user watching {self.hours} hours duration')
u1 = WatchHistory()
u1.duration(25)
u2 = WatchHistory()
u2.duration(35)
#get the complete duration
print(u1+u2)
#print(u1.hours + u2.hours)
u1.__str__()
u2.__str__()

