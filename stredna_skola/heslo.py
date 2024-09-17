import random, string
def password(n):
    heslo = ""
    for i in range(n):
        k = random.randint(1,3)
        if k == 1:
            heslo += random.choice(string.ascii_letters)
        if k == 2:
            heslo += random.choice(string.digits)
        if k == 3:
            heslo += random.choice(string.punctuation)
    
    return heslo

print(password(10))
        