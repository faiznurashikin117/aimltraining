# print("Write a function to find out the cube of given number")
# 5 : 5*5*5 (e.g. cube of 5 is 5*5*5 means 125)

# def cube(num):
#     return num**3

# num=(int(input("Enter number wanted to cube:\t")))
# print(f"cube for{num} is",cube(num))                   #????


# def multi(num1,num2):
#     return num1*num2

# fnum=int(input("Enter first number:\t"))
# snum=int(input("Enter second number:\t"))
# print(f'Result after adding {fnum} and {snum} is =\t',multi(fnum,snum))

# def cube(num):
#     return num*num*num

# given_num=int(input("Enter Number to find out cube of number:\t"))
# print(f"Number is:{given_num} cube is",cube(given_num))          


#Exercise
#Write a function to calculate bonus of given salary
#function take salary as input and return bonus 10% of salary.

def bonus(salary):
    return salary*0.1

given_salary=int(input("Enter your salary to find out bonus:"))
print(f"Salary is:{given_salary} bonus is",bonus(given_salary))
print("Your total salary is",given_salary+bonus(given_salary))



