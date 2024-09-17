def tobin(n):
    bin = ""
    for element in n:
        if element.isalpha():
            bin += str(1)
        else:
            bin += str(0)
    return bin

def bintodec(n):
    sum = 0
    index = 0
    for element in n[::-1]:
        sum += int(element) * 2 ** index
        index += 1
    return sum

def dectooct(n):
    result = ""
    while n > 0:
        result += str(n % 8)
        n = n // 8
    result += "0"
    return result[::-1]

def main(auth):
    return dectooct(bintodec(tobin(auth)))

print(main("rwxr-x---"))