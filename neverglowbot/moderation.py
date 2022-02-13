from nextcord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Moderation loaded")

    # Commands
    @commands.command(name="clear", brief="Removes the last x messages from the channel where this command is called")
    @commands.has_permissions()
    async def commandName(self, ctx: commands.Context, amount=1):
        await ctx.channel.purge(limit=amount+1)


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
