from typing import OrderedDict
import requests
import json
from bs4 import BeautifulSoup

def prettyPrices(i,j):
    str =""

    if len(i) < 4:
        str = str + f"{i}   : {j}"
    elif len(i) <= 5: 
        str = str + f"{i}  : {j}"
    elif len(i) <=6:
        str = str + f"{i} : {j}"
    else:
        str = str + f"{i}: {j}"
    return str

def Alias(id):

    aliasbuscar = requests.get(f"https://www.goat.com/search?query={id}")

    soupp = BeautifulSoup(aliasbuscar.content, "html.parser")
    div = soupp.find('div', {"id":"grid-body"})
    ass = div.find_all("a")
    for a in ass:
        ss = a["href"]
        if id.lower() in ss.lower() and "/sneakers/" in ss.lower() :
            ss = ss.replace("/sneakers/","")
            break
    list = []
    busc = requests.get(f"https://sell-api.goat.com/api/v1/analytics/products/{ss}/availability")
    if busc.status_code == 200:
        data_json = json.loads(busc.content)
        for a in data_json["availability"]:
            if "lowest_price_cents" in a:
                s = a["size"]
                size = str(f"US {s}")
                price = int(a["lowest_price_cents"])/100
                print(len(size))
                list.append(prettyPrices(size,price))
                
    print(list)            
    return list

Alias('DD1875-100')