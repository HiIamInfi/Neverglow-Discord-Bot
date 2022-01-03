import datetime
import os

import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
from numpy import genfromtxt

TASK_CYCLE = 10

# Auxiliary Methods


def is_birthday(birthday):
    datestring = datetime.date.today().strftime("%d.%m.%Y")

    if datestring[:6] == birthday[:6]:
        return True
    else:
        return False


def get_current_hour():
    now = datetime.datetime.now()
    return now.strftime("%H")


def has_been_run_today():
    file = f"{os.getcwd()}/neverglowbot/resources/last_check.txt"
    with open(file, "r") as f:
        last_check = f.read()
        last_check = last_check.split(sep=",")

    if last_check[0] == datetime.date.today().strftime("%d.%m.%Y"):
        return True
    else:
        return False


def update_last_check():
    file = f"{os.getcwd()}/neverglowbot/resources/last_check.txt"
    with open(file, "w") as f:
        f.write(datetime.datetime.now().strftime("%d.%m.%Y,%H:%M:%S"))


def get_idol_data():
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
    @ commands.Cog.listener()
    async def on_ready(self):
        print("Extension KPop Idol Data loaded")

    # Commands
    @ commands.command()
    async def tester(self, ctx):
        channel = self.client.get_channel(self.idol_channel)
        print(channel)
        await channel.send("Hi")

    # Tasks

    @ tasks.loop(seconds=TASK_CYCLE)
    async def idol_birtday_shoutout(self):
        # Check if current time is between 10:00 am and 10:59 am
        if int(get_current_hour()) != 17:
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
                embed = discord.Embed(
                    title=f"Happy {element[3]} Day!",
                    colour=discord.Colour.from_rgb(141, 106, 159),
                    type="rich",
                    description=f"Today is {element[4]}'s {element[3]}'s Birtday!\nShe got {calc_age} years old today!")
                # Set thumbnail (placeholder for now)
                embed.set_thumbnail(
                    url=element[5])
                channel = self.client.get_channel(self.idol_channel)
                # Send message
                await channel.send(embed=embed)
                update_last_check()
            except Exception as e:
                print(e)


def setup(bot):
    bot.add_cog(Kpop_Idol_Data(bot))
