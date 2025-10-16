#take user marks from user within 1-50
#if user enter outside [0-50] raise Error InvalidMarks using Custom Exception
#Give chance to user till, he'she entered valid marks

class InvalidMark(Exception):
    pass

def check_Mark(mark):
    if (mark<=0):
        raise InvalidMark("Mark should not be negative")
    elif (mark>=50):
        raise InvalidMark("Mark should not be more than 50")
    else:
        print(f"The {mark} is accepted and valid")

while True:        
    try:
        usermark=int(input("Enter your mark:\t"))
        check_Mark(usermark)
    except InvalidMark as e:
        print("Invalid mark:\t",e)
    except Exception as ex:
        print("Error!!!",ex)
    else:
        print("Recorded")
    choice=input("Press y to continue key-in the mark:").lower()
    if(choice!='y'):
        print("Ciao")
        break

    