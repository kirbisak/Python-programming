import os

def BintoDec(n):
  sum = 0
  index = 0
  for element in n[::-1]:
    sum += int(element) * 2 ** index
    index += 1

  return sum 

if not os.path.exists("binary.txt"):
  print("Neexistuje subor")
else:
  with open("binary.txt", "r") as f:
    sum = 0
    k = 0
    for line in f:
      line = line.replace("\n", "")
      sum += BintoDec((line))
      k += 1
    priemer = sum / k
  print(priemer)
  