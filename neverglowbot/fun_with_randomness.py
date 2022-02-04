from random import choice, randint
from typing import overload

from discord.ext import commands
from discord import Embed, Colour


def throw_dice(number=1, sides=6):

    results = []

    for i in range(number):
        results.append(randint(1, sides))

    return results


class Fun_with_Randomness(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Fun with Randomness loaded")

    # Commands
    @commands.command(name="oracle", brief="Ask the magic conch shell a question")
    async def ask_shell(self, ctx, *, question="Nothing specifically asked"):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        embed = Embed(title="Oracle Sana says:", colour=Colour.from_rgb(
            167, 211, 166), type="rich", description=f"{choice(responses)} \n\n  (Question was: {question})")
        embed.set_thumbnail(url="https://i.imgur.com/bprCsC4.jpeg")
        await ctx.send(embed=embed)

    @commands.command(name="dice", brief="Throws a number of dices specified by the first number provided with sides equal to the second number prodived")
    async def dice(self, ctx: commands.Context, *, input_string="1 6"):
        try:
            input_string = input_string.split(" ")
            dices = [int(i, base=16) for i in input_string]
            results = throw_dice(number=dices[0], sides=dices[1])
        except Exception as e:
            print(e)

        embed = Embed(title="Pink Yiren says:", colour=Colour.from_rgb(
            167, 211, 166), type="rich", description=f"I threw the dices for you and this is what came out {results}")
        embed.set_thumbnail(url="https://i.imgur.com/BHcHfej.jpg")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun_with_Randomness(bot))
