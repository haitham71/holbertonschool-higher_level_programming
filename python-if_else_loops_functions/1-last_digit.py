#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
zero = 0
num1 = number % 10 if number >= 0 else -(abs(number) % 10)
if num1 > 5:
	print(f"Last digit of {number} is {num1} and is greater than 5")
elif num1 == zero :
    print(f"Last digit of {number} is {num1} and is {zero}")
elif num1 < 6:
    print(f"Last digit of {number} is {num1} and is less than 6 and not {zero}")
