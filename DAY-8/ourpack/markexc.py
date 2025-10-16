class InvalidMark(Exception):
    pass

def check_Mark(mark):
    if (mark<=0):
        raise InvalidMark("Mark should not be negative")
    elif (mark>=50):
        raise InvalidMark("Mark should not be more than 50")
    else:
        print(f"The {mark} is accepted and valid")