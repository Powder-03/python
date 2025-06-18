# decision control statement
 

# correct email - campusx@gmail.com
# password - 1234
email = input("Apna email batao: ")  # Assign user input to the email variable
password = input("Apna password bhi bata: ")  # Assign user input to the password variable

if email == "campusx@gmail.com" and password == "1234":
    print("Welcome!")
else:
    print("Incorrect credentials")


# now we create program if we write the password wrong then it will give another try for password 

#else if is written as elif in python



email = input("Enter email: ")
password = input("Enter password: ")

if email == "campusx@gmail.com" and password == "1234":
    print("Welcome")
elif email == "campusx@gmail.com" and password != "1234":
    print("Password incorrect")
    password = input("Password phirse bol: ")
    if password == "1234":
        print("Finally correct")
    else:
        print("Still incorrect")
else:
    print("Incorrect credentials")
