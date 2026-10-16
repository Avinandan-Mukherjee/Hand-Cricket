
import discord
from discord.ext import commands

@commands.command(description="Shows all available bot commands.")
async def help(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description="Here are all the available commands.. \nTo run a command, do `hc <command>`\n",
        color=discord.Color.blurple()
    )

    embed.set_author(
        name=ctx.author.name,
        icon_url=ctx.author.display_avatar.url,
    )

    embed.set_footer(
        text="Hand Cricket",
        icon_url=ctx.bot.user.display_avatar.url
    )

    embed.timestamp = discord.utils.utcnow()
    c=1
    for cmd in ctx.bot.commands:
        if cmd.hidden:
            continue

        embed.add_field(
            name=f"{c}. `{cmd.name}`",
            value=cmd.description or "No description available.",
            inline=False
        )
        c+=1



    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(help)
