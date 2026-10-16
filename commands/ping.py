from discord.ext import commands

@commands.command(description="Ping the bot")
async def ping(ctx):
    await ctx.send(f"ping {round(ctx.bot.latency*1000)} ms")

async def setup(bot):
    bot.add_command(ping)