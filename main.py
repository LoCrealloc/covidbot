import requests
from discord.ext.commands import Bot, Context, CommandError, guild_only, CommandNotFound
import discord.utils
import discord
from data import token

bot = Bot(command_prefix="|", case_insensitive=True)


@bot.event
async def on_ready():
    print("Corona ist doof")


@bot.command(name="get")
async def get(ctx):
    resp = requests.get("https://api.covid19api.com/summary", params=dict())

    data = resp.json()

    newcases = data["Countries"][63]["NewConfirmed"]
    totalcases = data["Countries"][63]["TotalConfirmed"]

    newrecs = data["Countries"][63]["NewRecovered"]
    totalrecs = data["Countries"][63]["TotalRecovered"]

    newdeaths = data["Countries"][63]["NewDeaths"]
    totaldeaths = data["Countries"][63]["TotalDeaths"]

    embed = discord.Embed(title="Corona-Statistiken",
                          description="Aktuelle Statistiken zur Corona-Krise",
                          color="#0404B4",
                          url="https://github.com/LoCrealloc/covidbot",
                          )
    embed.set_thumbnail()

bot.run(token)
