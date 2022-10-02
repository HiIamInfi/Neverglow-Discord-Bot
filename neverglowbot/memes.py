from nextcord.ext import commands, tasks
import nextcord
from os import getenv
from json import load
import requests
from random import randint, choice
import praw


def get_meme_config() -> list:
    with open(getenv("CONFIG")+"/meme_config.json", "r") as read_file:
        meme_data = load(read_file)
    return meme_data


def scrape_meme(topic: str):
    reddit = praw.Reddit(
        client_id=getenv("REDDIT_CLIENT_ID"),
        client_secret=getenv("REDDIT_SECRET"),
        user_agent=getenv("REDDIT_USER_AGENT"),
        check_for_async=False
    )

    subreddit = reddit.subreddit(topic)
    meme = subreddit.random()
    try:
        _ = meme.preview
        result = {
            "post_link": meme.shortlink,
            "subreddit": topic,
            "title": meme.title,
            "url": meme.url,
            "author": meme.author.name,
            "spoilers_enabled": subreddit.spoilers_enabled,
            "nsfw": subreddit.over18,
            "image_previews": [i["url"] for i in meme.preview.get("images")[0].get("resolutions")]
        }
    except Exception as e:
        result = {
            "post_link": meme.shortlink,
            "subreddit": topic,
            "title": meme.title,
            "url": meme.url,
            "author": meme.author.name,
            "spoilers_enabled": subreddit.spoilers_enabled,
            "nsfw": subreddit.over18,
            "image_previews": ["No Preview Found For This Meme.. Sorry For That"]
        }
    return result


class Memes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = get_meme_config()
        print(self.config)
        self.meme_channel = int(getenv("MEME_CHANNEL"))

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension Memes loaded")
        self.hourly_meme.start()

    # Commands
    @commands.command(name="meme", brief="Fetches a meme")
    async def meme(self, ctx: commands.Context):

        topic = choice(self.config["subreddits"])
        print(topic)
        res = scrape_meme(topic)

        title = res["title"]
        url = res["url"]
        subreddit = res["subreddit"]
        author = res["author"]

        embed = nextcord.Embed(
            title=title, colour=nextcord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        embed.set_image(url=url)
        embed.set_footer(
            text=f"{author} | Subreddit: {subreddit}")
        await ctx.send(embed=embed)

    # Tasks
    @tasks.loop(seconds=3600)  # To be changed to 3600
    async def hourly_meme(self):
        channel = self.bot.get_channel(self.meme_channel)

        topic = choice(self.config["subreddits"])
        res = scrape_meme(topic)

        title = res["title"]
        url = res["url"]
        subreddit = res["subreddit"]
        author = res["author"]

        embed = nextcord.Embed(
            title=title, colour=nextcord.Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        embed.set_image(url=url)
        embed.set_footer(
            text=f"{author} | Subreddit: {subreddit}")

        await channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Memes(bot))
