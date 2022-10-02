import datetime
import os
from dataclasses import asdict, astuple, dataclass
from json import load

from nextcord import Colour, Embed
from nextcord.ext import commands, tasks

# Auxiliary class


@dataclass(frozen=False, order=True)
class Idol():
    id: str         # Unique ID
    name: str       # Legal Name
    birthday: datetime.datetime   # Birthday
    group: str      # Group name
    country: str    # Country of birth
    stage_name: str  # Stage name
    image_url: str  # URL to image on imgur
    age: int  # Age
    diff_next: int  # Days left till next birthday

    def __init__(self, id: str, name: str, birthday: str, group: str, country: str, stage_name: str, image_url: str):
        self.id = id
        self.name = name
        self.birthday = datetime.datetime.strptime(birthday, "%d.%m.%Y")
        self.group = group
        self.country = country
        self.stage_name = stage_name
        self.image_url = image_url
        self.age = datetime.datetime.today().year - self.birthday.year - \
            ((datetime.datetime.today().month, datetime.datetime.today().day)
             < (self.birthday.month, self.birthday.day))
        this_year = self.birthday \
            .replace(year=datetime.datetime.today().year)
        if this_year.date() < datetime.datetime.today().date():
            this_year = this_year.replace(
                year=datetime.datetime.today().year+1)
        self.diff_next = abs(this_year.date() -
                             datetime.datetime.today().date()).days

    def update(self):
        # Update age
        today = datetime.today()
        idol_birthday = datetime.strptime(self.birthday, "%d.%m.%Y")
        idol_birthday = idol_birthday.replace(year=today.year)
        if idol_birthday < today:
            idol_birthday = idol_birthday.replace(year=today.year+1)
        self.diff_next = abs(idol_birthday - today).days
        # Update days till next birthday
        today = datetime.today()
        born = datetime.strptime(self.birthday, "%d.%m.%Y")
        self.age = today.year - born.year - \
            ((today.month, today.day) < (born.month, born.day))

# Auxiliary Methods


def get_idol_data(path: str) -> list:
    # Aquire keys
    with open(path, "r") as read_file:
        raw_data = load(read_file)
    # Initialize the list
    idol_data = []
    # Create a new Idol object for each idol in idol_data.json
    for key in raw_data:
        new_idol = get_idol(path, key)
        idol_data.append(new_idol)

    return idol_data


def get_idol(path: str, idol_id: str) -> Idol:
    # Aquire raw data
    with open(path, "r") as read_file:
        idol_data = load(read_file)
    ask = idol_data[idol_id]
    tell = Idol(id=idol_id, name=ask["name"],
                birthday=ask["birthday"], group=ask["group"], country=ask["country"], stage_name=ask["stage_name"], image_url=ask["image_url"])
    return tell


class Kpop_Idol_Data(commands.Cog):

    def __init__(self, bot):
        self.client = bot
        cpath = os.getenv("CONFIG")
        self.idol_data = get_idol_data(f"{cpath}idol_data.json")
        self.idol_channel = int(os.getenv("IDOL_ALERT_CHANNEL"))
        self.run = datetime.datetime(1900, 1, 1)

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension KPop Idol Data loaded")
        self.idol_birthday_shoutout.start()

    # Commands
    @commands.command(name="nextbday", brief="Ouputs the next Idols birthday and also names the following four")
    async def k_forecast(self, ctx):

        forecast_data = sorted(
            self.idol_data, key=lambda x: x.diff_next, reverse=False)

        embed = Embed(
            title=f"Thank you for asking! Next up is {forecast_data[0].name}",
            colour=Colour.from_rgb(141, 106, 159),
            type="rich",
            description=f"The next Idols birthday will be {forecast_data[0].name}, her upcoming birthday is in {forecast_data[0].diff_next} days. \n Next after that: {forecast_data[1].name}, her upcoming birthday is in {forecast_data[1].diff_next} days."
        )
        embed.set_thumbnail(url=forecast_data[0].image_url)
        await ctx.send(embed=embed)

    # Tasks

    @tasks.loop(seconds=20)
    async def idol_birthday_shoutout(self):
        # Check if current time is between 00:00 am and 00:59 am
        if int(datetime.datetime.now().strftime("%H")) != 0:
            return
        # Check if task was already completed today
        if self.run.date() == datetime.datetime.now().date():
            return
        # Get Data from CSV
        cache = []
        # Search for positive Hits
        for idol in self.idol_data:
            if idol.diff_next == 0:
                cache.append(idol)

        # Prepare & send messages
        for element in cache:
            try:
                # Calc age based on current day
                calc_age = int(datetime.date.today().strftime("%Y")) - \
                    int(element.birthday.strftime("%Y"))
                # Create Embed
                embed = Embed(
                    title=f"Happy { element.stage_name } Day!",
                    colour=Colour.from_rgb(141, 106, 159),
                    type="rich",
                    description=f"Today is {element.group}'s {element.stage_name}'s Birthday!\nShe got {calc_age} years old today!")
                embed.set_thumbnail(
                    url=element.image_url)
                channel = self.client.get_channel(self.idol_channel)
                # Send message
                await channel.send(embed=embed)
                # Update last check
                self.run = datetime.datetime.now()
            except Exception as e:
                print(e)


def setup(bot):
    bot.add_cog(Kpop_Idol_Data(bot))
