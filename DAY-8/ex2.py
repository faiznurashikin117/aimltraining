from ourpack import calc

# fnum=float(input("Enter first number:\t"))
# snum=float(input("Enter the second number:\t"))
# op=input("Choose operation +,-,*,/:\t")

# if (op=="+"):
#     print("Result:\t",calc.add(fnum,snum))
# elif (op=="-"):
#     print("Result:\t",calc.sub(fnum,snum))
# elif (op=="*"):
#     print("Result:\t",calc.multi(fnum,snum)) 
# elif (op=="/"):
#     print("Result:\t",calc.div(fnum,snum)) 
# else:
#     print("Wrong operation Choice")


# #contoh untuk fnum,snum error only
# try:
#     fnum=float(input("Enter first number:\t"))
#     snum=float(input("Enter the second number:\t"))
#     op=input("Choose operation +,-,*,/:\t")
#     if (op=="+"):
#         print("Result:\t",calc.add(fnum,snum))
#     elif (op=="-"):
#         print("Result:\t",calc.sub(fnum,snum))
#     elif (op=="*"):
#         print("Result:\t",calc.multi(fnum,snum)) 
#     elif (op=="/"):
#         print("Result:\t",calc.div(fnum,snum)) 
#     else:
#         print("Wrong operation Choice")
# except Exception as e:
#     print("Error",e)


# #contoh untuk fnum,snum dan op error skli
# try:
#     fnum=float(input("Enter first number:\t"))
#     snum=float(input("Enter the second number:\t"))
#     op=input("Choose operation +,-,*,/:\t")
#     if (op=="+"):
#         print("Result:\t",calc.add(fnum,snum))
#     elif (op=="-"):
#         print("Result:\t",calc.sub(fnum,snum))
#     elif (op=="*"):
#         print("Result:\t",calc.multi(fnum,snum)) 
#     elif (op=="/"):
#         print("Result:\t",calc.div(fnum,snum)) 
#     else:
#         raise ValueError
    
# except ZeroDivisionError as ze:
#     print("Division by 0 not allowed",ze)
# # except ValueError as ve:
# #     print("Error in values",ve)
# except Exception as e:
#     print("Error",e)
# finally:
#     print("End of program")


#contoh untuk fnum,snum dan op error skli dan loop untuk run another operations
while True:
    try:
        fnum=float(input("Enter first number:\t"))
        snum=float(input("Enter the second number:\t"))
        op=input("Choose operation +,-,*,/:\t")
        if (op=="+"):
            print("Result:\t",calc.add(fnum,snum))
        elif (op=="-"):
            print("Result:\t",calc.sub(fnum,snum))
        elif (op=="*"):
            print("Result:\t",calc.multi(fnum,snum)) 
        elif (op=="/"):
            print("Result:\t",calc.div(fnum,snum)) 
        else:
            raise ValueError
        
    except ZeroDivisionError as ze:
        print("Division by 0 not allowed",ze)
    # except ValueError as ve:
    #     print("Error in values",ve)
    except Exception as e:
        print("Error",e)
    choice=input("Press y to continue:").lower()
    if(choice!='y'):
        print("Bye")
        break
