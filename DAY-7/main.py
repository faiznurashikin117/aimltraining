from ourpack import welcome
name=input("Enter your name:\t")
welcome.display(name)
msg=welcome.display(name)
print(msg)


from ourpack import student
s1=student.Student(1,"Ravi")
s1.print_info()