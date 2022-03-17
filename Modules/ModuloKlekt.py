import requests
import json
from bs4 import BeautifulSoup

def Klekt(sku):

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://apiv2.klekt.com',
    }

    json_data = {
        'query': 'query SearchProducts($input: SearchInput!) { search(input: $input) { items { productId slug styleCode categoryNames brandNames brandLineNames productName description variantsCount sameDayShipping sdsPriceWithTaxMin styleCode sizeType conditions { condition } customMappings { ... on CustomProductMappings { featured new } } priceWithTax { ... on PriceRange { min max } } productAsset { id preview } } totalItems }}',
        'variables': {
            'input': {
                'term': sku,
                'sizeType': 0,
                'facetValueIds': [],
                'groupByProduct': True,
                'brandSlugs': [],
                'brandLineSlugs': [],
                'categorySlugs': [],
                'availability': 'available',
                'take': 48,
                'skip': 0,
                'sort': {
                    'featured': 'DESC',
                },
                'showWithoutSizeSet': False,
                'conditions': [
                    'new',
                ],
                'boxConditionSlugs': [],
                'itemConditionSlugs': [],
            },
        },
    }


    response = requests.post('https://apiv2.klekt.com/shop-api/', headers=headers, json=json_data)

    jsonero = json.loads(response.text)
    
    l = jsonero["data"]["search"]["items"][0]["slug"]
    r = requests.get(f"https://www.klekt.com/product/{l}").text

    soup = BeautifulSoup(r,"html.parser")

    links = soup.find(id="__NEXT_DATA__").contents[0]

    jotason = json.loads(links)


    id =jotason["props"]["pageProps"]["productDetails"]["productId"]

    json_data = {
        'query': 'query ProductDetails($productId: ID!) { productDetails(id: $productId) { name id slug description conditions { condition minPrice } featuredAsset { preview } assets { asset { id preview name } position } customFields { new featured styleCode releaseDate } facetValues { code } variants { id customFields { sameDayShipping } availableCount priceWithTax facetValues { code name id facet { code } } } variantsNDD { id customFields { sameDayShipping } availableCount priceWithTax facetValues { code name id facet { code } } } variantsUSED { id price name priceWithTax customFields { sameDayShipping } } }}',
        'variables': {
            'productId': id,
        },
    }

    response = requests.post('https://apiv2.klekt.com/shop-api/', headers=headers, json=json_data)

    res = json.loads(response.text)
    dicty = {}
    for e in res["data"]["productDetails"]["variants"]:
        price = int(int(e["priceWithTax"]) / 100 * 0.85)
        talla = e["facetValues"][0]["name"]

        dicty[float(talla[2:])] = price

    talls = sorted(dicty.keys())
    presios = sorted(dicty.values())
    liston = []
    
    for i in range(len(talls)):
        if(len(str(talls[i])) < 4):
            liston.append(f"US {talls[i]}  : {dicty[talls[i]]} €")
        else:
            liston.append(f"US {talls[i]} : {dicty[talls[i]]} €")
            
    

    linkVenta = "https://www.klekt.com/seller/"+l+"?condition=new"
    return linkVenta, liston