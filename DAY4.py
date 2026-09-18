'''
Scenario to understand (*args and **kwargs)
Modules --> Some interesting cases -> Projects(Virtual Assistant, Email Automation)
OOP --> GitHub (branch)

Projects

Module --> A Module is simple python file(reusable,organised code) -> import keyword

Employee Details/Performance metrics (employee.py)
    --> employees function
    --> performance function
    --> Increment/Leadersgip/Learning function

OOP

Organisation --> class

Encapsulation, Inheritance, Polmorphism

Employees --> Function
Performance Metrics --> Function
Increment --> Function

Emp1,Emp2,Emp3,........ -> Object
'''
#Employee Details

def employees(*names,**settings):
    """Employee Details along with their Settings"""
    print("Employee Names")
    for employee in names:
        print('--------')
        print('-',employee)

    for key,value in settings.items():
        #print("Key is",key)
        #print("value is",value)
        print(key, ":" ,value)
        
'''employees("Ekanth","Kalyan","Deepika",
          department = "Operations",
          experience_letters = True,
          salary = 200000)'''

#if __name__ == "__main__":

details = {'Organization':'Codegnan',
            'Year':2018,
            'branches':['Vijaywada','Hyderabad','Vizag']}

print(__name__) #Dunder methods --> Magic methods

    

