# with open('skuska.txt', 'w')as f:
#   sentence = input()
#   f.write(sentence)

def cesar(sentence, posun):
    scypher = ""
    posun = posun % 26
    for element in sentence:
        if int(ord(element)) + posun > 90:
            element = chr(int(ord(element)) + posun - 26)
            scypher += element
        else:
            scypher += chr(int(ord(element)) + posun)
    return scypher

# try:
#   with open('skuska.txt', 'r') as f:
#     obsah = f.read()
#     nieco = int(input("zadaj posun na zakodovanie: "))
#     print(cesar(obsah, nieco))
# except IOError:
#     print("neexistuje subor")

print(cesar("ABC", 22))