import discord
from discord.ext import commands
#import stkap

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    #smsg = stkap.func()
    #msg = await client.wait_for('message', check=check)
    #await channel.send('Hello {.author}!'.format(msg))
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):

        await message.channel.send('hello')



client.run('ODYwMTE4Mzc5OTY4MjAwNzA0.YN2lqg.a4Z9xLmNvHtz3P5R9rRIXpX6tI8')