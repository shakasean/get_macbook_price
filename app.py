from bs4 import BeautifulSoup
import requests

req = requests.get("http://www.apple.com/shop/buy-mac/macbook-pro")
content = req.content

soup = BeautifulSoup(content,"html.parser")

model_size = soup.findAll("span", {"class":"as-macbundle-modelsize"})
specs = soup.findAll("h3", {"class":"as-macbundle-modelvariationtitle"})
price = soup.findAll("span", {"itemprop":"price"})

for i in range(len(price)):
    print(model_size[i].text.strip() + " - " + specs[i].text.strip() + " - " + price[i].text.strip())

