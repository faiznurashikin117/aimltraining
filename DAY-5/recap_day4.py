# def display():
#     print("Welcome to recap of functions")

def welcome(name):
    print("Welcome to functions Mr.\\Ms. ",name)

def cube(num):
    cube_num= num*num*num
    print(f"The cube of given number {num} is =\t {cube_num}")

# def square(num):
#     return num*num

# def salBonus(salary):
#     return salary*0.10


# welcome('sam')
# display()
my_num=int(input("Enter number to find out Cube:\t"))
cube(my_num)

#Exercise
# username=input("Enter User Name:\t")    #test
# my_num=int(input("Enter number to find out cube and square:\t"))   #test
# welcome(username)
# cube(my_num)
# square(my_num)


# print(welcome(username) , cube(my_num)) #myanswer #wrong

# #Exercise 2
# sq=square(my_num)
# print(f"Square of m{my_num} is: {sq}")
# print(f"Number:{my_num} Square:{sq}")

# #Exercise 3
# my_sal=float(input("Enter salary to find outbonus:\t"))
# bonus=salBonus(my_sal)
# print(f'Salary {my_sal} Bonus:{bonus}')
# print(f"Salary after bonus =\t",(my_sal+bonus))

# def salBonus(salary):
#     bonus=salary*0.10
#     newSalary=bonus+salary
#     print(f"Salary {salary} Bonus:{bonus}")

# my_sal=float(input("Enter Salary to find out bonus:\t"))
# salBonus(my_sal)
# print("Salary after bonus \t") #no function can be used bcz funtion provided is only bonus, not salary+bonus

