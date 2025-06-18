#operators are used to perform operations on variables and values 

#arithmatic operators

x=5
y=2
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x%y)
print(x**y)#this is powerof operator
print(x//2)#this is called true division it converts the float value or any value to integer value


# logical operators

x=False
y = True
print(x or y)
print(x and y)
print (not y)


#bitwise operator

x=2
y=3

print(x & y)  #here & is bitwise operator
print( x| y)
print(x>>2)
print(~3) 


#assignment operator

a=3 #here = is assignment operator
print(a)

#in python a++ and ++a does not work    agr value badhana h toh a+=1 or a=a+1 use krna hoga

a=3
b=3
print(a is b) #return true or false....when a and b both are stored at same memory location it returns true otherwise it stores false


#membership operator ........ye batata hai ki koi cheej kisi ke ander h ki nhi

x= 'DELHI'
print("D" in x) #returns true because D is present in delhi 

print ("D " not in x) # returns false

x =(1,2,3)
print(5 in x) #returns false because 5 is not present in this list


