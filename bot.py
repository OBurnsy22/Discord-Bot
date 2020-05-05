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
import urllib.request
import urllib.parse
import re

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
    embed.add_field(name='.smash', value='Peep some exclusive TOP-TIER gameplay', inline=False)
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

#gets random smash clip
@bot.command()
async def smash(ctx):
    clips = ['https://drive.google.com/file/d/11JZ9Q0mZ4MQyS5XTeSY89MnVSjOQPXtv/view',
             'https://drive.google.com/open?id=1IZTjOcCe6oU18pAUhn6Lz-6Q1jRzVTEG', 'https://drive.google.com/open?id=16TK7lgOoTxKCvOeEmIYGp-TELiRRk4bj', 'https://drive.google.com/open?id=150uvf9WSskMh879UqSrNBrUT3vTMxpUw', 'https://drive.google.com/open?id=1gIMYoyTm2ZRCyVKW6bVzDnEAXMFVww2U', 'https://drive.google.com/open?id=14C7Rk9yWnx9SxjJwtfiWwtmemZ9_pyEg',
             'https://drive.google.com/open?id=1eRI1zBcdaj0bSXr4SGkqahFKzQP7h5rW', 'https://drive.google.com/open?id=1aCNbcfVI3NV1EaD7BPLCFlxghJ-Oc7_b', 'https://drive.google.com/open?id=1Hh7xZMAYzcw-E3z7juj5X86ysJZgNPqe', 'https://drive.google.com/open?id=1Z0V91DS3ufnou9xNTo2_mpA0Xs19rOD_', 'https://drive.google.com/open?id=1SjygM3dmyIFXSg8EEXyGOBJZ-4C-2r9M', 
             'https://drive.google.com/open?id=1b1QOn3sfAtPcziZtkAD71Zr75qY_tVU0', 'https://drive.google.com/open?id=1IkJtYBSfpdRFvuKXFFYIJBGFihojnya0', 'https://drive.google.com/open?id=1C8N1Trds5q2gGoQVe59pgRqM8kEGWGe4', 'https://drive.google.com/open?id=1XSZFr70JVN0amCgNAN4GklzJtu_9IFxH', 'https://drive.google.com/open?id=10xlM6VHaUNbNwVc-1jBGe8kOtyh8Z-PC', 
             'https://drive.google.com/open?id=1JJ-qxs6gbmjdN3NIqClz02C0YQuxIxa5', 'https://drive.google.com/open?id=1FqEEbK5hqXNkBDTD2KqoZ5JVUz92hF99', 'https://drive.google.com/open?id=1G0M2zDcDkuosKuRBhe-_ypgqMCKK0PE7', 'https://drive.google.com/open?id=19cVaT5qFeRr3MGNpxwnzy_jfXQvc1SGQ', 'https://drive.google.com/open?id=1ifPnKRc6lA_Ypf88FcjcbJ1oahbBma_u', 
             'https://drive.google.com/open?id=1jgVnigQAmApSlSvDMrHzXyPdKZa5MShr', 'https://drive.google.com/open?id=1gATFhDU2FgoIhh0MeTorjhnbw9WLgzQ3', 'https://drive.google.com/open?id=1EDIT-8jhYlhP9ehHznMyz7tEc0cDpsHT', 'https://drive.google.com/open?id=1HXUkNs3W60QDQOHdSIrUEy22VcGa6-_j', 'https://drive.google.com/open?id=1b-4F8Y4ht3NlheqdArr--HtzDxSDPa1a', 
             'https://drive.google.com/open?id=1wQfLpMpo7luw5RUHxpHfjGtRIooEkmLv', 'https://drive.google.com/open?id=1-3ZwEfo354ILBZgmSKb_shl303beFyEc', 'https://drive.google.com/open?id=15yHeciIfsbqhB0V_4Bm8X9CwZmhZPKLY', 'https://drive.google.com/open?id=1o_0Q_w_ILwgTipxJ0A5NHIUnH8AfrFiL', 'https://drive.google.com/open?id=1cTWhexBwADDpw8H2nk6h4--45Og3Adiz', 
             'https://drive.google.com/open?id=1PiIrqDlCJPzI2X0mNzjMt4aNCy-6pbkK', 'https://drive.google.com/open?id=1f3Pv7oFkykljhIqtfJRC5zN_TXn2iSNq', 'https://drive.google.com/open?id=14zTphmCp2f6Vjf2R-1fv7SA7GajREiED', 'https://drive.google.com/open?id=11Dm8OoASOVYG-xZocKfc-uGTpkcWG7TT', 'https://drive.google.com/open?id=1rItXN6hJO2cJ5qqRCa0T9-tl50H8-Cqg', 
             'https://drive.google.com/open?id=1wHlDxci-jIBsW_aHODXetDWEiO6KHanK', 'https://drive.google.com/open?id=1L8h-moXUt8oDXOuX-RlQKaG-7KvoKT4Z', 'https://drive.google.com/open?id=17WDogVloq6-TaOCjGT15lw4gOzpnJSvS', 'https://drive.google.com/open?id=1pEcAfigGrZ5bML2VgUS1X0ozr4IRzle_', 'https://drive.google.com/open?id=1zKDsNq8e_VsgVX8f32PHBtiLVkU4-rqB', 
             'https://drive.google.com/open?id=1xHRHWEJYnM4Get4S_A8gJ45L351y5qyY', 'https://drive.google.com/open?id=1vIrAzxkwfKOwfHJ3Mw9HgM_h4-Taqpau', 'https://drive.google.com/open?id=1T0QKmIMeUbk8xxchFfltC4KIsV1wEiA3', 'https://drive.google.com/open?id=1MX7NcOPHQqTbO1LNyudnRH2pY3UO5wu6', 'https://drive.google.com/open?id=1RzH4EOEZo-hc7Xwb1QBHRZUK_sW36w-9', 
             'https://drive.google.com/open?id=1SIlNEk8y2XHldqyxYdky322l8cgjfwpb', 'https://drive.google.com/open?id=1_E5xXkjspe7396zbqTKM4QlpKj2qqPIz', 'https://drive.google.com/open?id=13O81Aady3FrvlRSFYuRP2gCugTfHAbeF', 'https://drive.google.com/open?id=1ADrA6W0AVVoqkLJnXepiXelQVOR7Czol', 'https://drive.google.com/open?id=1XjJEXqRCY1BJe5uAgLcE7k3YoBhNHJWD', 
             'https://drive.google.com/open?id=1Iyz_F8nCqXhawxfHZrGrdkTCbY06TH68', 'https://drive.google.com/open?id=1mTd8N9kOeGuuoVZludMM3szEN2dfHoFj', 'https://drive.google.com/open?id=18GlXDq8xIsDjQ-gOJ-EFRZUf35Mp_Avf', 'https://drive.google.com/open?id=1NhUNfsfYRAgrRV04z5H5UcHcidmLdDP9', 'https://drive.google.com/open?id=13cFP4SBv1j_xXqqnqrfZQpcvgADElBDc', 
             'https://drive.google.com/open?id=1UyuRvCWWQh3Ov5-ZaiEWAaVGz9tKBmoT', 'https://drive.google.com/open?id=1bBRtI9nNrAv-qkhayVd4ybAR7K8vQbAC', 'https://drive.google.com/open?id=18CO0laeXD1Ei5xDB4L9aaWSlQqAf6QQu', 'https://drive.google.com/open?id=1umbeRiuk7AK_I9tWjNZ0olbnDvV01Hy0', 'https://drive.google.com/open?id=1FWEN5142-7BEQ_A1_C8O77VxFeQYiLMq', 
             'https://drive.google.com/open?id=1eNNzMRpzp4WwUOdO38vtL0c0wPcV6V2a', 'https://drive.google.com/open?id=1A8x2UejZPij3nGAAt6ZsIBxVTeiydUjK', 'https://drive.google.com/open?id=1FSkk8Ny15MVLBRIA1YFlCkTnnduHpd2F', 'https://drive.google.com/open?id=1_F_O2DLggZjIaraWlXcYkTDe90Qvw2sC', 'https://drive.google.com/open?id=1HLQuTcXj9wSBgrBRzxHcBX5cghkI3XNp', 
             'https://drive.google.com/open?id=1N4RYTqBzakQpe1-SikirOGSizRETwIkv', 'https://drive.google.com/open?id=19aN3XzJCaLAQ4rNTP8vOF0VehWL8lq--', 'https://drive.google.com/open?id=1MRblMR4lAkdeZjuIqYqSDgodaG1v7yPA', 'https://drive.google.com/open?id=16Mu6_lhutFL73C8dE4RE9MaVxlplV9NE', 'https://drive.google.com/open?id=1EqyTo9sOmeETRyGbHvanPImGlp11OUkV', 
             'https://drive.google.com/open?id=1mfV_IjgU70pqz8sKGaXVWJ2NM0uISRpw', 'https://drive.google.com/open?id=1bY8m7gS9XbaIZjBRHSl5F4VRpffjyx1L', 'https://drive.google.com/open?id=16kiFmJM16wXnkAXpmdA6ZuJ0LHXR8lye', 'https://drive.google.com/open?id=1Yq1alvEeh2BZZRKVPc-LmhFtIw6nymf0', 'https://drive.google.com/open?id=1I7KSHHhRgolz-4ZuMDWKYxb5HlPE3tPX', 
             'https://drive.google.com/open?id=1mxtJz1nhuwMr3PfGQ8LfTg8NRhENJcpv', 'https://drive.google.com/open?id=18FBxAqbls6kz3_b7HNywsmYfVtHLuzx0', 'https://drive.google.com/open?id=1pIg9glFJYPaqVB-riw2JoSVdtvuam2K8', 'https://drive.google.com/open?id=1CjjjWvxDjHwqk3rAWmTrvpzBnYc0uvGx', 'https://drive.google.com/open?id=1-1kV2vgwZADeTh2iBzPb0hHW2qxxODph', 
             'https://drive.google.com/open?id=1qt1ILG16z4y3cH2qZBTCwlYcYznwI9A5', 'https://drive.google.com/open?id=11LK3-cbkYLrwi8z4d2IwFZpHy7PBjqXd', 'https://drive.google.com/open?id=1fsl80tHrsywpmpOAJo7_X79JOlFVMv6L', 'https://drive.google.com/open?id=15L25UPKEzoaW6FtgpI6_CiXw6cqUE54-', 'https://drive.google.com/open?id=1AdK-xkzO7Njrv_IAjr0HuIjYOn6Lc36O']
    await ctx.send(random.choice(clips))


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

#responds to certain messages in the chat
@bot.event
async def on_message(message):
    if message.author.id == 208835703235149824:
        emojis = ['(ノಠ益ಠ)ノ彡┻━┻', 'ヽ( ಠ益ಠ )ﾉ', '(-■_■)', '⊜_⊜', '눈_눈']
        x = random.randint(1, 2)
        if x == 1:
            await message.channel.send(random.choice(emojis))
    await bot.process_commands(message)

#runs bot with its respective token
bot.run(bot.config_token)
