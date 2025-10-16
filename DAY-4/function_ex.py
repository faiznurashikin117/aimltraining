# def function_name(parameters):
#     '''Docstring'''
#     statements

#function without parameters
def welcome():
    print("Welcome to Functions")
    print("Our First function")

# welcome()


# #function with parameters
def welcome(name):
    print("Welcome to functions in python Mr.\\Ms",name)
    print("Hope Mr.\\Ms",name," are in good health!") #{} use for value, no {} for xvalue

username=input("Enter your name:\t")
#function call
welcome(username)


# #function with parameter and return

def add(num1,num2):
    return num1+num2

fnum=int(input("Enter first number:\t"))
snum=int(input("Enter second number:\t"))
print(f'Result after adding {fnum} and {snum} is =\t',add(fnum,snum))


def multi(num1,num2):
    return num1*num2

fnum=int(input("Enter first number:\t"))
snum=int(input("Enter second number:\t"))
print(f'Result after adding {fnum} and {snum} is =\t',multi(fnum,snum))