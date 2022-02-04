from discord.ext import commands
from os import getenv
from requests import post
from discord import Embed
from discord import Colour


def get_streamkey(url: str):
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
        print(f"Request failed. Code {response.status_code}")
        return
    data = response.json()
    return data["streamkey"]


class Watch2gether(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.w2g_channel = int(getenv("WATCHTOGETHER_CHANNEL"))

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Watch2gether loaded")

    @commands.command(name="w2g", brief="Create a new Watch2Gether Room")
    async def get_w2g(self, ctx: commands.Context):
        streamkey = get_streamkey(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        embed = Embed(title="Cinematographer Chaeyoung says:", colour=Colour.from_rgb(
            0, 150, 199), type="rich", description=f"Here is your Watch2Gether Room \n https://w2g.tv/rooms/{streamkey}")
        embed.set_thumbnail(url="https://i.imgur.com/qp8JDRp.jpeg")
        channel = self.bot.get_channel(self.w2g_channel)
        await channel.send(embed=embed)

    @commands.command(name="energyrestore", brief="Open a new room with the og energy restore playing")
    async def get_energyrestore(self, ctx: commands.Context):
        streamkey = get_streamkey(
            "https://youtu.be/OPtFn5YBhkc")
        embed = Embed(title="Cinematographer Chaeyoung says:", colour=Colour.from_rgb(
            0, 150, 199), type="rich", description=f"Here is your Watch2Gether Room \n https://w2g.tv/rooms/{streamkey}")
        embed.set_thumbnail(url="https://i.imgur.com/qp8JDRp.jpeg")
        channel = self.bot.get_channel(self.w2g_channel)
        await channel.send(embed=embed)

    @commands.command(name="itsabout", description="Opens a new room with the ITZY/Everglow clip compilation playing")
    async def get_b_and_food(self, ctx: commands.Context):
        streamkey = get_streamkey(
            "https://youtu.be/Oaq8-JVLuHU")
        embed = Embed(title="Cinematographer Chaeyoung says:", colour=Colour.from_rgb(
            0, 150, 199), type="rich", description=f"Here is your Watch2Gether Room \n https://w2g.tv/rooms/{streamkey}")
        embed.set_thumbnail(url="https://i.imgur.com/qp8JDRp.jpeg")
        channel = self.bot.get_channel(self.w2g_channel)
        await channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Watch2gether(bot))
