class Emp:
    def display(self):
        print("Display of Employee Class")

obj = Emp()
obj.display()

#class className:
    #definition of class
    #attribute Method, constructors

#objectName=ClassName()
#objectnName.MethodName()

e = Emp()
e.display()

#Second Example
class Emp:
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print("Employee details as follows")
        print("Employee Id:",self.eid)
        print("Employee Name:",self.ename)

e1 = Emp()
e2 = Emp()
e3 = Emp()
e1.registr(1,"Sam")
e2.registr(102,"Neha")
e3.registr(103,"Jai")
print("First Employee details")
e1.display()
print("Second Employee details")
e2.display()
print("Third Employee details")
e3.display()
