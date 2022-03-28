import discord
from discord import Colour
from Modules.ModuloKlekt import Klekt
from Modules.ModuloRestocks import Restocks
from Modules.ModuloAlias import Alias

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!payout"): 
        if message.guild:
            user_message = message.content.split()
            pid = user_message[1]
            nombre, foto, preciosR =  Restocks(pid)
            linkVentaKlekt, preciosK =  Klekt(pid)
            listAlias =  Alias(pid)
            
            
            preciosRestocks = "\n".join(preciosR)
            preciosKlekt = "\n".join(preciosK)
            preciosAlias = "\n".join(listAlias)
            
            embed = discord.Embed(title=nombre + " (" + pid + ")",
            color = 0x9faaec)
            embed.add_field(name = "‎", value = f"[**Restocks**](https://restocks.net/es/account/sell)\n```{preciosRestocks}```",inline=True)
            embed.add_field(name = "‎", value = f"[**Klekt**]({linkVentaKlekt})\n```{preciosKlekt}```",inline=True)
            embed.add_field(name = "‎", value = f"[**Alias**]()\n```{preciosAlias}```",inline=False)
            embed.set_footer(text="Flow 2000", icon_url="https://yt3.ggpht.com/lVOG576nC91WIpfjaS-LFjoGCnhlLxRKEKlzZpe8FIwKcCfAzYxlw_wixar7PB1OAuXjNBcDZg=s900-c-k-c0x00ffffff-no-rj")
            embed.set_thumbnail(url=foto)
            await message.channel.send(embed=embed)
      
                       
client.run("ODY2NjE4NjIzMDgxODQwNjQw.YPVLfA.rMu3GFfDOubR7910M_edIdof91I")