# 12:34:56:78:9A:BC

def hex_to_dec(num):
    index = 0
    sum = 0
    for element in num[::-1]:
        if element.isalpha():
            element = ord(element) - 55
        sum += int(element) * 16 ** index
        index += 1
    return sum

def dec_to_bin(num):
    lst = ""
    while num > 0:
        lst += str(num % 2)
        num = num // 2
    return lst[::-1]

# print(dec_to_bin(hex_to_dec("A7")))

def mac_adresa(adress):
    lstDec = []
    lstBin = ""
    adress = adress.split(":")
    for element in adress:
        lstDec.append(hex_to_dec(element))

    for element in lstDec:
        lstBin += (dec_to_bin(element))
    return lstBin

# def mac_adresa(adress):
#     result = ""
#     adress = adress.split(":")
#     for element in adress:
#         result += dec_to_bin(hex_to_dec(element))
#     return result


print(mac_adresa("12:34:56:78:9A:BC"))