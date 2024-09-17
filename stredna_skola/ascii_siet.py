import os

def dectobin(num):
    res = ""
    while num > 0:
        res += str(int(num) % 2)
        num = num // 2
    return res

def main(n):
    output = ""
    for element in n:
        temp = dectobin(ord(element))
        while len(temp) < 8:
            temp += str(0)
        output += temp[::-1]
        temp = ""
        
    return output

if not os.path.exists("sprava.txt"):
    print("subor neexistuje")
else:
    with open("sprava.txt", "r") as f:
        for line in f:
            print(main(line))