# print("First example \n")
# for i in range(10):
#     print(i)
#     print("welcome")

# print("Second example")
# for i in range (1,11):
#     print(i)

# print("Third example")
# for i in range(10):
#     print(i+1)
    
# for item in range(100):
#     print(item+1,end=" ")


# for item in range(10):
#     print(item+1,end="\t")

# for item in range(5):
#     print(item+1,end="\n")

# employees=['Raj', 'Ravi','Sam','Anu','Ri']
# for e in employees:
#     print(e)


# products=['Facewash','Sunscream','Facial kit','Lip glos', 'Lip Balm', 'Hair oil']
# for item in products:
#     print(item)


# for ch in 'Nexperts Academy':
#     print(ch)

# for ch in 'Nexperts Academy':
#     print(ch,end=" ")

# name=input("Enter your name: \t")
# print("Characters of your name is as follows: \n")
# for ch in name:
#     print(ch)

num=int(input("Please enter number to find out table: \t"))
print(f'Table of Number {num} as follows \n')
for i in range (1,11):
    print(f'{num}*{i}=\t{num*i}')


#A tuple is an immutable data type in python.
#One example of tuple using for loop

# players=("fawwaz","fateh","furqan","faizal")
# for player in players:
#     print(player)

players=("fawwaz","fateh","furqan","faizal")
for player in players:
    print(player[2]) 

# players=("fawwaz","fateh","furqan","faizal")
# for player in players:
#     print(player,end=" ") 