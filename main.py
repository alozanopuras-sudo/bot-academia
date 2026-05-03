import discord
import os
from discord.ext import commands

# Configuración de los permisos (Intents)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot online: {bot.user.name}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy tu Tutor ALP y ya estoy vivo.')

# Aquí es donde el bot lee la llave de Render
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
