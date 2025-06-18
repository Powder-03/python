#example - banking me users ke transaction ke lie ......ek loop chlega har user ke lie doosra chlega sare transaction ke lie

rows= int(input("number of rows"))

for i in range(1,rows+1):
    for j in range(0 , i):
        print("*", end=" ")
    print(" ")
