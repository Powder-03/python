#dictionary
print({"name": "nitesh" , "gender":"male"})

#dictionary has no indexing
# dictionary is a mutable type
# keys-> immutable , values-> they can be mutable

# keys should be unique

#mutable data types are - lists/sets/dictionary
#immutable-> strings/ tuples/int/ float/boolean/complex

#create 
D={}  #empty dictionary
print(D)

p ={"name": "nitesh" , "gender":"male"}
print(p)
# keys should be immutable

d ={"name": "nitesh" , "name":"male"} # keys should be unique the recent value is our answer
print(d)

#acessing item from an dictionary
#cannot access like array with index we use key for finding the value
print(p["gender"])


#edit 
d["name"]="rahul"
print(d)

# add new key value pairs

d["age"]= 23
print(d)

# delete

del d 
print(d)