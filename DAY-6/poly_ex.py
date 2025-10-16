# class Bird:
#     def fly(self):
#         print("Bird can fly")

# class Airplane(Bird):
#     def fly(self):
#         print("Airplane fly")

# b=Bird()
# print("Bird Implement")
# b.fly()

# print("Airplane Implement")
# a=Airplane()
# a.fly()
# print("Using for loop")

# for obj in [Bird(),Airplane()]:
#     obj.fly()


#Example 2

class Emp:
    def reg(self):
        self.id=int(input("Enter id:\t"))
        self.name=input("Enter name:\t")

    def disp(self):
        print("Name:\t",self.name)
        print("ID:\t",self.id)

class Dev(Emp):
    def reg(self):
        super().reg()
        self.domain=input("Enter Domain:\t")

    def disp(self):
        super().disp()
        print("Domain:\t",self.domain)

d1=Dev()
d1.reg()
d1.disp()