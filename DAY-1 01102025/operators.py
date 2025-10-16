#Assignment operators: =, +=, -=
price=float(input("Enter Product Price"))
discount=price*0.10
disPrice=price-discount
print(f"Price:{price} \n Discount: {discount} \n DiscountedPrice:{disPrice}")


# Assignment operators: +=
salary=50000.50
bonus=5000.60

print(f"Salary{salary} and Bonus{bonus}")
salary+=bonus         #salary=salary+bonus
print("Salary with Bonus",salary)


# Assignment operators: -=
salary=50000.50
tds=salary*0.10

print(f"Salary{salary} and TDS {tds}")
salary-=tds         #salary=salary-tds
print("Salary sfter tax",salary)


#Comparison operators: ==, >, >=, <, != etc
#if(condition)
# #code
#else
# #code

# age=int(input("Enter your age"))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("You are not eligible to cast your vote, you have to wait")
# print("End of program")


# #Comparison operators: <
# marks=int(input("Enter marks percentage without '%' sign"))
# if(marks<30):
#     print("Fail in exam")
# else:
#     print("Clear the exam")


# #Comparison operators: !=
# #accessCode="wes12"
# accessCode=input("Enter Access Code")
# if(accessCode!="wes12"):
#     print("Invalid Access Code")
# else:
#     print("Welcome to your course")


##Comparison operators: ==
##accessCode="wes12" 
# accessCode=input("Enter Access Code")
# if(accessCode=="wes12"):
#     print("Welcome to our courses")
# else:
#     print("Invalid Access Code")
    

# #Logical Operators: and, or, not.
# phyMarks=int(input("Enter marks obtained in Physics: "))
# cheMarks=int(input("Enter your marks in Chemistry: "))
# mathMarks=int(input("Enter your marks in Mathematics: "))

# if((mathMarks>=55,) and (phyMarks>=50) and (cheMarks>=60)):
#     print("You are eligible to sit in pre exam of MBBS")
# else:
#     print("You have not got the required marks")


# #Logical Operators: or.
# idProof=input("Enter Id proof you have")
# if((idProof=="passport") or (idProof=="dl") or(idProof=="voter id")):
#     print(f"Valid Id {idProof} we accept here")
# else:
#     print("Only passport, dl and voter id are accepted as Identity Proof")
#     print(f"{idProof} is not valid here")


#Logical Operators: not.
mathMarks=int(input("Enter your marks in Mathematics:\t"))
gapYear=int(input("Enter Year gap if any otherwise Zero:\t"))
if ((mathMarks<=55) and (gapYear!=0)):
    print("Not eligible for BTech")
else:
    print("Eligible for BTech")




