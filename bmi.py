mass = float(input('Your weight in kgs: '))
height = float(input('Your height in metres: '))
bmi_1 = mass / height**2
bmi = float(bmi_1)

if bmi < 18.5:
    print('High risk: the weight is too low')
elif bmi >= 18.5 and bmi <= 25:
        print('Minimum/Low risk')
elif bmi >= 25 and bmi <= 30:
    print('Low/Medium risk')
elif bmi >= 30 and bmi <= 35:
    print('Medium/High risk')
else:
    print('High risk: the weight is too high')