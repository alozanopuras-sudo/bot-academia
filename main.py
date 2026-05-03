import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot online: {bot.user.name}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy tu Tutor ALP y ya estoy vivo.')

# Esto lee la llave de la pestaña Ambiente de Render
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ ERROR: No se encontró la variable DISCORD_TOKEN")
