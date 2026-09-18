'''
=> Python project --> POP / OOP --> DSA (Logic based --> pattern based --> platform
=> POP (Procedure Oriented Programming) --> Dividing the entire code into blocks --> procedure --> functions(def)
=> Functions --> A reusable block of code (A block of statements which performs a specific task)

syntax :
def <funcname>(parameters): #fun def
    """DOC String"""
    statement(s)...     #body of func
    ...............
    return value(s)...
funcname(args) #func call
'''
#simple scenario to understand

def add(a,b):
    """Addition Function"""
    c = a+b
    return c
print(add(4,5)) #addition
c,d = 'codegnan ','python'
print(add(c,d)) #concatenation
e,f = map(str,input("enter your values").split(','))
print(add(e,f))
print(add([1,3,4],[4,6,7])) #merging
# print(add(1,2,3,4)) #positional arguments

#Variable length arguments --> *args - we can pass any no of postional arguments --> data will be stored in tuple

def sample(*a):
    """Demo of varaible lenth arguments"""
    print(a)
    print(type(a)) #default it stores in tuple format
sample()
sample(1,2,3,4,5,6,7,8,9,0)
sample('codegnan',[23,4],'poll',2+5j)

marks = [20,15,25,18]
sample(marks)
sample(*marks) # to use collection individual we have use * infront of variable

# * is used to unpack the values into a collection
a,*b,c = 12,'code','poll',23,4,9
print(a)
print(b)
print(c)

d = 12,'code','poll',23,4,9
print(d)

def add(*a):
    """Perform addition for numeric values"""
    print(a)
    result = 0
    for i in a:
        #pirnt(i)
        #if type(i) in [int,float]:
        if type(i)==int or type(i)==float:
            result += i
    return result
print(add(2,3,4))
print(add(2,'codegnan',3,4))

#keyword arguments --> we can pass the name for the arguments

def batch(name='ekanth',age,place='vzm'):
    """Keyword arguments usage"""
    print(f'{name} is in {place} and age is {age} years')
batch('ekanth',21,'vzm')
batch(place='vsp',name='shankar',age=21)
#keyword arguments only needs name matching not order
batch(name='mani',age=19)
#default arguments can accept a value as default

print(4,5)
print(4,5,sep=':') #here keyword argument is sep and we are changing the default value for sep

#keyword variable length arguments (**kwargs) --> any no of keyword arguments, data is stored in dictionary
def batch(**a):
    """ Keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch()
batch(name="ekanth",age=21,place="vzm",branch="ai&ds")

data = {'names':['ekanth','sankar'],
        'place':['vzm','vsp']}
data.update({'batch':'PFS-VSP-004'})
batch(**data)


#Task - create a function with the usage of *args & **kwargs




