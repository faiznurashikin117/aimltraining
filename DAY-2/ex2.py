# #while loop
# num=1
# print('Printing numbers from 1 to 100')
# while(num<=100):
#     print(num,end=" ")
#     num+=1


# #while loop
# num=3
# print('Printing numbers from 1 to 100')
# while(num<=100):
#     print(num,end=" ")
#     num+=5   


#BREAK EXAMPLE 
num=1
print('Print Numbers from 1 to 100 before we get the number divisible by 11')
while(num<=100):
    if(num%11==0):
        break
    print(num,end=" ")
    num+=1

#Continue EXAMPLE 
num=1
print('Print Numbers from 1 to 100 those are not divisible by 11')
while(num<=100):
    if(num%11==0):
        num+=1
        continue
    print(num,end=" ")
    num+=1

#Continue EXAMPLE 
# print("Odd Numbers from 1 to 100")
# num=1
# while(num<=100):
#     if(num%5==0):
#         num+=2
#         continue
#     print(num,end=" ")
#     num+=1


# for i in range(1,100):
#     if (i%5==0):
#         continue
#     print(i,end="\t")


#WHILE loop to keep the user able to try another password, that's the loop. 
# the unexpected condition is we never know how mny times incorrect pssword
# correctPwd='sam@1256'

# while True:
#     pwd=input('Enter Password to start the game:\t')
#     if(correctPwd==pwd):
#         print('Permission granted')
#         break
#     else:
#         print('Wrong password, Try again!')        
# print('***Game Started!!!***')


#if want to limit wrong attempt
correctPwd='sam@1256'
counter=0
while True:
    pwd=input('Enter Password to start the game:\t')
    if(correctPwd==pwd):
        print('Permission granted')
        break
    else:
        print('Wrong password, Try again!')
        counter+=1
        if(counter>=3):
            print('Blocked for further attempts')
            break