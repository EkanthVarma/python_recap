# exapmle 1
def example(*a,**b):
    print(a)
    print(b)
    print("sum of a:",sum(a))
    print("length of a:",len(a))
    print("length of b:",len(b))

example(1,2,3,4,name = "ekanth", age=21)

# example 2
def _employee_(*args, **kwargs):
    """enter 'performance scores' and 'employee details'"""
    print(f'Employee Name: {kwargs["name"]}\nDepartment: {kwargs["department"]}')
    print(f'Total Score: {sum(args)}')
    print(f'Average Score: {sum(args)/len(args)}')

emp_dict = {
    "name": input("Enter employee name: "),
    "department": input("Enter department: ")
}

print("Enter performance scores:")
_employee_(
    int(input("Communication: ")),
    int(input("Problem Solving: ")),
    int(input("Technical Skills: ")),
    int(input("Teamwork: ")),
    **emp_dict
)
