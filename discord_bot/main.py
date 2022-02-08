#Librerias.
from discord import *
import discord
from discord.ext import commands

# Prefix

bot =  commands.Bot(command_prefix='!', description='Bot de clase...')

#Comandos.
@bot.command()

async def ping(ctx):
    await ctx.send("Pong! " + round(bot.latency*1000)+ " ms.")



#Eventos.
@bot.event

async def on_ready():
    await bot.change_presence(status="Ready!")
    print('El bot esta Listo.')
#Información del Bot
    embed = discord.Embed(title="Bot Pruebas")
    embed.set_footer("Esto es una puta prueba bro.")

    await


#Token bot.
bot.run('OTEwMTU1NTk5NzY4MDkyNjgy.YZOudA.FqtQgwVk-qQ33wKiqyCvimuNbSY')

