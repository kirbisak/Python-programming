vocab = {}
temp = []

with open("chatbot.txt", "r") as f:
    for line in f:
        temp.append(line.replace("\n", ""))

for i in range(0, len(temp) - 1):
    vocab.update({temp[i] : temp[i+1]})

while True:
    res = input()
    if res in vocab.keys():
        print(vocab[res])
    elif res == "Dovidenia":
        break
    else:
        print("Nerozumiem ti.")