# numbers=[10,25,30,40,2,1]
# double_num=list(map(lambda x:2*x,numbers))
# print('Original List')
# for num in numbers:
#     print(num,end=" ")

# even_numbers=list(filter(lambda x: x%2==0, numbers))

# print("\nEven Numbers from list as follows\n")
# for num in even_numbers:
#     print(num,end=" ")

# #you have following list
# our_list=[4,2,5,6,7,3,1,10]
# #write code using filter to find out all the number less than 5
# print("Original list")
# for thelist in our_list:
#     print(thelist,end="\t")

# newlist=list(filter(lambda x:x<5,our_list))
# print("\nNumbers less than 5 is:")
# for num in newlist:
#     print(num,end="\t")


students_marks={"Sam":60,"Raj":55,"Mihir":35,"Sandy":45,"Niraj":76,"Deep":40,"Garima":54}

# print("All students")
# for k,v in students_marks.items():
#     print(f'Name:{k}-. Marks {v}')

pass_students=dict(filter(lambda x:x[1]>=50,students_marks.items()))

print("Passed Students")
for k,v in pass_students.items():
    print(f'Name:{k}-. Marks {v}')

sort_pass_students=dict(sorted(pass_students.items(),key=lambda x:x[1]))
print("Ascending Order")
print(sort_pass_students)
sort_pass_students_desc=sorted(pass_students.items(), key=lambda x:x[1],reverse=True)
print('Descending Order')
print(sort_pass_students_desc)


# print(students_marks)
# print(pass_students)