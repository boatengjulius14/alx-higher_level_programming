#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
str = f"Last digit of {number} is {last_dig} "
if last_dig > 5:
    str += "and is greater than 5"
elif last_dig == 0:
    str += "and is 0"
elif last_dig < 6 and last_dig != 0:
    str += "and is less than 6 and not 0"
print(str)
