import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os




Papa=discord.Client()
Papa= commands.Bot(command_prefix="/")

#main:programme
@Papa.event
async def on_ready():
    print("Cool")
    await Papa.change_presence(status=discord.Status.online,activity=discord.Game("Naughty"))
@Papa.command()
async def game(ctx):
    while(True):
        await ctx.send("Do your homework")
@Papa.command()
async def sleep(ctx):
    await ctx.send("Good Bye")
    await Papa.change_presence(status=discord.Status.idle,activity=discord.Game("Zzzzzzz..."))
    await exit()
    await print('hi')
@Papa.command()
async def rules(ctx):
  await ctx.send("1. the first command is /game, i will spam :Do your homework")
  await Papa.change_presence(status=discord.Status.online,activity=discord.Game("Explaining"))
  await ctx.send("2. The second and the final command is /sleep it will stop the programm")
keep_alive()
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
Papa.run(TOKEN)