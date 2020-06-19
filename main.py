import requests
from discord.ext.commands import Bot, Context, CommandError, guild_only, CommandNotFound
import discord.utils
import discord
import data

bot = Bot(command_prefix="|", case_insensitive=True)


@bot.event
async def on_ready():
    print("Corona ist doof")


@bot.command(name="get")
async def get(ctx):
    resp = requests.get("https://api.covid19api.com/summary", params=dict())

    daten = resp.json()

    wwcases = daten["Global"]["TotalConfirmed"]
    wwrecs = daten["Global"]["TotalRecovered"]
    wwdeaths = daten["Global"]["TotalDeaths"]

    denewcases = daten["Countries"][63]["NewConfirmed"]
    detotalcases = daten["Countries"][63]["TotalConfirmed"]

    denewrecs = daten["Countries"][63]["NewRecovered"]
    detotalrecs = daten["Countries"][63]["TotalRecovered"]

    denewdeaths = daten["Countries"][63]["NewDeaths"]
    detotaldeaths = daten["Countries"][63]["TotalDeaths"]

    embed = discord.Embed(title="Corona-Statistiken",
                          description="Aktuelle Statistiken zur Corona-Krise",
                          color="#0404B4",
                          url="https://github.com/LoCrealloc/covidbot",
                          )

    embed.set_thumbnail(url=daten.thumb_url)

    embed.add_field(name="Fälle weltweit", value=wwcases, inline=False)
    embed.add_field(name="Genesene weltweit", value=wwrecs, inline=True)
    embed.add_field(name="Tote weltweit", value=wwdeaths, inline=True)

    embed.add_field(name="Neue Fälle Deutschland", value=denewcases, inline=False)
    embed.add_field(name="Neue Genesene Deutschland", value=denewrecs, inline=True)
    embed.add_field(name="Neue Tote Deutschland", value=denewdeaths, inline=True)

    embed.add_field(name="Gesamt Fälle Deutschland", value=detotalcases, inline=False)
    embed.add_field(name="Gesamt Genesene Deutschland", value=detotalrecs, inline=True)
    embed.add_field(name="Gesamt Tote Deutschland", value=detotaldeaths, inline=True)

    embed.add_field(name="Daten", value="Diese Daten stammen von https://covid19api.com", inline=False)

    await ctx.channel.send(content="@" + str(ctx.author), embed=embed)

bot.run(data.token)
