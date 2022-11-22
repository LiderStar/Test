import re
import requests
import lxml
import json
from bs4 import BeautifulSoup as bs

# url = "https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0"
# header = {
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }
# req = requests.get(url=url,headers=header)
# with open("wiki.html", "w", encoding='utf-8') as file:
#     print(req.text, file=file)

with open("wiki.html", encoding="utf-8") as file:
    soup = bs(file, "lxml")
    # id_n = soup.find_all("p")
    # id_n = soup.find_all( re.compile("^a")) 
    # id_n = soup.find_all(re.compile(".+href.+")) 
    id_n = soup.find("a", class_= (re.compile(".+jump.+"))).text
    tl = soup.find("title").text
    hr = soup.find_all("a")
    for item in hr:
        print(item.get("href"))
    dv = soup.find_all("div", class_="floatright")
    
    # for item in soup.find_all(href = re.compile("wikiped")):
    #     print(item)

    # ls = soup.find_all(["nav", "h3"])
    
    # print(ls)
    # print(id_n)
    # print(hr)
    print(tl)
    # print(dv)