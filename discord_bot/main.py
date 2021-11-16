#Librerias.
import discord
from discord.ext import commands
# Prefix
bot =  commands.Bot(command_prefix='!', description='Bot de clase...')

#Comandos.
@bot.command()

async def ping(ctx):
    await ctx.send('pong')

#Eventos.
@bot.event()
async def on_ready():
    await bot.change_presence(activity='Tamos ready!')
    print('El bot esta Listo.')


#Token bot.
bot.run('OTEwMTU1NTk5NzY4MDkyNjgy.YZOudA.FqtQgwVk-qQ33wKiqyCvimuNbSY')

