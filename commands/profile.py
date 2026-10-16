from discord.ext import commands


@commands.command(description="Shows the user Profile")
async def profile(ctx):
    await ctx.send(f"ping", mention_author=True)


async def setup(bot):
    bot.add_command(profile)