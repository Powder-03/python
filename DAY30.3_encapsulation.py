# instance variable -- jo bhi variables aap constructor ke ander bnate unhe instance variable khte hai ...
#kyuki in variables ki value har object kee lie alag hota hai 
# jab aap class bnate ho toh its not a good practice ki aap apne data ko open chhod do
#in python we dont have access modifier as private or public ....so for making any varible private we just add two underscore before its name
# nothing in python is fully private
#suppose balance variable is hidden but you can see it using the command sbi._Atm__balance

# Encapsulation is the bundling of data with the methods that operate on that data.
# It restricts direct access to some of an object's components, which can prevent the accidental modification of data.
# In Python, encapsulation is achieved by using private variables and methods, which are prefixed with double underscores (__).
# Example of encapsulation in a simple ATM class
# This ATM class encapsulates the pin and balance attributes, providing methods to interact with them.
# jjab bhi aap __pin ya __balance likhte ho toh python automatically inhe _Atm__pin ya _Atm__balance me convert kar deta hai



class Atm:
    def __init__(self): 

        self.__pin=""
        self.__balance= 0

        self.menu()
    
    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("pin changed")
    
    def menu(self):
        while True:
            user_input = input("""
                        Hello , how would you like to proceed?
                        1.Enter 1 to create pin
                        2.Enter 2 to deposit
                        3.Enter 3 to withdraw
                        4.Enter 4 to check balance
                        5.Enter 5 to exit
                        
""" )
            if user_input =="1":
                self.create_pin()
            elif user_input =="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input =="4":
                self.check_balance()
            elif user_input =="5":
                print("bye")
                break
            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        self.__pin= input("enter your pin: ")
        print("Pin set successfully")

    def deposit(self):
        temp = input("enter your pin: ")
        if temp == self.__pin:
            amount = int(input("enter the amount: "))
            self.__balance = self.__balance + amount
            print("deposit successful")
        else: 
            print("invalid pin")
    
    def withdraw(self):
        temp = input("enter your pin: ")
        if temp == self.__pin:
            amount = int(input("enter the amount: "))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("operation successful")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")
    
    def check_balance(self):
        temp = input("enter your pin: ")
        if temp== self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")



# apne data ka seedha access ni denge . agr need h toh mere methods ke through hi access karenge , mere method se hi get krenge aur mere method se hi set


# object create krte time aap object ko jis variable me store krte ho us variable ko khte h refrence variable



#refrence variable 
#agr function me pass kia hai object ko ...aur function me object ko edit kia hai toh real me jo bahar iobject hai wo bhi edit ho jaiga
#class ke objects are also mutable like lists dictionary and sets


# there are two methods getter and setter that are used to access and modify private variables
# getter is used to access the private variable
# setter is used to modify the private variable


# pASS BY REFRENCE  - 
