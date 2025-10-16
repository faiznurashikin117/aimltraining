class InvalidAge(Exception):
    pass

def check_age(age):
    if (age<=0):
        raise InvalidAge("Age should not be negative")
    elif (age<=18):
        raise InvalidAge ("Age should be greater than 18 years")
    elif (age>=150):
        raise InvalidAge ("Unrealistic age")
    else:
        print(f"Age {age} is accepted and valid age for employment")
    
try:

    userage=int(input("Enter your age:\t"))
    check_age(userage)
except InvalidAge as e:
    print("Invalid age:\t",e)
except Exception as ex:
    print("Error!!!",ex)