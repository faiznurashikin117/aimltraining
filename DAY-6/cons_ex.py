class Emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual
   
    def display(self):
        print("ID:\t",self.id)
        print("Name:\t",self.name)
        print("Quali:\t",self.qual)

class Dev(Emp):
    def __init__(self, id, name, qual,domain,project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print('Domain:\t',self.domain)
        print('Project:\t',self.project)

#create one employee object with id=1, name="Sam", qual="MCA"
#create one Development employee object with id=3, name="Ravi", qual="Mtech", project="eShopping", Domain='dot net'
#Display Development employee details
#Display employee details

#Answer:object created
e1=Emp(1,"Sam","MCA")
d1=Dev(3, "Ravi", "Mtech", "eShopping", 'dot net')
#Answer:Display
print("Employee details:\t")
e1.display()
print("Development employee details:\t")
d1.display()
