import discord
import os
from dotenv import load_dotenv
import re

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

holding = 0.0

def getval(x):
    y = re.findall(r"[-+]?\d*\.\d+|\d+",x)
    newval = float(y[0])
    return newval

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(',holding'):
        global holding
        changedval = getval(message.content)
        newhold = holding + changedval
        holding = newhold
        printhold = str(newhold)
        await message.channel.send('Current Hold: ' + printhold + '%')
        return holding

    if message.content == (',total'):
        printhold = str(holding)
        await message.channel.send('Current Hold: ' + printhold + '%')

    if message.content ==(',reset'):
        holding = 0
        return holding

    if message.content.startswith(',change'):
        changedval = getval(message.content)
        newhold = holding - changedval
        holding = newhold
        printhold = str(newhold)
        await message.channel.send('Current Hold: ' + printhold + '%')
        return holding

    if message.content.startswith(',wafflebothelp'):
        await message.channel.send('Instructions:')
        await message.channel.send('For submiting damage, enter ",holding XX"')
        await message.channel.send('For checking current total, enter ",total"')
        await message.channel.send('For reseting total, enter ",reset"')
        await message.channel.send('For changing your current hold, enter your last hold amount as ",modify XX", and then re-enter your new hold as ",holding XX"')

client.run(TOKEN)
