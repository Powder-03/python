class Atm:
    def __init__(self): #jab bhi class me variable declare krte wo def init self se krte
        # here init is a constructor....constructor is a special method jiske ander ka code execute hota hai 
        #jaise hi us class ka obk=jet bnate hai


        #constructor init is a magic method....agar kisi method ke aage aur peeche double underscore ho to magic method hota h
        #magic method is special method jo apne aap trigger hota haik 


        #constructor is something jiska control user ke pass nhi hai ye chalne lgta hai jabbhi app open hota hai ....constructor start hota hai
        #constructor ke ander configuration related task hote hai jo user se ni puchte
        #Static /Class variable is a variable jiska value har object ke lie same hota hai
        #instance variable ko use krne ko self ka use krte aur 
        # static ke lie class ka name use krte
        
        
        
        self.pin=""
        self.balance= 0

        self.menu()
    
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
            elif user_input == "5":
                print("bye")
                break
            else:
                print("Invalid option. Please try again.")


    def create_pin(self):
        self.pin= input("enter your pin")
        print("Pin set successfully")


    def deposit(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            self.balance = self.balance + amount
            print("deposit successful")
        else: 
            print("invalid pin")
    
    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("operation successful")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")
    

    def check_balance(self):
        temp = input("enter your pin")
        if temp== self.pin:
            print(self.balance)
            print("balance checked successfully")
        else:
            print("invalid pin")
 






olay= Atm()   #calling the class


#jis object pe kaam kr rhe whi self hota hai
#self exist because ...ek class ko call krne ko object ki need hoti hai ...aur ek method doosre method ko access ni kr pata ...
#but bht sare scenario aainge jab ek method ko doosre method se intract krna hoga tab ...tab "self " as a object krke methods ko access krte


