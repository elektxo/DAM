#Librerias.
import discord
from discord.ext import commands
import time
# Prefix
bot =  commands.Bot(command_prefix='!', description='Bot de clase...')

#Comandos.
@bot.command()

async def ping(ctx):
    ms1= time.monotonic()
    mensaje = await ctx.send('Pong! ')
    ms2 = (time.monotonic() - ms1)*1000
    ms = (str(ms2).split("."))[0]
    await mensaje.edit(content="Pong! " + ms + " ms.")



#Eventos.
@bot.event
async def on_ready():
    await bot.change_presence(status="Ready!")
    print('El bot esta Listo.')

   


#Token bot.
bot.run('OTEwMTU1NTk5NzY4MDkyNjgy.YZOudA.FqtQgwVk-qQ33wKiqyCvimuNbSY')

