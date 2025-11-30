import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Configuration
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_ENDPOINT = os.getenv("MISTRAL_API_ENDPOINT")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ask(ctx, *, question):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": question
    }
    response = requests.post(MISTRAL_API_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        answer = response.json().get("answer", "No answer received")
        await ctx.send(f"Mistral says: {answer}")
    else:
        await ctx.send(f"Error: {response.status_code}")

bot.run(DISCORD_BOT_TOKEN)