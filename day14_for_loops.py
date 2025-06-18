#python for loop is different from cpp and java

#general structure

#range function - built in function used to generate integers in a given range
#you give start and end in the function 
#if u give only one number then it is considered that  it is the end number strating from 0


ans =list(range(1,11))
print (ans)


#step

babu =list(range(1,11,2))
print (babu)
#here third argument is the jump u want in the range


#Sequence --order #example is string - sequence of character
#tuples ,sets , dictionary are also sequence


#for loop in python iterate over sequence or range function


for i in range(21,11, -1):
    print(i)


for i in "kolkata":
    print(i)



for i in [1,2,3]:
    print(i)



#agr pata hai ki loop kitne number of times chlega toh use for loop else use while loop




