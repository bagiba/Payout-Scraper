import json
from bs4 import BeautifulSoup
import cloudscraper

#sku = "DD1391-100"
def WeTheNew(sku):

    cookies = { "slrspc_token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImNvbW11bmlzbXBvd2FoQGdtYWlsLmNvbSIsImZpcnN0bmFtZSI6Ikp1YW4iLCJsYXN0bmFtZSI6Ik1lbmVuZGV6IiwiaWF0IjoxNjU2NDUxMzI1LCJleHAiOjE2NjE2MzUzMjV9.UEOuranCfDptj1yKDxr-DmWwAreOKoKqbDVDAT0-uCk"}

    #Request que busca la zapatilla y devuelve un json, cargarlo a un diccionario
    scraper = cloudscraper.create_scraper(browser="chrome")
    weTheNewBuscar = scraper.get('https://sell.wethenew.com/api/products?skip=0&take=100&keywordSearch='+sku)


    jsonBusqueda = json.loads(weTheNewBuscar.text)

    #Pillar el id del json de la request
    jsonBusqueda['results']
    for i in jsonBusqueda['results']:
        id = (i['id'])

    linkVenta = "https://sell.wethenew.com/listing/product/"+str(id)
    resultadoIDs = scraper.get(linkVenta, cookies=cookies)
    soupIDs = BeautifulSoup(resultadoIDs.text, 'html.parser')



    all = soupIDs.find("ul", class_ = "VariantsList_VariantsListSquare__f2Ivd")
    IDs = all.find_all("li")
    listonIDs = []
    listonTallas = []
    liston = []
    for i in IDs:
        listonIDs.append(i.get("id"))
        listonTallas.append(i.text.replace("WTB", ""))
        #if(len(i.text) <= 2):
        #    i = i + "  "

    listonPrecios = []
    for i in listonIDs:
        requestChetada = scraper.get("https://sell.wethenew.com/api/listings/cheapest?variantIds[]="+i, cookies=cookies)
        listonPrecios.append(requestChetada.json())

    for i in range(len(listonPrecios)):
        preciada = listonPrecios[i][0]["price"]
        tallada = listonTallas[i]
        liston.append(f"{tallada} : {preciada}")
    
    return linkVenta, liston