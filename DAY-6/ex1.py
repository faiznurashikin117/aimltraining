# class Player:
#     def __init__(self):
#         print("Welcome to Player Class")

#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f'Id:{self.id}\t Name:{self.name}\tTeam:{self.team}')

# #object creation
# p1=Player()
# p2=Player()
# p3=Player()
# p1.reg(1,"MSD","India")
# p2.reg(2,"R.Khan","Afghanistan")
# p3.reg(3,"Moin Ali","England")

# p1.display()
# p2.display()
# p3.display()


#Example 2 (Parameterized constructor)

class Player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    # def display(self):
    #     print(f'Id:{self.id}\t Name:{self.name}\tTeam:{self.team}')

#method 1
    def display(self):
        print(f"{self.id}\t{self.name}\t{self.team}")
#method 2
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.team}"

#object creation
p1=Player(1,"MSD","India")
p2=Player(2,"R.Khan","Afghanistan")
p3=Player(3,"Moin Ali","England")

#displaying first player details using method from def display
p1.display()
p2.display()
p3.display()

#displaying first player details using method from def display
# print(p1)
# print(p2)
# print(p3)