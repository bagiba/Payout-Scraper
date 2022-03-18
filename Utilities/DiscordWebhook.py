
import requests

def MandarWebhook(linkFoto, nombreSneaker, pid, listaRestocks, listaKlekt, linkVenderKlekt, listaAlias):

    preciosRestocks = " \n".join(listaRestocks)
    preciosKlekt = " \n".join(listaKlekt)
    preciosAlias = " \n".join(listaAlias)
    url = "https://discord.com/api/webhooks/950411947243896843/HpL4SsU-JJNcOKWn4ZnyiC4nAq9SPStnpzr3yAzVTHp1yJMeRLXO6w6VZmELYqz_7FBO"

    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "username" : "Payout Scraper",
        "avatar_url" : "https://pbs.twimg.com/profile_images/1436701160505843715/WGvKZ70-_400x400.jpg"
    }

    #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
    data["embeds"] = [
        {
            "title" : nombreSneaker + " " + "(" + pid +")",
            "thumbnail": {"url": linkFoto},
            "footer": {"text": "Provided by cinkillo industries",
            "icon_url": "https://cdn.discordapp.com/attachments/839055920016392235/949001974219694180/98393497dba4005d447acb431607ca6c.png"},
            "color": 4191046,
            "fields": [
            {
                "name": "‎",
                "value": f"[**Restocks**](https://restocks.net/es/account/sell)\n```{preciosRestocks}```",
                "inline": True
            },            {
                "name": "‎",
                "value": f"[**Klekt**]({linkVenderKlekt})\n```{preciosKlekt}```",
                "inline": True
            },{
                "name": "‎",
                "value": f"[**Alias**]({linkVenderKlekt})\n```{preciosAlias}```",
                "inline": True                
            }
            ]
            }  
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
        

def prettyPrices(d):
    str =""
    for i in d:
        if len(i) < 4:
            str = str + f"{i}    : {d[i]}\n"
        elif len(i) < 5: 
            str = str + f"{i}   : {d[i]}\n"
        elif len(i) <6:
            str = str + f"{i}  : {d[i]}\n"
        else:
            str = str + f"{i} : {d[i]}\n"
    return str