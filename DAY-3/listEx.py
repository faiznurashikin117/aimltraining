# print("List Example One")

# my_list=[10,20,30,"Python",None,True,12.45,'Ravi']
# print('Number of items in list are:',len(my_list))
# for item in my_list:
#     print(item)

# print("Second example of list")
emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of employees:",len(emps))
# print('All employees')
# for emp in emps:
#     print(emp,end=" ")


#Sort Example
#listName.sort()

# emps.sort()
# print("List after sorting")
# for e in emps:
#     print(e,end=" ")


# emps.reverse()
# print ("Employees in descending order")
# for e in emps:
#     print(e,end=" ")


#append, remove, pop insert method

# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of employees:",len(emps))
# for emp in emps:
#     print(emp,end="\t")

#     #append:adds the item at the end of the list
# newEmp=input("\nEnter employee name to add in list ")
# emps.append(newEmp)
# print("\nAfter adding New Employee:Number of employees are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")
    

#insert(index,item): This will add item at given index
# newEmp=input("\nEnter employee name to add in list:\t ")
# pos=int(input("Enter position where you want to add in the list:\t"))
# emps.insert(pos,newEmp)
# print("\nAfter adding New Employee:Number of employees are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")


#listName.remove(item): Will remove item from the list
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of employees:",len(emps))
# print('All employees')
# for emp in emps:
#     print(emp,end=" ")

# delEmp=input("\nEmployee to remove from the list:\t ")
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of employees after deleting {delEmp} in list are:\t",len(emps))
#     for emp in emps:
#         print(emp,end=" ")
# else:
#     print(f"No such item {delEmp} in employee list")


# POP() example
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of employees:",len(emps))
# print('All employees')
# for emp in emps:
#     print(emp,end=" ")
# #listName.pop(index): Will delete element at index 2 and return its value.
# del_index=int(input("\nEnter Index to pop item:\t"))-1
# print('Pop Result: ',emps.pop(del_index))

# print("Number of employees after pop() are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")


# #find out first and last element from the list
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of employees:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

# print('\n First Element of employee list is:',emps[0])
# print('\n Last Element of employee list is:',emps[-1])
# print('\n Second Last Element of employee list is:',emps[-2])
