import random
jackpot = random.randint(1 ,100) #it can generate numbers in the range [a,b] including a and b
guess = int(input("chal guess kr"))
while guess != jackpot:
    if guess > jackpot:
        print("guess lower")
    else:
        print("guess higher")
    guess = int(input("chal guess kr"))
print("sahi jawab")

