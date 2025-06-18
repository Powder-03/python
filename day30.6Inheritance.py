# the benefit of inheritance is that it provides code reusability
#inheritance hmesha oopar ki direction me hota hai
# when you inherit you inherit all the ...data members....constructor....methods or member function
#you cannot inhrit private members

class User:
    def login(self):
        print("login")
        
    def register(self):
        print("register")
        
class Student(User): #showing student class is subclass of user class
    def enroll(self):
        print("enroll")
        
    def review(self):
        print("review")
        
        
stu1= User()
stu1.login

