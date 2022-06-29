import json
import requests
from bs4 import BeautifulSoup

def Restocks(sku):

    #Request que busca la zapatilla y devuelve un json, cargarlo a un diccionario
    restocksBuscar = requests.get('https://restocks.net/es/shop/search?q='+sku+'&page=1&filters[0][range][price][gte]=1&options[getAllPages]=0')
    jsonBusqueda = json.loads(restocksBuscar.text)

    #Pillar el link de json de la request
    jsonBusqueda['data']
    for i in jsonBusqueda['data']:
        link = (i['slug'])
        fotoZapa = (i['image'])
        nombreZapa = (i['name'])

    #Con el link sacado arriba, sacar todo el html de la zapatilla
    restocks = requests.get(link)
    soupRestocks = BeautifulSoup(restocks.content, 'html.parser')

    #Filtrar tallas y precios del html
    soupTallas = soupRestocks.find("ul",class_="select__size__list")


    all = soupTallas.find_all("li",{"class" : "", "data-type" : "all"})
    liston = []
    for i in all:
        tall = i.find("span",class_="text").text
        price = i.find("span",class_="").text
        price = f"{round((int(price[2:].replace('.',''))-10)*0.9)} €"
        if(len(tall) <= 2):
            tall = tall + "  "
        liston.append(f"{tall} : {price}")

    return nombreZapa, fotoZapa, liston