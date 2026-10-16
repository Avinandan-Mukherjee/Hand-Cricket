import discord
from discord.ext import commands
import random
import asyncio


#main game logic
class MainGame(discord.ui.View):
    def __init__(self, plr1, plr2, choose):
        super().__init__(timeout=60)

        if choose == 1:
            self.plr1 = plr1
            self.plr2 = plr2

        else:
            self.plr1 = plr2
            self.plr2=plr1


        self.choose = choose
        self.players = [self.plr1,self.plr2]
        self.choices={}
        self.totalRun = 0
        self.targetRun = 0

        self.embed = discord.Embed(
            title=f"**{self.plr1.name} vs {self.plr2.name}**",
            description=f"{self.plr1.name} is Batting first",
            color=discord.Color.from_str("#aeff93")
        )

        self.embed.add_field(
            name=f"{self.plr1.name} Runs",
            value=f"{self.totalRun}"
        )

        self.embed.set_footer(
            text="Hand Cricket",
            icon_url=""
        )

        self.embed.timestamp = discord.utils.utcnow()


        self.player1 = True

    async def play(self, interaction, value):
        
        uid = interaction.user.id


        if uid not in [p.id for p in self.players]:
                    await interaction.response.send_message(
                        "This game isn't for you..",
                        ephemeral=True
                    )
                    return


        if uid in self.choices:
                    await interaction.response.send_message(
                        "You already chose!",
                        ephemeral=True
                    )
                    return


        self.choices[uid] = value

        # Waiting for the other player
        if len(self.choices) < 2:
            # await interaction.response.edit_message(
            #     content=(
            #         f"{interaction.user.mention} has chosen!\n"
            #         "Waiting for the other player..."
            #     ),
            #     view=self
            # )
            await interaction.response.defer()
            return

        a = self.choices[self.plr1.id]
        b = self.choices[self.plr2.id]
        self.choices={}

        if self.player1:
            if a!=b:
                if a!=0:
                    self.totalRun+=a
                    
                else:
                    self.totalRun+=b
                    

                self.embed=interaction.message.embeds[0]
                self.embed.set_field_at(0, name=f"{self.plr1.name} Runs",value=f"{self.totalRun}")

                if len(self.embed.fields) == 1:
                    self.embed.add_field(name="\u200b",value="\u200b", inline=False)
                    self.embed.add_field(name=f"{self.plr1.name} Chose",value=f"{a}", inline=True)
                    self.embed.add_field(name=f"{self.plr2.name} Chose",value=f"{b}", inline=True)

                else:
                    self.embed.set_field_at(1, name="\u200b",value="\u200b", inline=False)
                    self.embed.set_field_at(2, name=f"{self.plr1.name} Chose",value=f"{a}", inline=True)
                    self.embed.set_field_at(3, name=f"{self.plr2.name} Chose",value=f"{b}", inline=True)

                await interaction.response.edit_message(embed=self.embed, view=self)

            else:
                self.player1=False
    
                self.embed=interaction.message.embeds[0]
                self.embed.description=f"**{self.plr1.name} is out.**"
                self.embed.clear_fields()
                self.embed.add_field(name=f"{self.plr1.name} Runs",value=f"{self.totalRun}")
                self.embed.add_field(name=f"To Win", value=f"{self.plr2.name} has to score {(self.totalRun)+1}")

                self.embed.add_field(name="\u200b",value="\u200b", inline=False)
                self.embed.add_field(name=f"{self.plr1.name} Chose",value=f"{a}", inline=True)
                self.embed.add_field(name=f"{self.plr2.name} Chose",value=f"{b}", inline=True)
                await interaction.response.edit_message(embed=self.embed, view=None)
    
                await asyncio.sleep(5)
    
    
    
                self.embed.description=f"{self.plr2.name} is batting"
                self.embed.set_field_at(1, name=f"{self.plr2.name} Runs",value=f"{self.targetRun}")
                self.embed.remove_field(4)
                self.embed.remove_field(3)
                self.embed.remove_field(2)
                await interaction.message.edit(embed = self.embed, view=self)





        else:
            if (b!=a):
                if b!=0:
                    self.targetRun+=b
                    
                else:
                    self.targetRun+=a
                    

                self.embed=interaction.message.embeds[0]
                self.embed.set_field_at(1, name=f"{self.plr2.name} Runs",value=f"{self.targetRun}")


                if len(self.embed.fields) == 2:
                    self.embed.add_field(name="\u200b",value="\u200b", inline=False)
                    self.embed.add_field(name=f"{self.plr1.name} Chose",value=f"{a}", inline=True)
                    self.embed.add_field(name=f"{self.plr2.name} Chose",value=f"{b}", inline=True)

                else:
                    self.embed.set_field_at(2, name="\u200b",value="\u200b", inline=False)
                    self.embed.set_field_at(3, name=f"{self.plr1.name} Chose",value=f"{a}", inline=True)
                    self.embed.set_field_at(4, name=f"{self.plr2.name} Chose",value=f"{b}", inline=True)

                if self.targetRun > self.totalRun:
                    self.embed.description=f"**{self.plr2.name} was batting**"
                    self.embed.add_field(name=f"***{self.plr2.name} Won the match***", value="\u200b", inline=False)
                    self.embed.color = discord.Color.from_str("#6cf542")
                    await interaction.response.edit_message(embed=self.embed, view=None)

                else:
                    await interaction.response.edit_message(embed=self.embed, view=self)


            elif(a==b):
                self.embed=interaction.message.embeds[0]
                self.embed.description=f"**{self.plr2.name} is out.**"
                self.embed.set_field_at(0, name=f"{self.plr1.name} Runs",value=f"{self.totalRun}")
                self.embed.set_field_at(1, name=f"{self.plr2.name} Runs",value=f"{self.targetRun}")

                if len(self.embed.fields) == 2:
                    self.embed.add_field(name="\u200b",value="\u200b", inline=False)
                    self.embed.add_field(name=f"{self.plr1.name} Chose",value=f"{a}", inline=True)
                    self.embed.add_field(name=f"{self.plr2.name} Chose",value=f"{b}", inline=True)

                else:
                    self.embed.set_field_at(2, name="\u200b",value="\u200b", inline=False)
                    self.embed.set_field_at(3, name=f"{self.plr1.name} Chose",value=f"{a}", inline=True)
                    self.embed.set_field_at(4, name=f"{self.plr2.name} Chose",value=f"{b}", inline=True)


                if self.targetRun == self.totalRun:
                    self.embed.add_field(name="***Match Draw***", value="\u200b", inline=False)
                    self.embed.color = discord.Color.from_str("#eeff00")

                else:
                    self.embed.add_field(name=f"***{self.plr1.name} Won the match***", value="\u200b", inline=False)
                    self.embed.color = discord.Color.from_str("#6cf542")
                await interaction.response.edit_message(embed = self.embed, view=None)


        

    @discord.ui.button(
            label="0",
            style=discord.ButtonStyle.primary
        )
    async def zero(self, interaction, button):
        await self.play(interaction, 0)


    @discord.ui.button(
            label="1",
            style=discord.ButtonStyle.primary
        )
    async def one(self, interaction, button):
        await self.play(interaction, 1)


    @discord.ui.button(
            label="2",
            style=discord.ButtonStyle.primary
        )
    async def two(self, interaction, button):
        await self.play(interaction, 2)


    @discord.ui.button(
            label="3",
            style=discord.ButtonStyle.primary
        )
    async def three(self, interaction, button):
        await self.play(interaction, 3)


    @discord.ui.button(
            label="4",
            style=discord.ButtonStyle.primary
        )
    async def four(self, interaction, button):
        await self.play(interaction, 4)


    @discord.ui.button(
            label="5",
            style=discord.ButtonStyle.primary
        )
    async def five(self, interaction, button):
        await self.play(interaction, 5)


    @discord.ui.button(
            label="6",
            style=discord.ButtonStyle.primary
        )
    async def six(self, interaction, button):
        await self.play(interaction, 6)





        



# Batting / Bowling UI
class BatBallButtons(discord.ui.View):
    def __init__(self, challenger, opponent, tossWinner):
        super().__init__(timeout=60)

        self.challenger = challenger
        self.opponent = opponent
        self.tossWinner = tossWinner

        self.otherPlayer = (
            opponent if tossWinner.id == challenger.id else challenger
        )

    async def choose(self, interaction, choice):
        if interaction.user.id != self.tossWinner.id:
            await interaction.response.send_message(
                f"Only {self.tossWinner.name} can choose!",
                ephemeral=True
            )
            return

        if choice == "Batting":
            plr = 1
            result = (
                f"{self.tossWinner.mention} chose **Batting**\n"
                f"{self.otherPlayer.mention} will bowl."
            )
        else:
            plr = 2
            result = (
                f"{self.tossWinner.mention} chose **Bowling**\n"
                f"{self.otherPlayer.mention} will bat."
            )

        await interaction.response.edit_message(
            content=result+"\n Game will begin Shortly"
        )

        mainGame = MainGame(self.tossWinner, self.otherPlayer, plr)
        await asyncio.sleep(5)
        await interaction.message.edit(
            content="",
            embed=mainGame.embed,
            view=mainGame)


    @discord.ui.button(
        label="Batting",
        style=discord.ButtonStyle.success
    )
    async def batting(self, interaction, button):
        await self.choose(interaction, "Batting")

    @discord.ui.button(
        label="Bowling",
        style=discord.ButtonStyle.primary
    )
    async def bowling(self, interaction, button):
        await self.choose(interaction, "Bowling")

        






# Head Tail
class TossButtons(discord.ui.View):
    def __init__(self, challenger, opponent, chosen):
        super().__init__(timeout=60)

        self.challenger = challenger
        self.opponent = opponent
        self.chosen = chosen

        
        self.chosenHT = random.choice(["Head", "Tail"])

    async def toss(self, interaction, choice):
        if interaction.user.id != self.chosen.id:
            await interaction.response.send_message(
                f"Only {self.chosen.name} can choose!",
                ephemeral=True
            )
            return

        # who won the toss
        if choice == self.chosenHT:
            tossWinner = self.chosen
        else:
            tossWinner = (
                self.opponent
                if self.chosen.id == self.challenger.id
                else self.challenger
            )

        otherPlayer = (
            self.opponent
            if tossWinner.id == self.challenger.id
            else self.challenger
        )

        batball = BatBallButtons(
            self.challenger,
            self.opponent,
            tossWinner
        )

        await interaction.response.edit_message(
            content=(
                f"**Toss Result: {self.chosenHT}**\n\n"
                f"{tossWinner.name} won the toss\n"
                f"{tossWinner.name}, choose Batting or Bowling."
            ),
            view=batball
        )

    @discord.ui.button(
        label="Heads",
        style=discord.ButtonStyle.primary
    )
    async def head(self, interaction, button):
        await self.toss(interaction, "Head")

    @discord.ui.button(
        label="Tails",
        style=discord.ButtonStyle.primary
    )
    async def tail(self, interaction, button):
        await self.toss(interaction, "Tail")






# Accept and Decline
class ChallengeButtons(discord.ui.View):
    def __init__(self, challenger, opponent):
        super().__init__(timeout=60)

        self.challenger = challenger
        self.opponent = opponent

    @discord.ui.button(
        label="Accept",
        style=discord.ButtonStyle.success
    )
    async def accept(self, interaction, button):
        if interaction.user.id != self.opponent.id:
            await interaction.response.send_message(
                "Only the challenged player can accept!",
                ephemeral=True
            )
            return

        
        self.chosenPlayer = random.choice([
            self.challenger,
            self.opponent
        ])

        await interaction.response.edit_message(
            content=(
                f"{self.opponent.name} accepted the challenge!\n"
                f"The game will begin shortly..."
            ),
            view=None
        )

        await asyncio.sleep(2)

        toss = TossButtons(
            self.challenger,
            self.opponent,
            self.chosenPlayer
        )

        await interaction.message.edit(
            content=(
                f" **Toss Round**\n\n"
                f" {self.chosenPlayer.mention}, "
                f"choose Heads or Tails!"
            ),
            view=toss
        )

    @discord.ui.button(
        label="Decline",
        style=discord.ButtonStyle.danger
    )
    async def decline(self, interaction, button):
        if interaction.user.id != self.opponent.id:
            await interaction.response.send_message(
                "Only the challenged player can decline!",
                ephemeral=True
            )
            return

        await interaction.response.edit_message(
            content=f" {self.opponent.name} declined the challenge.",
            view=None
        )





#start frm here


@commands.command(description="Challenge an user for a match")
async def challenge(ctx, opponent: discord.Member = None):
    if opponent == None:
        await ctx.send("Ping anyone to play with..")

    if opponent.id == ctx.author.id:
        await ctx.send("You cant challange urself..")
        return

    if opponent.bot:
        await ctx.send("You cant challenge a bot..")
        return

    await ctx.send(
        f" {opponent.mention}, "
        f"{ctx.author.mention} has challenged you\n"
        "Will you accept?",
        view=ChallengeButtons(ctx.author, opponent)
    )


async def setup(bot):
    bot.add_command(challenge)