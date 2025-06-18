#two kind of relationship 
 #one is aggregtion --(Has -A)
 #other is Inheritence (Is -A)
 
#example smartphone is a product...


#AGGREGATION

#we have two class customer and adddress ....between them teh relation is that the customer has a address...toh customer ko adress 
#class chahir toh ye hai aggregation

class Customer:
    def __init__(self, name , gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)
    
class Address:
    def __init__(self , city, pincode , state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state

add = Address("Kolkata", 700156, "WB")  # Fixed the typo here        
cust = Customer("Nitesh", "Male", add)  # Aggregation

# Edit profile with new name and address
cust.edit_profile("Ankit" , "Gurgaon", "122011", "Haryana")

# Print the updated city from the address
print(cust.address.city)

    