number = int(input('Enter a number: '))
digit_sum = 0
while number>0:
    digit_sum += number % 10
    number //= 10

print(f'{digit_sum}')