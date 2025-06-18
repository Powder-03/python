class Fraction:
    def __init__(self , n ,d):# constructor
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num , self.den)
    
    def __add__(self , other): #self is fraction and other is other fraction 
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num , temp_den)
    
    
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num , temp_den)
    
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num , temp_den)
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num

        return "{}/{}".format(temp_num , temp_den)
    

# magic method __str__ ye automatically call hota hai jab bhi aap class ke object ko print me daalte
# magic method __add__ ye method tab trigger hota hai jabbhi koi do object ke beech me plus aata toh python automatically aapke code me jake 
#__add__ wle function ko khojta hai

x= Fraction(4,5)
y = Fraction(5,6)
print(x+y)
print(type(x))