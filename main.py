import discord
import os
from discord.ext import commands

# Configuramos los permisos obligatorios
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ SISTEMA PREPARADO: {bot.user.name}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Aquí el Tutor ALP, listo para ayudar!')

# Leemos el token de forma segura desde el panel de Render
TOKEN = os.environ.get('DISCORD_TOKEN')

if __name__ == "__main__":
    if TOKEN:
        try:
            bot.run(TOKEN)
        except Exception as e:
            print(f"❌ ERROR DE CONEXIÓN: {e}")
    else:
        print("❌ ERROR CRÍTICO: No se encontró la variable DISCORD_TOKEN en Render.")
