#list -- A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements
# difference between array and list 
  # array is homogeneous....list can be heterogeneous
  # array is contagious ...list is not contagious
  # array are much faster 
  # lists are more programmer friendly 


#creating list in python 
listz = [] #empty list

list1 = [1,2,3,4,5]
print(list1)

list2 = [1,2,3,4,'helo']
print(list2)

# multidimensional list 
 #2D
list3 =[1 , 2 ,3 , [2 , 3]]
print(list3)



print(list("haldia"))


#access item from a lsit
print(list3[0])


#add item in a list 
 #append - adds the element in the end of the list
 #extend - adds multiple elements in the end of the list
 #insert - add at desired position
l =[100 , 200 , 300 , 400]
l.append(1000)
print(l)
l.append('hello')
print(l)



l.extend([5000,6000,8000])
print(l)
l.append([5,2])
print(l)

l.extend('goa')
print(l)

l.insert(1 , 'world')
print(l)


#delete in an list
 #del - deletes the entire list  del l  ..if want index based del l[0]
 #remove - we dont know the index but we know our element---- l.remove('hello')
 #pop - deletes the last element in the list --- l.pop()
 #clear -- instead of deleting it empties the list



#operation that are present with list

l = [1 , 2 ,3]
l1= [5 , 6,7,8]
print(l+l1)
print(l*3)

#functions that are present on list

print(len(l)) #tells the length of the list
print(min(l))
print(max(l))
print(sorted(l))
print(sorted(l , reverse=True)) #changes made using sorted functions are temporary they are not permanent

print(l.sort()) #sort and these changes are permanent
