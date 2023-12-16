def sum_digits(number):
    digit_sum = 0
    while number > 0:
        last_digit = number % 10
        digit_sum += last_digit
        number = number // 10
    return digit_sum

user_number = int(input('Enter a number: '))
digit_sum = sum_digits(user_number)
print(f'The sum of digits in {user_number} is: {digit_sum}')