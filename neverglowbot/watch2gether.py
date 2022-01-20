from discord.ext import commands
from os import getenv
from requests import post
from discord import Embed
from discord import Colour


class Watch2gether(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Watch2gether loaded")

    @commands.command(name="w2g", brief="Create a new Watch2Gether Room")
    async def commandName(self, ctx: commands.Context, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        body = {
            "w2g_api_key": getenv("WATCH2GETHER_API_KEY"),
            "share": url,
            "bg_color": "#000000",  # Watch2Gether Background Color
            "bg_opacity": 100  # Watch2Gether Background opacity"
        }
        response = post("https://w2g.tv/rooms/create.json",
                        headers=headers, json=body)

        if response.status_code != 200:
            await ctx.send(f"Request failed. Code {response.status_code}")
            return

        data = response.json()
        embed = Embed(title="Cinematographer Chaeyoung says:", colour=Colour.from_rgb(
            0, 150, 199), type="rich", description=f"Here is your Watch2Gether Room \n https://w2g.tv/rooms/{data['streamkey']}")
        embed.set_thumbnail(url="https://i.imgur.com/qp8JDRp.jpeg")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Watch2gether(bot))
