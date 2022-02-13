from json import load
from os import getenv, getcwd
from random import choice

from nextcord import Colour, Embed
from nextcord.ext import commands

# Methods


def get_operator(group: str) -> list:
    with open(getcwd()+"/neverglowbot/resources/r6_operators.json", "r") as read_file:
        operator_data = load(read_file)
    return operator_data[group]


def get_armament(operator: str) -> dict:
    with open(getcwd()+"/neverglowbot/resources/r6_armament.json", "r") as read_file:
        operator_armament = load(read_file)
    return operator_armament[operator]


class Rainbow_Six(commands.Cog):

    def __init__(self, bot):
        self.client = bot
        self.r6_channel = int(getenv("RAINBOW_SIX_CHANNEL"))

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Rainbow Six loaded")

    # Commands
    @commands.command(name="r6-def", brief="Let the bot choose a defender and an armament suggestion for you")
    async def operator_defender(self, ctx):
        # Get Operators and pick a random defender
        defenders = get_operator("defender")
        def_pick = choice(defenders)
        # Pick a random armament
        armament = get_armament(def_pick)
        arm_primary, arm_secondary = choice(
            armament["primary"]), choice(armament["secondary"])
        # Send a message with the picked operator
        embed = Embed(title="Police Captain Yiren says:", colour=Colour.from_rgb(
            167, 211, 166), type="rich", description=f"Heard you were looking for a Defender?\nCongrats your randomized defender is {def_pick}\n Your suggested armament is {arm_primary}, {arm_secondary}")
        embed.set_thumbnail(url="https://i.imgur.com/Uu8Rsg1.jpg")
        channel = self.client.get_channel(self.r6_channel)
        await channel.send(embed=embed)

    @commands.command(name="r6-att", brief="Let the bot choose a attacker and an armament suggestion for you")
    async def operator_attacker(self, ctx):
        attackers = get_operator("attacker")
        att_pick = choice(attackers)
        armament = get_armament(att_pick)
        arm_primary, arm_secondary = choice(
            armament["primary"]), choice(armament["secondary"])
        embed = Embed(title="Police Captain Yiren says:", colour=Colour.from_rgb(
            167, 211, 166), type="rich", description=f"Heard you were looking for a Attacker?\nCongrats your randomized defender is {att_pick}\n Your suggested armament is {arm_primary}, {arm_secondary}")
        embed.set_thumbnail(url="https://i.imgur.com/Uu8Rsg1.jpg")
        channel = self.client.get_channel(self.r6_channel)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Rainbow_Six(bot))
