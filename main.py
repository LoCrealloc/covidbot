import requests
from discord.ext.commands import Bot
import discord.utils
import discord
import data
from tokenid import tokenid

bot = Bot(command_prefix="|", case_insensitive=True)


@bot.event
async def on_ready():
    print("Bot is online")
    status = discord.Activity(name="Developed by LoC!")
    await bot.change_presence(status=discord.Status.online, activity=status)


@bot.command(name="info", aliases=["infos", "about"])
async def info(ctx: discord.Message):
    embed = discord.Embed(title="Corona-Statistiken-Bot",
                          description="Dieser Bot sendet aktuelle Coronastatistiken direkt auf deinen Server",
                          color=0x088A08,
                          url="https://github.com/LoCrealloc/covidbot")

    embed.set_thumbnail(url=data.thumb_url)

    embed.add_field(name="Features", value="\n".join(data.features), inline=False)

    embed.add_field(name="GitHub", value="https://github.com/LoCrealloc/covidbot", inline=False)

    embed.add_field(name="Entwickler", value="Dieser Bot wird von LoC entwickelt, bitte teile mir Fehler "
                                             "oder Verbesserungsvorschläge über die Issue-Seite auf dem "
                                             "GitHub-Repository des Bots mit!")

    ctx.channel.send(embed=embed)


@bot.command(name="stats")
async def stats(ctx: discord.Message):
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
                          color=0x088A08,
                          url="https://covid19api.com",
                          )

    embed.set_thumbnail(url=data.thumb_url)

    embed.add_field(name="Fälle weltweit", value=wwcases, inline=True)
    embed.add_field(name="Genesene weltweit", value=wwrecs, inline=True)
    embed.add_field(name="Tote weltweit", value=wwdeaths, inline=True)

    embed.add_field(name="Neue Fälle Deutschland", value=denewcases, inline=True)
    embed.add_field(name="Neue Genesene Deutschland", value=denewrecs, inline=True)
    embed.add_field(name="Neue Tote Deutschland", value=denewdeaths, inline=True)

    embed.add_field(name="Gesamt Fälle Deutschland", value=detotalcases, inline=True)
    embed.add_field(name="Gesamt Genesene Deutschland", value=detotalrecs, inline=True)
    embed.add_field(name="Gesamt Tote Deutschland", value=detotaldeaths, inline=True)

    embed.add_field(name="Daten", value="Diese Daten stammen von https://covid19api.com", inline=False)

    await ctx.channel.send(embed=embed)


bot.run(tokenid)
