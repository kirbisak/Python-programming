import random
# list1 = [random.randint(1, 10) for i in range(10)]

# def sorting(lst):
#     for i in range(0, len(lst)-1):
#         minpos = i
#         for j in range(i, len(lst)):
#             if lst[j] < lst[minpos]:
#                 lst[j], lst[minpos] = lst[minpos], lst[j]
#     return lst
# print(sorting(list1))
# def median(n):
#     if len(n) % 2 == 0:
#         median = (n[len(n) // 2] + n[(len(n) // 2 ) - 1]) / 2
#     elif len(n) % 2 != 0:
#         median = n[len(n) // 2]
#     return(median)


def median():
    list2 = []

    while True:
        num = int(input("Zadaj cislo (ukonci nulou): "))
        if num == 0:
            break
        else:
            list2.append(num)

    for i in range(len(list2)-1):
        if list2[i] > list2[i+1]:
            sorted = False
            break
        else:
            sorted = True
    
    if sorted == False:
        print("konecna")
   
   
    else:
        if len(list2) % 2 == 0:
            median = (list2[len(list2) // 2] + list2[(len(list2) // 2 ) - 1]) / 2
        elif len(list2) % 2 != 0:
            median = list2[len(list2) // 2]
    
    print(f"median je {median}")
        

median()
