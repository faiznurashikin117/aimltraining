import math
import random
# my_num=int(input("Enter number to find out square root:\t"))
# print(f"Square root of {my_num} is:\t",math.sqrt(my_num))

# print("Your lucky number from 1 to 100 is:",random.randint(1,100))

# # To check function inside module
import math
import inspect

functions=inspect.getmembers(math,inspect.isbuiltin)
for n, func in functions:
    print(n)

# print(math.sin(90))
# print(math.tan(90))
# print(math.cos(90))

# deg=int(input("Degree to find out cos"))
# print(f"Cos {deg} is:\t",math.cos(deg))

