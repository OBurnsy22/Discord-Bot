'''
Author: Matthew Burns
DS: OBurnsy22#7248
4/30/2020
'''

import discord
import discord.utils
from discord.ext import commands
from pathlib import Path
import json
import random
import urllib.parse

#ensures bot is in current working directory
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

#setup
secret_file = json.load(open(cwd+'/bot_config/config.json'))  #loads json file
bot = commands.Bot(command_prefix='.', case_insensitive=True)  #hsetting up the bot
bot.config_token = secret_file['token'] #configure the secret token
bot.remove_command("help")

#displays this on terminal startup, as well as when it is in server
@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: .\n-----")
    await bot.change_presence(activity=discord.Game(name=f"Type '.help', for a list of commands!"))

#displays list of commands for BeanBot
@bot.command()
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.purple())
    embed.set_author(name='Description of commands for BeanBot, exclude brackets when typing commands')
    embed.add_field(name='.hi', value='Says Hello to user who promted command', inline=False)
    embed.add_field(name='.ping', value='Checks your latency on discord', inline=False)
    embed.add_field(name='.choose [Enter choices]', value='Chooses randomly between inputted choices', inline=False)
    embed.add_field(name='.google [You know what to put here]', value='Googles whatever is inputted after the command', inline=False)
    embed.add_field(name='.users', value='Displays current active users', inline=False)
    embed.add_field(name='.rng [num1] [num2]', value='Generates random number between specified num1/num2, defualt values are 1 and 10', inline=False)
    embed.add_field(name='.coin', value='Flips a coin', inline=False)
    embed.add_field(name='.dice', value='Rolls a dice', inline=False)
    embed.add_field(name='.ranlink', value='Get a random link from the Beanboy CACHE', inline=False)
    embed.add_field(name='.clear [num]', value='Clears a specified number of messages from the channel its used in, default value is 5 [ADMIN ONLY]', inline=False)
    embed.add_field(name='.exterminate @[name]', value='Kicks specified member from server [ADMIN ONLY]', inline=False)
    await ctx.send(embed=embed)

#simple command, says hi back to user that prompted command
@bot.command()
async def hi(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

#tests latency on discord
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong: **{}ms**".format(round(bot.latency * 1000, 2)))

#Get a random link from the Beanboy CACHE
@bot.command()
async def ranlink(ctx):
    f_list = ['https://i.imgur.com/8nfH8nz.jpg',
              'https://imgur.com/jVNd5NH', 'https://i.imgur.com/nXQ9pOx.jpg', 'https://i.imgur.com/lrDstZ4.jpg', 'https://imgur.com/YjI1Y8X', 'https://imgur.com/c3Tul49', 'https://imgur.com/DwLgleM', 'https://imgur.com/zhml5ti', 'https://imgur.com/BocIOO3', 'https://imgur.com/WWTao4K',
              'https://imgur.com/ciuzh5c', 'https://imgur.com/0ctHpVe', 'https://imgur.com/XHWbtIB', 'https://imgur.com/HiG9num', 'https://imgur.com/yQZjyWD', 'https://imgur.com/jcBFXXc', 'https://imgur.com/ffQafqF', 'https://imgur.com/xfaYTVx', 'https://imgur.com/VF77Btl', 
              'https://imgur.com/BH0t2ud', 'https://imgur.com/M2yklMJ', 'https://imgur.com/xC1d1lg', 'https://imgur.com/7OTH2CM', 'https://imgur.com/T0abWMH', 'https://imgur.com/8Fcz1UX', 'https://imgur.com/UZC6QPf', 'https://imgur.com/EKvSVuM', 'https://imgur.com/PZe9gjX',
              'https://imgur.com/JqdrrcF', 'https://imgur.com/sviCJob', 'https://imgur.com/HhL4pCV', 'https://imgur.com/qgV4ZJd', 'https://imgur.com/m3QpIMA', 'https://imgur.com/OqAnnSQ', 'https://imgur.com/RKA4YMa', 'https://imgur.com/12zxq0r', 'https://imgur.com/ViG6XVR',
              'https://imgur.com/bZQBwn4', 'https://imgur.com/Qq8XAJz', 'https://imgur.com/lUbjTr0', 'https://imgur.com/nphU2nH', 'https://imgur.com/WAjGgS5', 'https://imgur.com/pHEyNGX', 'https://imgur.com/UIaRMgK', 'https://imgur.com/CdNnPkD', 'https://imgur.com/e3nVtZF',
              'https://imgur.com/XzvTeqE', 'https://imgur.com/j3P2OBW', 'https://imgur.com/Ynvh3B6', 'https://media.discordapp.net/attachments/536110922843029506/555187712538443776/unknown.png', 'https://cdn.discordapp.com/attachments/320700701967777803/542579030289940505/image0.jpg',
              'https://cdn.discordapp.com/attachments/320700701967777803/542572679224360980/image0.jpg', 'https://cdn.discordapp.com/attachments/320700701967777803/486716183924441088/unknown.png', 'https://www.youtube.com/watch?v=rgX_DGVThzQ', 'https://www.youtube.com/watch?v=_qG9bSebOho',
              'https://www.youtube.com/watch?v=k6yHal3LhlQ', 'https://www.youtube.com/watch?v=Gonv4FuA5us', 'https://www.youtube.com/watch?v=zTXrH0m6I_g']
    await ctx.send(random.choice(f_list))


#googles whatever is inputted after the command
@bot.command()
async def google(ctx, *, searchquery : str):
    searchquerylower = searchquery.lower()
    if searchquerylower.startswith('images'):
        await ctx.send('<https://www.google.com/search?tbm=isch&q={}>'.format(urllib.parse.quote_plus(searchquery[7:])))
    else:
        await ctx.send('<https://www.google.com/search?q={}>'.format(urllib.parse.quote_plus(searchquery)))

#kicks specified member from server [ADMIN ONLY]
@bot.command()
@commands.has_role('Admin')
async def exterminate(ctx, member : discord.Member, *, reason=None):
    if member.id == 135215722157572096:
        await ctx.send("I will not kick my creator")
    else:
        await member.kick(reason=reason)

#chooses randomly between inputted options
@bot.command()
async def choose(ctx, *choices : str):
    await ctx.send((random.choice(choices)) + ', I choose you!')

#flips a coin and prints the outcome
@bot.command()
async def coin(ctx):
    outcome = ['Heads', 'Tails']
    await ctx.send(random.choice(outcome))

#rolls a dice and prints the outcome
@bot.command()
async def dice(ctx):
    outcome = ['1', '2', '3', '4', '5', '6']
    await ctx.send(random.choice(outcome))

#returns the number of members in a given server
@bot.command()
async def users(ctx):
    server_id = bot.get_guild(320700701967777803)
    await ctx.send(f"{server_id} has {server_id.member_count} active members.")

#generates random number between inputted num1/num2 
@bot.command()
async def rng(ctx, num1=1, num2=10):
    if num2 < num1:
        await ctx.send("num2 must be larger than num1") 
    else:
        await ctx.send(random.randint(num1, num2))

#used to rename the bot [ADMIN ONLLY] [SECRET]
@bot.command()
@commands.has_role('Admin')
async def rename(ctx, name):
    await bot.user.edit(username=name)

#clears specified number of commands from whatever channel it's called in [ADMIN ONLY]
@bot.command()
@commands.has_role('Admin')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#greeting banner when someone new joins the server
@bot.event
async def on_member_join(member):
    messageChannel = discord.utils.get(member.guild.channels, name='messages')
    await messageChannel.send(f"Welcome to the server {member.mention}!")

#error handler
@bot.event
async def on_command_error(error, ctx):
        await error.send("Error: No such command, or missing required arguments")

@bot.event
async def on_message(message):
    await bot.process_commands(message)


#runs bot with its respective token
bot.run(bot.config_token)