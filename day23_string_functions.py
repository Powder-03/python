# common functions 1. len 2.max 3.min 4.sorted

c ="kolkata"
print(len(c)) #len func. gives the length of string

print(max(c)) #max returns the element having maximum ascii value in the string
print(sorted(c)) #return the string in ascending order

# capitalise make the first element of ur string to capital
print(c.capitalize()) #but it does not change the original sting

print(c.upper())
print(c.lower())

print("kolKata".swapcase())

#count fn tells the count of substrings in a string
print("it is rainging".count("ing"))


# find function tells the first occurence of a element in the string
print("it is raninign".find("t"))
print("it is raninign".find("in"))

#
print("it is raninign".endswith("gn"))


#format -- we use jab hm phle se pta ni ho ki kya input dena hai toh ye use krlo

print("hello my name is {} and i am {}".format("nitish" , 30))

# split  -- important 
#converts the string to list

print("who is the pm of india".split())
print("who is the pm of india".split("i"))


#join -- convert list to string

print(" ".join(['who' ,'is' , 'the']))
print("-".join(['who' ,'is' , 'the']))


#strip -- clears the trailing and leading spaces
name ="        nitish              "
print(name)

print(name.strip())


