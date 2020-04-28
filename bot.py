import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():  #when the bot is ready from discord
    print('Bot is ready.')

client.run('NzA0NTA1NDI2OTI1ODQ2Njcx.XqeH4g.wpZg2MCmQ2ZblBt_CLj2e6fXOt8')  #once the client is created and has an event to look for, it runs (insert bot token)
