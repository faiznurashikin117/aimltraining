#Write a function to check a number is odd or even
def check_odd_even(number):
    if(number%2==0):
        print(f"{number}is even")
    else:
        print(f"{number} is odd")

number=int(input("Enter number:\t"))
check_odd_even(number)