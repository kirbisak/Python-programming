from bs4 import BeautifulSoup
import requests

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tag = doc.find_all("p")[0]

# print(tag.find_all("b "))

# url = "https://www.newegg.com/msi-rtx-3060-ventus-2x-12g-oc-nvidia-geforce-rtx-3060-12gb-gddr6/p/N82E16814137632"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(string="$")
# parent = prices[0].parent
# strong = parent.find("strong")

# print(strong.string)

from bs4 import BeautifulSoup

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

doc = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', "html.parser")
tag = doc.p

# print(tag['class'])
print(doc.string)
# print(doc)