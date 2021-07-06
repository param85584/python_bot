import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def ping(ctx):
    await ctx.send('Hello')

client.run('ODYwMTE4Mzc5OTY4MjAwNzA0.YN2lqg.a4Z9xLmNvHtz3P5R9rRIXpX6tI8')