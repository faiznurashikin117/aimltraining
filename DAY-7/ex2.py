# import random

# print('Random Number from 1 to 1000')

# print(random.randint(1,1000))

# import random
# name=input("Enter Your name\t")
# luckyNumber=random.randint(1,10)
# print(f"Welcome Mr.\\Ms\t {name}, Your coupon number is {luckyNumber}")
# if(luckyNumber==1):
#     print("You have won Proton XL-65 car")
# elif(luckyNumber==3):
#     print("You have won an ipad")
# elif(luckyNumber==9):
#     print("You have won an iPhone")
# else:
#     print("Better luck next time")


#create a function
import random
def findwinner():
    name=input("Enter Your name:\t")
    luckyNumber=random.randint(1,10)
    print(f"Welcome Mr.\\Ms\t {name}, Your coupon number is {luckyNumber}")
    if(luckyNumber==1):
        print("You have won Proton XL-65 car")
    elif(luckyNumber==3):
        print("You have won an ipad")
    elif(luckyNumber==9):
        print("You have won an iPhone")
    else:
        print("Better luck next time")
        


