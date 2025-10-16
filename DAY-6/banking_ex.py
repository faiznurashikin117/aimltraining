# class Account:
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self,amount):
#         self.bal+=amount
#         print("Balance after deposit:\t",self.bal)

#     def withdraw(self,amount):
#         if (self.bal>=amount):
#             self.bal-=amount
#             print("Balance after withdraw:\t",self.bal)
#         else:
#             print("Insufficient amount in acc")
#             print("Transaction Failed !!!")

#     def show(self):
#         print(f"Account Holder Name:{self.ac_holder}\nAccount Balance{self.bal}")


# ac1=Account("Sameer",50000)
# ac2=Account("Chang",14000)
# ac1.show()
# ac2.show()

# ac1=Account("Sameer",50000)
# ac1.show()
# w_amount=float(input("Enter amount to withdraw:\t"))
# ac1.withdraw(w_amount)


#Encapsulation sir pnya example

# class Account:
#     def _init_(self,acc_holder,bal):
#         self.holder=acc_holder
#         self.bal=bal
#     def deposit(self,amount):
#         self.bal+=amount
#     def withdraw(self,amount):
#         if(self.bal>=amount):
#             self.bal-=amount
#             print("Balance after withdrawal; ",self.bal)
#         else:
#             print("Insufficient amount in account")
#             print("Transaction failed!")
#     def show(self):
#         print(f"\nAccount holder name: {self.holder}, \naccount balance: {self.bal}")

# # * object *

# ac1=Account("Sameer",50000)
# ac2=Account("Chang",14000)
# ac1.show()
# ac2.show()

# ac3=Account("King",12000)
# ac3.show()
# wamount=float(input("Enter amount to withdraw: "))
# print('\n')
# ac3.withdraw(wamount)

# class Account:
#     def _init_(self,balance,ac_holder):
#         self.bal=balance
#         self.ac_holder=ac_holder
    
#     def get_balance(self):
#         return self.bal

# acc = Account(1000,"Sam")
# acc.=34000


#Encapsulation with loop exercise

class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print("Balance after deposit:\t",self.bal)

    def withdraw(self,amount):
        if (self.bal>=amount):
            self.bal-=amount
            print("Balance after withdraw:\t",self.bal)
        else:
            print("Insufficient amount in acc")
            print("Transaction Failed !!!")

    def show(self):
        print(f"Account Holder Name:{self.ac_holder}\nAccount Balance{self.bal}")


ac=Account("Sam",15000)
ac.show()

while True:
    op=(int(input("Please choose\n 1.Deposit 2.Withdraw 3.Exit\n")))
    if (op==3):
        print("Thank you")
        break
    else:
        if (op==1):
            amount=(int(input("Please insert how much is the amount:\n")))
            ac.deposit(amount)
            break
        if (op==2):
            amount=(int(input("Please insert how much is the amount:\n")))
            ac.withdraw(amount)
            break
        else :
            print ("Choose only option provided")










