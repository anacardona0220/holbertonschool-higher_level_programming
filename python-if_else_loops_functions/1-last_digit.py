#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = 100

if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

if number == 0:
    print(f'Last digit of {number} is {last_digit}  and is 0')    
elif number > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
else:
    print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')