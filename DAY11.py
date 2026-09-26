'''
List Comperhension --> Tuples

Generators, Execep;tion Handling along with File handling

b = [i for i in range(1,10) if i>4]
print(b)
print(type(b))

#in python there is no Tuple Comprehension --> Generators
b = (i for i in range(1,10) if i>4)
print(b)
print(type(b))

#Generator --> it is also a special function in python which produces value one by one,
#which makes program memory efficient

def details():
    """Simple Function"""
    return f'Codegnan is in Vizag'
print(details())
#in  above case if we pass multiple return statements it doesnt retuirn
#the results, whereas a single return statement can pass multiple value

def details():
    """return with multiple values"""
    return 'Codegnan is in Vizag','ekanth is in codegnan'
print(details())


def subjects():
    """stidents subjects  details"""
    yield "pyhton"
    yield "MYSQL"
    yield "Aptitude"
    yield "Frontend"
#print(subjects()) #this becomes a generator object
subject = subjects()
print(subject)
print(type(subject))
#As above function becomes a generator to access values from the function
#we use next() keyword, or we prefer loop , or we can also use * to unpack valueprint(next(subject))#first value is returned

print(next(subject))
print(next(subject))
print(next(subject))
print(next(subject)) #raises StopIteration as all values are accessed
for i in subject:
    print(i)
    #print(next(i)) # its not possible as already we have used for loop
#Once we use next() function loop usage is not needed

print(*subject) #it unpacks the vlaues are return all at a time (side by side)

#now no tuple comprehension --> Generator to access values
b = (i for i in range(1,10) if i>4)
#print(*b)
for i in b:
    print(f'value is {i}')
    
#either we prefer *usage or loop usage
a,b = 3,5
a,b,*c = 12, 'codegnan','ekanth','vzm',25
print(a)
print(c)
print(b)
'''

#Exception Handling --> Exception Handlind is the process of making the program
#or script to function(normally)
#we use keywords --> try,expect,finally
'''
try:
    #program to execute/conditions.. it will also raise errors
except:
    #it will handle the error
finally:
    #irrespective of try,except it executes

#Base Exception handling
try:
    a,b = map(int,input('enter the values:').split(','))
    c = a/b
    print(c)
except Exception as e:
    print(e)
#in above case we didn't specially tell the error name

#syntax errors and logical errors --> user have to handle
#runtime Errors --> machine (Exception Handling)
#Multiple Exceptions

try:
    a,b = map(int,input('enter the values:').split(','))
    c = a/b
    print(c)
except ZeroDivisionError:
    print('make sure the denominator value is only +ve/-ve')
except ValueError:
    print('make sure the check correct integer values')
except NameError:
    print('sarigo chusko')

#For a part. usecase think of all possible error types
try:
    a = [34,2,4,6]
    print(a[2])
    a.append('codegnan')
    print(a)
except IndexError:
    print("check the elements count properly")
except AttributeError:
    print("Do check the method names properly")
finally:
    print("Its done")

#Multiple Exceptions at a time

try:
    a = [34,2,4,6]
    print(a[2])
    a.append('codegnan')
    print(a)
except (IndexError,AttributeError,NameError) as e:
    print(e)
finally:
    print("Prepare well")
'''

#File handling --> 'r' --> Read(),'w' --> write(),'a','r+'
#with keyword usage

#'r+' --> Read() and write()

with open('day11.txt','r+') as f:
    #print(f) #it returns a wrapper object
    print(f.read()) #we can read the content
    f.write(" Vizianagaram boy")
    print(f.read())
#in above cases first read() and write() differs, whereas if we use write()
#it starts modifying from the beginning of the file...

#OOP Usecases --> pick one/two (star performer) deadline before monday
#send your Gitlinks in group..

























