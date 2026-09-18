# BMI (Body Mass Index)

# Formula of BMI - (weight)/((height)**2) , weight-kg , height-m
records = []
n = int(input("enter no. of records:"))
for i in range(n):
    rows = []
    name = input(f'\nenter your name{i+1}:')
    weight = float(input("enter your weight in kgs:"))
    height = float(input("enter your height in meters:"))
    rows.extend([name,weight,height])
    if weight > 0 and height > 0:
        BMI = (weight)/((height)**2)
        if BMI < 18.5:
            print(f'{name} is in Under Weight and BMI is {BMI:.2f}\n')
            rows.append(f'{BMI:.2f}')
        elif 18.5 <= BMI <=24.9:
            print(f'{name} is in Normal Weight and BMI is {BMI:.2f}\n')
            rows.append(f'{BMI:.2f}')
        elif 25 <= BMI <=29.9:
            print(f'{name} is in Over Weight and BMI is {BMI:.2f}\n')
            rows.append(f'{BMI:.2f}')
        else:
            print(f'{name} is in Obesity and BMI is {BMI:.2f}\n')
            rows.append(f'{BMI:.2f}')
    else:
        print("your weight and height should strictly greater than 0\n")
    records.append(rows)
print(records)

# check whether negatuve values given
count = 0
while True:
    try:
        weight = int(input("enter your weight in kgs:"))
        height = float(input("enter your height in meters:"))
        name = input("enter your name:")
        if weight > 0 and height > 0:
            count += 1
            break
        else:
            print("your weight or height should be positive numbers\n")
            continue
    except Exception as e:
        print(f'The Error is {e}')
n = int(input("enter no. of records:"))
while count<=n:
    BMI = (weight)/((height)**2)
    if BMI < 18.5:
        print(f'{name} is in Under Weight and BMI is {BMI:.2f}\n')
    elif 18.5 <= BMI <=24.9:
        print(f'{name} is in Normal Weight and BMI is {BMI:.2f}\n')
    elif 25 <= BMI <=29.9:
        print(f'{name} is in Over Weight and BMI is {BMI:.2f}\n')
    else:
        print(f'{name} is in Obesity and BMI is {BMI:.2f}\n')

                
