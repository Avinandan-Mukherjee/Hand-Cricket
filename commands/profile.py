import traceback
from discord.ext import commands
from database import create_user, get_stats
import discord

@commands.command(description="Shows the user Profile and statistics")
async def profile(ctx):
    await create_user(ctx.author.id, ctx.author.name)
    stats = await get_stats(ctx.author.id)

    embed = discord.Embed(
        title=f"{ctx.author.name}",
        description=" ",
        color=discord.Color.from_str("#6f00ff")
    )

    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.add_field(
            name=f"Todal Matches played",
            value=stats['matches'],
            inline=True
        )

    embed.add_field(
            name=f"Highst Runs scored",
            value=stats['highst_run'],
            inline=True
        )

    embed.add_field(name="\u200b", value="\u200b", inline=True)

    embed.add_field(
            name=f"Todal Matches won",
            value=stats['wins'],
            inline=True
        )

    embed.add_field(
            name=f"Todal Matches lost",
            value=stats['losses'],
            inline=True
        )

    embed.add_field(name="\u200b", value="\u200b", inline=True)


    embed.add_field(
        name=f"Todal Runs scored",
        value=stats['total_run'],
        inline=True
    )

    embed.add_field(
        name=f"Todal wickets taken",
        value=stats['wickets_taken'],
        inline=True
    )

    embed.add_field(name="\u200b", value="\u200b", inline=True)


    embed.set_footer(
    text=f"Hand Cricket",
    icon_url= ctx.bot.user.display_avatar.url
        )
    
    embed.timestamp = discord.utils.utcnow()


    await ctx.send(embed=embed)


async def setup(bot):
    bot.add_command(profile)