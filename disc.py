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

    if message.content.startswith("!IndustriasCinkilleras"): 
        if message.guild:
            user_message = message.content.split()
            pid = user_message[1]
            nombre, foto, preciosR =  Restocks(pid)
            linkVentaKlekt, preciosK =  Klekt(pid)
            listAlias =  Alias(pid)
            
            
            preciosRestocks = "\n".join(preciosR)
            preciosKlekt = "\n".join(preciosK)
            preciosAlias = "\n".join(listAlias)
            
            embed = discord.Embed(title=nombre )
            embed.add_field(name = "‎", value = f"[**Restocks**](https://restocks.net/es/account/sell)\n```{preciosRestocks}```",inline=True)
            embed.add_field(name = "‎", value = f"[**Klekt**]({linkVentaKlekt})\n```{preciosKlekt}```",inline=True)
            embed.add_field(name = "‎", value = f"[**Alias**]()\n```{preciosAlias}```",inline=False)
            embed.set_footer(text="Provided by cinkillo industries", icon_url="https://cdn.discordapp.com/attachments/839055920016392235/949001974219694180/98393497dba4005d447acb431607ca6c.png")
            embed.set_thumbnail(url=foto)
            await message.channel.send(embed=embed)
      
                       
client.run("ODY2NjE4NjIzMDgxODQwNjQw.YPVLfA.rMu3GFfDOubR7910M_edIdof91I")