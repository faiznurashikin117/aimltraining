#take user marks from user within 1-50
#if user enter outside [0-50] raise Error InvalidMarks using Custom Exception
#Give chance to user till, he'she entered valid marks

from ourpack import markexc

while True:        
    try:
        usermark=int(input("Enter your mark:\t"))
        markexc.check_Mark(usermark)
    except markexc.InvalidMark as e:
        print("Invalid mark:\t",e)
    except Exception as ex:
        print("Error!!!",ex)
    else:
        print("Recorded")
    choice=input("Press y to continue key-in the mark:").lower()
    if(choice!='y'):
        print("Ciao")
        break