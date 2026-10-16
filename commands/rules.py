import discord
from discord.ext import commands


@commands.command(description="Shows the game rules")
async def rules(ctx):
    embed = discord.Embed(
    title="Hand Cricket Rules",
    description="These r the rules of the game.",
    color=discord.Color.blurple()
)

    embed.add_field(
name="🪙 **The Toss Round**",
value="""
1. One player gets picked to call Heads or Tails.
2. The computer randomly flips a coin to reveal the result.
3. Whoever wins the toss gets to decide whether to Bat or Bowl first.
 
 """,
inline=False
    )   




    embed.add_field(
name="🏏 **Batting Rules**",
value="""
1. Every round, the batsman picks a number between 0 and 6.
2. Whatever number you pick gets added directly to your total score.
`Example: If you start with a 6 and then pick a 5, your score is 11.`
3. The Special 0 Rule: If you pick 0, you don't get zero points—instead, whatever number the bowler picked gets added to your score!
`Example: If you pick 0 and the bowler picked 4, you get 4 runs added to your total.`
 
 """,
inline=False
    )


    embed.add_field(
name="🥎 **Bowling & Getting Out**",
value="""
1. The bowler also picks a number between 0 and 6 each round.
2. The bowler’s goal is to match the exact number the batsman picks.
3. If both players pick the exact same number, the batsman is OUT!
`Note: This includes 0 vs 0—if both pick 0, it’s an out!`
 
 """,
inline=False
    )


    embed.add_field(
name="🔄 **Switching Sides**",
value="""
1. Once the first batsman is out, the roles flip: the bowler becomes the new batsman, and the original batsman now bowls.
2. The new batsman's goal is to beat the target score set by the first player.
 
 """,
inline=False
    )

    embed.add_field(
name="🏆 **Winning Condition**",
value="""
Whoever scores more total runs wins the game!
 """,
inline=False
    )


    embed.set_footer(
text=f"Requested by {ctx.author.name}",
icon_url= ctx.author.display_avatar.url
    )

    embed.timestamp = discord.utils.utcnow()

    
    await ctx.send(embed=embed)


async def setup(bot):
    bot.add_command(rules)