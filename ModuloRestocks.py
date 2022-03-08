import json
import requests
from bs4 import BeautifulSoup

def Restocks(sku):

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "es-ES,es;q=0.9", 
        "Host": "httpbin.org", 
        "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"", 
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": "\"Windows\"", 
        "Sec-Fetch-Dest": "document", 
        "Sec-Fetch-Mode": "navigate", 
        "Sec-Fetch-Site": "none", 
        "Sec-Fetch-User": "?1", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36", 
        "X-Amzn-Trace-Id": "Root=1-61fef4e2-5ae7466a0bbf3bcb22ae1f4d"
    }

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
        price = (f"{round(int(price[2:])*0.85)} €")
        if(len(tall) <= 2):
            tall = tall + "  "
        liston.append(f"{tall} : {price}")

    return nombreZapa, fotoZapa, liston

    
    #liston = " \n".join(liston)

    #soupPrecios = soupRestocks.find_all("span", class_="")


    # # #Convertir string de precio a float para descontar las comisiones, pasar a int
    # # for i in range(0, len(precios)):
    # #     precios[i] = float(precios[i]) * 0.85
    # #     precios[i] = int(precios[i])



    #Inicializar lista tallas, llenarla con las tallas
    # tallas = list()
    # for i in soupTallas:
    # #     tallas.append(i.text)

    # # #remove duplicates
    # # tallas = list(dict.fromkeys(tallas))
    # # #bucle que si + 4 caracteres lo borra
    # # tallas = [x for x in tallas if len(x) <= 4]

    # # #Imprimir por pantalla la lista de tallas
    # # print("Tallas: ", tallas)


    # # #Presio

    # # #Inicializar lista de precios, añadirlos todos a la lista
    # # precios = list()
    # # for i in soupPrecios:
    # #     precios.append(i.text)


    # # #Borrar precios inutiles, quitar simbolos para convertir el string del precio
    # # del precios[15:]
    # # precios = [s.replace('€ ', '') for s in precios]

    # # #Convertir string de precio a float para descontar las comisiones, pasar a int
    # # for i in range(0, len(precios)):
    # #     precios[i] = float(precios[i]) * 0.85
    # #     precios[i] = int(precios[i])

    # # #Imprimir payouts
    # # print("Payouts:", precios)