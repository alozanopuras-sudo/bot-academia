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

# IMPORTANTE: Asegúrate de que en Render la variable sea DISCORD_TOKEN
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    print("❌ ERROR: No se encuentra la variable DISCORD_TOKEN en Render")
else:
    bot.run(TOKEN)
