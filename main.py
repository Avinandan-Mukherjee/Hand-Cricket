import discord
from discord.ext import commands
import asyncio
import os

from dotenv import load_dotenv
load_dotenv() 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="hc ", intents=intents, help_command=None)



#bot presence
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("gay bot is ready")
    await bot.change_presence(
        status=discord.Status.idle,  
        activity=discord.Activity(type=discord.ActivityType.listening, name="hc help")
    )


#taking all functions
async def main():
    async with bot:
        await bot.load_extension("commands.ping")
        await bot.load_extension("commands.help")
        await bot.load_extension("commands.profile")
        await bot.load_extension("commands.rules")
        await bot.load_extension("commands.challenge")




        #bot token run
        await bot.start(os.getenv("bot_token"))



asyncio.run(main())