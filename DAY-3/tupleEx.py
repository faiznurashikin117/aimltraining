# print("We are going to discuss tuple here")
# subjects=("python","java","dotnet","sql","power bi")
# print("\nAll subjects are:\n")
# print("Number of subjects are:",len(subjects))
# for sub in subjects:
#     print(sub,end="\t")


# numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
# print("Total Number in tuple:",len(numbers))
# for num in numbers:
#     print(num,end="\t")

#tupleName.index(item) will return the index of first occurrence of item in tupleName
# search_num=int(input("\nEnter number to find out index:\t"))
# if search_num in numbers:
#     print(f'Index of {search_num} is:\t',numbers.index(search_num))
# else:
#     print(f"No such number {search_num} in our tuple")


#tupleName.count (item): tupleName count (item) will return number of times item occurs in tupleName.
# numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
# print("Total Number in tuple:",len(numbers))
# for num in numbers:
#     print(num,end="\t")
# search_num=int(input("\nEnter number to find out frequency:\t"))
# if search_num in numbers:
#     print(f'Number: {search_num} occurs: {numbers.count(search_num)} times')
# else:
#     print(f"No such number {search_num} in our tuple")



#Write a program to sum a list with 4 numbers
# DessertPrices=[14, 19, 8, 5]
# print('Total cost of desserts bought is:')
DessertPrices=[14, 19, 8, 5,7]
for TotalPrice in DessertPrices:
    print("TotalPrice:",sum(DessertPrices))


# DessertPrices=[14, 19, 8, 5]
# print("TotalPrice:",sum(DessertPrices))


