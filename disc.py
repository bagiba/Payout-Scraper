import discord
from discord import Colour
from Modules.ModuloKlekt import Klekt
from Modules.ModuloRestocks import Restocks
from Modules.ModuloAlias import Alias
from Modules.ModuloWeTheNew import WeTheNew

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    excepcionRestocks = False
    excepcionKlekt = False
    excepcionWTN = False

    if message.content.startswith("!v "): 
        if message.guild:
            user_message = message.content.split()
            pid = user_message[1]

            try:
                nombre, foto, preciosR =  Restocks(pid)
                preciosRestocks = "\n".join(preciosR)
            except:
                excepcionRestocks = True

            try:
                linkVentaKlekt, preciosK =  Klekt(pid)
                preciosKlekt = "\n".join(preciosK)
                if preciosKlekt == "": excepcionKlekt = True
            except:
                excepcionKlekt = True

            try:
                linkVentaWTN, preciosW =  WeTheNew(pid)
                preciosWTN = "\n".join(preciosW)
            except:
                excepcionWTN = True

            #listAlias =  Alias(pid)
            #preciosAlias = "\n".join(listAlias)
            
            if not excepcionRestocks:
                embed = discord.Embed(title=nombre + " (" + pid + ")",
                color = 0x2DE9FC)
                embed.add_field(name = "‎", value = f"[**Restocks**](https://restocks.net/es/account/sell)\n```{preciosRestocks}```",inline=True)
                embed.set_thumbnail(url=foto)
            else:
                embed = discord.Embed(title="ERROR en el NOMBRE HDP" + " (" + "ERROR en el SKU TRIPLE HDP" + ")",
                color = 0x2DE9FC)
                embed.add_field(name = "‎", value = "**Restocks**\n```Excepcion en Restocks```",inline=True)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/852943748245749793/984213090876940288/unknown.png")
            if not excepcionKlekt:
                embed.add_field(name = "‎", value = f"[**Klekt**]({linkVentaKlekt})\n```{preciosKlekt}```",inline=True)
            else:
                embed.add_field(name = "‎", value = "**Klekt**\n```Excepcion en Klekt```",inline=True)
            if not excepcionWTN:
                embed.add_field(name = "‎", value = f"[**We The New**]({linkVentaWTN})\n```{preciosWTN}```",inline=True)
            else:
                embed.add_field(name = "‎", value = "**We The New**\n```Excepcion en We The New```",inline=True)
            #embed.add_field(name = "‎", value = f"[**Alias**]()\n```{preciosAlias}```",inline=False)
            embed.set_footer(text="Scraper", icon_url="https://media.discordapp.net/attachments/852943748245749793/984197952971087892/dollar-sign-in-blue-circle.jpg?width=676&height=676")
            await message.channel.send(embed=embed)
      
                       
client.run("ODY2NjE4NjIzMDgxODQwNjQw.YPVLfA.rMu3GFfDOubR7910M_edIdof91I")