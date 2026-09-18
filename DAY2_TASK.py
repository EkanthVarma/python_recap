# BMI for individual students
results = []
number_of_users = int(input("Enter the number of users: "))
for i in range(number_of_users):
    while True:
        try:
            name = input("Enter your name: ")
            weight = float(input("Enter the weight in Kgs: "))
            height = float(input("Enter the height in meters: "))

            if weight > 0 and height > 0:
                break
            else:
                print("Enter only positive values")
                continue

        except Exception as e:
            print(f'{e} , Enter correct values only')

    bmi = weight / (height ** 2)

    if bmi<18.5:
        print(f'{name} is into Under Weight category and BMI is {bmi:.2f}')
    elif  18.5<=bmi<=24.9:
        print(f'{name} is into Normal Weight category and BMI is {bmi:.2f}')
    elif 25<=bmi<=29.9:
        print(f'{name} is into Over Weight category and BMI is {bmi:.2f}')
    elif bmi>=30:
        print(f'{name} is into Obesity category and BMI is {bmi:.2f}')

    result = {
        "name": name,
        "weight": weight,
        "height": height,
        "BMI": f'{bmi:.2f}',
    }

    results.append(result)

print("\nBMI Results:")

for result in results:
    print(result)
