
from operator import invert
from pydoc import plain
from typing import List


def skuska():
    list2D = [[0 for j in range(4)] for i in range(3)]
    for i in range (3):
        new = []
        for j in range(4):
            new.append(i * j)
        list2D.append(new)


# def is_face_on_photo(photo: List[List[str]]):
#     for i in range(3):
#         if "f" in photo[i]:
#             print("in", i)
#             break
#         else:
#             print("not in", i)

def is_face_on_photo(photo: List[List[str]]):
    count = 0
    wanted = ["f", "a", "c", "e"]
    new_list = []
    for i in range(len(photo)): new_list.extend(photo[i])
    for i in range(len(wanted)):
        if wanted[i] in new_list:
            return True
        else:
            return False
    count = 0
    for e in new_list:
        if e == "x":
            count += 1
        else:
            count = 0
            return True
        # if e == "x":
        #     count += 1
        #     print(count)
        # else:
        #     print("je tam", wanted)


# print(is_face_on_photo([['f', 'a', 'c', 'e']]))# print(list2D)


def encode(n: int, plain_text: str) -> str: # vraci ciphertext typu String 
    split_plain_text = [(plain_text[i:i+n]) for i in range(0, len(plain_text), n)]
    split_invert = [e[::-1] for e in split_plain_text]
    return "".join(split_invert)






def decode(n: int, plain_text: str) -> str: # vraci ciphertext typu String
    split_plain_text = [(plain_text[i:i+n]) for i in range(0, len(plain_text), n)]
    split_invert = [e[::-1] for e in split_plain_text]
    return "".join(split_invert)

