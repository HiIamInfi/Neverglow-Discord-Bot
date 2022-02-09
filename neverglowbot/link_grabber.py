from discord.ext import commands
from os import getenv
from re import search


class Link_Grabber(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link_channel = int(getenv("LINK_CHANNEL"))

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Link Grabber loaded")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        # Checks if a bot is sending the message and exits if thats the case
        if ctx.author.bot:
            return
        if ctx.channel.id == self.link_channel:
            return
            # Checks if a URL is in the message content and exits if it is not
        if search("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ctx.content) == None:
            return
        # Saves the found match object into a variable
        url = search(
            "http[s]?://(?:[a-zA-ZäöüÄÖÜß]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", ctx.content)
        # Posts the URL to the specified channel
        channel = self.bot.get_channel(self.link_channel)
        await channel.send(f"Message noticed in Link Grabber: {url.group()}")


def setup(bot: commands.Bot):
    bot.add_cog(Link_Grabber(bot))
