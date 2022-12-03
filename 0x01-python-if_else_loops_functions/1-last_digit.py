#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
if number < 0:
    last_digit = int(num_str[-1])
    last_digit = last_digit * -1
else:
    last_digit = int(num_str[-1])

if (last_digit % 10) > 5:
    msg = "and is greater than 5"
    print(f"Last digit of {number} is {last_digit} {msg}")
elif (last_digit == 0):
    msg = "and is 0"
    print(f"Last digit of {number} is {last_digit} {msg}")
elif last_digit < 6 and last_digit != 0:
    msg = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit} {msg}")
