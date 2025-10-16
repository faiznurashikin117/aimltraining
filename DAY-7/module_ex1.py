import math
import inspect

# num=int(input("Enter number to find out square root"))
# print(f"Square root of {num} \t",round(math.sqrt(num),2))


functions=inspect.getmembers(math,inspect.isbuiltin)

print("All function in math module")
for n,func in functions:
    print(n,end="\t")