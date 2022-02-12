import datetime
import os

from nextcord.ext import commands, tasks
from nextcord import Colour, Embed
from numpy import genfromtxt

# Auxiliary Methods


def is_birthday(birthday: str) -> bool:
    datestring = datetime.date.today().strftime("%d.%m.%Y")
    if datestring[:6] == birthday[:6]:
        return True
    else:
        return False


def calc_difference(idol_birtday: str) -> int:
    today = datetime.date.today()
    idol_birtday = idol_birtday.split(".")

    idol_birtday = datetime.date(today.year, int(
        idol_birtday[1]), int(idol_birtday[0]))

    if idol_birtday < today:
        idol_birtday = idol_birtday.replace(year=today.year+1)

    return abs(idol_birtday - today).days


def get_deltas(idol_dataset: list) -> list:
    deltas = []
    for idol in idol_dataset:
        new_line = (idol[0], idol[1], calc_difference(idol[1]), idol[5])
        deltas.append(new_line)

    deltas.sort(key=lambda x: x[2], reverse=False)

    return deltas


def get_current_hour() -> str:
    now = datetime.datetime.now()
    return now.strftime("%H")


def has_been_run_today() -> bool:
    file = f"{os.getcwd()}/neverglowbot/resources/last_check.txt"
    with open(file, "r") as f:
        last_check = f.read()
        last_check = last_check.split(sep=",")
    if last_check[0] == datetime.date.today().strftime("%d.%m.%Y"):
        return True
    else:
        return False


def update_last_check() -> None:
    file = f"{os.getcwd()}/neverglowbot/resources/last_check.txt"
    with open(file, "w") as f:
        f.write(datetime.datetime.now().strftime("%d.%m.%Y,%H:%M:%S"))


def get_idol_data() -> list:
    data_source = f"{os.getcwd()}/neverglowbot/resources/idol_data.csv"
    idols_array = genfromtxt(data_source, delimiter=",",
                             dtype=None, encoding="UTF-8")
    return idols_array


class Kpop_Idol_Data(commands.Cog):

    def __init__(self, bot):
        self.client = bot
        self.idol_channel = int(os.getenv("IDOL_ALERT_CHANNEL"))
        self.idol_birtday_shoutout.start()

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension KPop Idol Data loaded")

    # Commands
    @commands.command(name="nextbday", brief="Ouputs the next Idols birthday and also names the following four")
    async def k_forecast(self, ctx):
        data = get_idol_data()
        delta_list = get_deltas(data)

        forecast_data = delta_list[0:5]

        embed = Embed(
            title=f"Thank you for asking! Next up is {forecast_data[0][0]}",
            colour=Colour.from_rgb(141, 106, 159),
            type="rich",
            description=f"The next Idols birthday will be {forecast_data[0][0]}, her birthday is on {forecast_data[0][1]}, in {forecast_data[0][2]} days. \n Next after that: {forecast_data[1][0]} in {forecast_data[1][2]} days, {forecast_data[2][0]} in {forecast_data[2][2]} days, {forecast_data[3][0]} in {forecast_data[3][2]} days, {forecast_data[4][0]} in {forecast_data[4][2]} days."
        )
        embed.set_thumbnail(url=forecast_data[0][3])
        await ctx.send(embed=embed)

    # Tasks

    @tasks.loop(seconds=20)
    async def idol_birtday_shoutout(self):
        # Check if current time is between 01:00 am and 01:59 am
        if int(get_current_hour()) != 1:
            return
        # Check if task was already completed today
        if has_been_run_today():
            return
        # Get Data from CSV
        data = get_idol_data()
        cache = []
        # Search for positive Hits
        for idol in data:
            if is_birthday(idol[1]):
                cache.append(idol)
        # Prepare & send messages
        for element in cache:
            try:
                # Calc age based on current day
                calc_age = int(datetime.date.today().strftime("%Y")) - \
                    int(element[1][6:])
                # Create Embed
                embed = Embed(
                    title=f"Happy {element[3]} Day!",
                    colour=Colour.from_rgb(141, 106, 159),
                    type="rich",
                    description=f"Today is {element[4]}'s {element[3]}'s Birtday!\nShe got {calc_age} years old today!")
                embed.set_thumbnail(
                    url=element[5])
                channel = self.client.get_channel(self.idol_channel)
                # Send message
                await channel.send(embed=embed)
                # Update last check
                update_last_check()
            except Exception as e:
                print(e)


def setup(bot):
    bot.add_cog(Kpop_Idol_Data(bot))
