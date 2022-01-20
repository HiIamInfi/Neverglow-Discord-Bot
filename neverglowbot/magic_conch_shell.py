from random import choice

from discord.ext import commands
from discord import Embed, Colour


class Magic_Conch_Shell(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Magic Conch Shell loaded")

    # Commands
    @commands.command(name="oracle", brief="Ask the magic conch shell a question")
    async def ask_shell(self, ctx, *, question):
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


def setup(bot):
    bot.add_cog(Magic_Conch_Shell(bot))
