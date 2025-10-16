def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

print("Welcome to our Calculator")
while True:
    print("Select Operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit")
    op=int(input("Enter your operation choice:\t"))
    if(op==6):
        print("Goodbye")
        break
    if (op>=7)or(op<=0):
        print("Wrong operation choice, please choose only 1 to 6")
        break
    else:
        fnum=float(input('Enter first number:\t'))
        snum=float(input('Enter second number:\t'))
        if(op==1):
            print(f"Result after adding:\t",add(fnum,snum))
        elif(op==2):
            print(f"Result after subtracting:\t",sub(fnum,snum))
        elif(op==3):
            print(f"Result after multiplying:\t",multi(fnum,snum))
        elif(op==4):
            print(f"Result after dividing:\t",div(fnum,snum))
        elif(op==5):
            print(f"Average:\t",avg(fnum,snum))


#another example if want to do differnt operations for same numbers

# print("Welcome to our Calculator")
# fnum=float(input('Enter first number:\t'))
# snum=float(input('Enter second number:\t'))
# while True:
#     print("Select Operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit")
#     op=int(input("Enter your operation choice:\t"))
#     if(op==6):
#         print("Goodbye")
#         break
#     if (op>=7)or(op<=0):
#         print("Wrong operation choice, please choose only 1 to 6")
#         break
#     else:
#         if(op==1):
#             print(f"Result after adding:\t",add(fnum,snum))
#         elif(op==2):
#             print(f"Result after subtracting:\t",sub(fnum,snum))
#         elif(op==3):
#             print(f"Result after multiplying:\t",multi(fnum,snum))
#         elif(op==4):
#             print(f"Result after dividing:\t",div(fnum,snum))
#         elif(op==5):
#             print(f"Average:\t",avg(fnum,snum))

