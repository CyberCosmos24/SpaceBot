import discord
from discord import shard
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command
import random
import json
import os
import datetime, time
from datetime import datetime
import aiohttp
import requests   
import sys
import secrets
from discord.member import Member
import socket
import arrow
import discord
import humanfriendly
import psutil
import asyncio
intents = discord.Intents.default()  
intents.members = True             



client = commands.AutoShardedBot (shard_count=3,command_prefix ="&", intents=intents, case_insensitive=True)

api_key = "a66b910bd3c8596a07b90052435da25f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@client.event
async def on_ready():
    activity = discord.Streaming(name="&help", url="https://www.twitch.tv/chillhopmusic")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    channel = client.get_channel(870049723535474698)
    total_members = list(client.get_all_members())
    total_channels = sum(1 for x in client.get_all_channels())
    print('Guilds: ', len(client.guilds))
    print('Large Guilds: ', sum(g.large for g in client.guilds))
    print('Chunked Guilds: ', sum(g.chunked for g in client.guilds))
    print('Members: ', len(total_members))
    print('Channels: ', total_channels)
    print('Message Cache Size: ', len(client.cached_messages))
    await channel.send(f'Space has been restarted!')
    print(f"Welcome back Cosmos!")
    print(f"{client.user}")
    print(f'Client = {round(client.latency * 1000)}ms')
    print(f'All shards are online')

@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        sname = str(ctx.guild.name)
        uuser = str(ctx.message.author)
        await ctx.send("`Command not found.`")
        print(sname)
        print(uuser)




#===============OWNER============
@client.command()
@commands.is_owner()
async def speak(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")
@speak.error
async def speak_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} you can not use this command.")
    else: raise(error)

@client.command()
@commands.is_owner()
async def ping(ctx):
    shard_id = ctx.guild.shard_id
    shard = client.get_shard(shard_id)
    shard_ping = f'{round(shard.latency * 1000)}ms'

    await ctx.send(f'Client: `{round(client.latency * 1000)}ms`')
    await ctx.send(f'Shard: `{shard_ping}`')
   

  


@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} you can not use that command.")
    else: raise(error)

@client.command()
@commands.is_owner()
async def add(ctx, *,  member:discord.User=None):
    message = ctx.message
    await ctx.send(f"{member} has been added to the list")


@client.command()
@commands.is_owner()
async def spaceadd(ctx, *,  member:discord.User=None):
    await ctx.send(f"{member} has been added to `s6823_Guilds:gamma.bloom.host`")


@client.command()
@commands.is_owner()
async def cosmos(ctx):
    await ctx.send(f"Our favorite coding guy! <3") 



@client.command()
@commands.is_owner()
async def peppermint(ctx):
    await ctx.send(f"@ᖴIGᗰEᑎT#6858 is Cosmos bitch") 
@peppermint.error
async def peppermint_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} you can not use that command")
    else: raise(error)






@client.command()
@commands.is_owner() # Checks if the bot owner exectued the command
async def restart(ctx):
    await ctx.send("Client is restarting...")
    await client.logout() # Logging outyyyyyyyyyyyyy
   

@client.command()
@commands.is_owner()
async def dm(ctx, user: discord.User, *, value):

    await user.send(f"**{value}**")
    await ctx.send(f"Message Sent!")

@client.command()
async def paro(ctx):
    id = str(ctx.author.id)
    if id == '463932071451164673':
        await ctx.send('paro is the tall and we love him. <3')
        
    else:
        await ctx.send(f" {ctx.message.author} you can not use that command")


@client.command()
async def pping(ctx):
    id = str(ctx.author.id)
    if id == '463932071451164673':
        await ctx.send(f'Websocket ping {round(client.latency * 10000)}ms')
        
    else:
        await ctx.send(f" {ctx.message.author} you can not use that command")

@client.command()
@commands.is_owner() # Checks if the bot owner exectued the command
async def rr(ctx):
    await ctx.send("Testing") 
   



#=====================FUN=================



@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=discord.Colour.blue(),
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQuR-ZAJLPssLQvBFN0cntycP24gDRVqTGHA&usqp=CAU")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
        await channel.send(embed=embed)
    else:
        await channel.send("City not found.")
@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"Enter a city!")
    else: raise(error)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):

  responses = ['It is certain.', 
                'Without a doubt',
                'Yes',
                'No',
                'Discord says no',
                'Count on it',
                'Nope',
                'Go think about it',
                'I do not know',
                'Space says yes',
                'Cosmos says no',
                ''
  ]
  await ctx.send(content=f'Question: {question}\n:8ball: says: {random.choice(responses)}')


@client.command()
async def coinflip (ctx):
  responses = ['Heads','Tails']
  await ctx.send(f'{random.choice(responses)}')


@client.command()
async def joke (ctx):
  responses = ['What kind of car runs on leaves? An autumn-mobile!','Why was the math teacher late to work? She took the rhombus.','What do you give to a sick lemon? Lemon aid!','What do you call a fish with no eyes? A fsh.']
  await ctx.send(f'{random.choice(responses)}')












@client.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, we tied. I will win next time!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'Paper beats rock. You win!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock! Get it. ;)\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. Rigged. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")




@client.command()
async def members(ctx):
    gname = str(ctx.guild.name)
    await ctx.send(f" {gname} member count is {(ctx.guild.member_count)}")
    


@client.command(aliases=['av'])
async def avatar(ctx, user : discord.Member=None):
    
    await ctx.send(user.avatar_url)
@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} please mention a member!")
    else: raise(error)

@client.command()
async def td(ctx):
    truth_items = ['If you could be invisible, what is the first thing you would do?',
    'If a genie granted you three wishes, what would you ask for?',
    'What is the longest you have ever slept?',
    'What animal do you think you most look like?',
    'What was your favorite childhood show?',
    'What person do you text the most?',
    'Who is your celebrity crush?',
    '']
    dare_items = ['Eat A Dry Pack Of Noodles.',
    ' Dance With No Music For 1 Minute.',
    'Give Someone Your Phone And Let Them Send One Text To Anyone In Your Contacts.',
    ' Let The Person To Your Left Draw On Your Face With A Pen.',
    'Attempt To Do A Magic Trick.',
    'Break Two Eggs On Your Head.',
    'Go Outside And Pick Exactly 40 Blades Of Grass With A Pair Of Tweezers.',
    ' Go Outside And Howl, Bark, And Meow All For 2 Minutes.',
    'Make A Sandwich While Blindfolded.']
    await ctx.send("Please type t for truth and d for dare.")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ("t", "d")
    message = await client.wait_for("message", check=check)
    choice = message.content.lower()
    if choice == "t":
        await ctx.send(f"{random.choice(truth_items)}")
    if choice == "d":
        await ctx.send(f"{random.choice(dare_items)}")







@client.command()
@commands.has_permissions(administrator=True)
async def poll(ctx, *, text):
    number = {1: ":one:", 2: ":two:", 3: ":three:", 4: ":four:", 5: ":five:", 6: ":six:", 7: ":seven:", 8: ":eight:",9: ":nine:"}
    emoji = {1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}
    count = 1
    countemoji = 1
    split = text.split('" "')
    split[-1] = split[-1].replace("\"", "")
    question = split.pop(0).replace("\"", "")
    if len(split) > 9 or len(split) < 2:
        await ctx.send("> You must have at least 2 answers and at most 9 answers.")
    else:
        descembed = "\n"
        numberRes = len(split)
        while count <= numberRes:
            descembed += number[count] + " " + split[count - 1] + "\n"
            count += 1
        embedpoll = discord.Embed(title="**" + question + ":**", description=descembed, colour=discord.Colour.random()) #You can select another colour by replacing green by another colour. For example: discord.Colour.blue() // Here's the link for the colors: https://discordpy.readthedocs.io/en/latest/api.html?#colour
        embed = await ctx.send(embed=embedpoll)
        while countemoji <= numberRes:
            await embed.add_reaction(emoji[countemoji])
            countemoji += 1
        await ctx.message.delete()
    
@poll.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"You need ADMINISTARTOR permission to use this command! ")
    else: raise(error)
#=======================CUSTOM===================

@client.command() # Hide custome command 
async def meow (ctx):
    id = str(ctx.author.id)
    if id == '578699592116207629':

        embed = discord.Embed(title="Meow motherfucker :heart:", description="",color=0x0FEBE1)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Only Hide can use that command!")



@client.command() # Candy custom command
async def candy(ctx):
    id = str(ctx.author.id)
    if id == '424792930461417475':
        await ctx.send("Candy is a little one! :hearts:  ") 
    else:
        
             await ctx.send("Only Candy can use that command!")

@client.command() 
async def train(ctx):
    await ctx.send("choo choo :train: :rainbow: :sparkling_heart: ")


@client.command() # Soccer Mom custom command 
async def uglybean(ctx):
    id = str(ctx.author.id)
    if id == '867986155684126750':
        await ctx.send("Thats soccer mom! :soccer: ") 

@client.command() # Spicyy
async def spieccyy(ctx):
    id = str(ctx.author.id)
    if id == '812528856363696138':
        await ctx.send("He's Spieccyy")

    else:   
         await ctx.send("Only Spiecy can use that command!")

@client.command() # Dumpy 
async def dork(ctx):
 id = str(ctx.author.id)
 if id == '660609569525071883':
        await ctx.send("❤️ she is a Valorant god and we love her lots! ❤️ ")
 else:   
         await ctx.send("Only Dork can use that command!")


@client.command() # Snowy COmmand
async def snow(ctx):
 id = str(ctx.author.id)
 if id == '269684770680602624':
        await ctx.send("Snowy is amazing! ❤️ ")
 else:   
         await ctx.send("Only Snowy can use that command!")

@client.command()
async def racc(ctx):
    id = str(ctx.author.id)
    if id == '290649060002496512':
        await ctx.send(f'Thats a dirty raccoon bitch')
        
    else:
        await ctx.send(f" {ctx.message.author} you can not use that command")


#-============================ROLEPLAY========
@client.command(pass_context=True)
async def kiss(ctx, member: discord.Member=None):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://neko-love.xyz/api/v1/kiss')
      kissjson = await request.json()
      author = ctx.author.mention
      mention = member.mention

   embed = discord.Embed(description=f"{author} gave {mention} a hug", color=discord.Color.random())
   embed.set_image(url=kissjson['link'])
   await ctx.send(embed=embed)


@client.command(pass_context=True)
async def hug(ctx, member: discord.Member=None):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animu/hug')
      hugjson = await request.json()
      author = ctx.author.mention
      mention = member.mention

   embed = discord.Embed(description=f"{author} gave {mention} a hug", color=discord.Color.random())
   embed.set_image(url=hugjson['link'])
   await ctx.send(embed=embed)


@client.command(pass_context=True)
async def bonk(ctx, member: discord.Member=None):
        
        author = ctx.author.mention
        mention = member.mention
        
        bonk = "**{0} bonked {1}!**"
        
        choices = ['',
         'https://tenor.com/view/klee-klee-bonk-head-bonk-klee-gif-20738643', 
         'https://media.tenor.com/images/ac368de0a352fe2722bf100060da07e9/tenor.gif',
          'https://media.tenor.com/images/805df9431b3ad6956eecc87ace9fb150/tenor.gif', 
          'https://media.tenor.com/images/66921099d8b114b749f75b34a5a95ea2/tenor.gif',
          'https://media.tenor.com/images/ecc9c67c1e55ca221fb2a2e8056dc2db/tenor.gif',
          'https://media.tenor.com/images/9b1ca6f99af29db6a74077bbc36f7008/tenor.gif',
          'https://media.tenor.com/images/de9535e81034a889303bb2db0b0c6a15/tenor.gif',
          'https://media.tenor.com/images/f7619f7dca7db8c53ca739820aebdf27/tenor.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=bonk.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)



    
#==================MODERATION==============
    





 
@client.command()
@commands.has_permissions(manage_channels=True) 
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in lockdown. To unlock this channel do `&unlock`***")
@lockdown.error
async def lockdown_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("`You can not use this command`")
    else: raise(error)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")
@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("`You can not use this command`")
    else: raise(error)


@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0): 
   await ctx.channel.purge(limit=amount)                                     
   await ctx.send(f'{ctx.message.author} have deleted {amount} messages!')                         
    
@clear.error 
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("`You need the manage_message permission`")
    else: raise(error)


@client.command(description="ban a user with specific reason (only admins)") #kick
@commands.has_permissions(ban_members=True)
async def ban (ctx, member:discord.User=None, reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot ban yourself!""")
    await ctx.guild.ban(member, reason=reason)
    print(member)
    print(reason)
    await ctx.channel.send(f"{member} has been banned!")
 except:
    await ctx.send(f"Error banning user {member}")


 
    
@client.command(description="kicks a user with specific reason ") #kick
@commands.has_permissions(kick_members=True)
async def kick (ctx, member:discord.User=None, reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("```You cannot kick yourself!```") 
    await ctx.guild.kick(member, reason=reason)
    print(member)
    print(reason)
    await ctx.channel.send(f"{member} is kicked!")
 except:
    await ctx.send(f"{ctx.author} you can not kick user {member}! ")



@client.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.send("Nuked the Channel sucessfully!")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")


#===============================INFO=====================

@client.command(pass_context=True)
async def status(ctx):
    general_text = f'Latency: **{round(client.latency * 1000)}ms**'
    general_text += f'\nPlatform: **{sys.platform.upper()}**'
    general_text += f'\nStarted: **{arrow.get(psutil.boot_time()).humanize()}**'
    cpu_clock = psutil.cpu_freq()
    cpu_clock = round(cpu_clock.current, 2) if cpu_clock else '???'
    cpu_text = f'Count: **{psutil.cpu_count()} ({psutil.cpu_count(logical=False)})**'
    cpu_text += f'\nUsage: **{psutil.cpu_percent()}%**'
    cpu_text += f'\nClock: **{cpu_clock} MHz**'
    avail_mem = psutil.virtual_memory().available
    total_mem = psutil.virtual_memory().total
    used_mem = humanfriendly.format_size(total_mem - avail_mem, binary=True)
    total_mem = humanfriendly.format_size(total_mem, binary=True)
    sigma_mem = humanfriendly.format_size(psutil.Process(os.getpid()).memory_info().rss, binary=True)
    mem_text = f'Me: **{sigma_mem}**'
    mem_text += f'\nUsed: **{used_mem}**'
    mem_text += f'\nTotal: **{total_mem}**'
    response = discord.Embed(color=0x176cd5)
    response.add_field(name='General', value=general_text)
    response.add_field(name='CPU', value=cpu_text)
    response.add_field(name='Memory', value=mem_text)
    await ctx.send(embed=response)

@client.command(pass_context=True)
async def botinfo (ctx):


    authors = f'Cosmos#2424,Hawk#5651'
    env_text = f'Language: Python {sys.version.split()[0]}'
    env_text += f'\nLibrary: discord.py {discord.__version__}'
    env_text += f'\nPlatform: {sys.platform.upper()}'
    sas_text = f'Guilds: {len(client.guilds)}'
    sas_text += f'\nMembers: {len(client.users)}'
    sas_text += f'\nCommands: {len(client.commands)}'
    Embed = discord.Embed(title="Space Bot Info",color=0x176cd5)
    Embed.add_field(name='Authors', value=authors)
    Embed.add_field(name='Environment', value=env_text)
    Embed.add_field(name='Stats', value=sas_text)
    await ctx.send(embed=Embed)




@client.command(aliases=['serverinfo'])
async def server(ctx):
    datetime_format = "%a, %d %b %Y"
    
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)
    

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=(0x176cd5)
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name=" Owner", value=owner, inline=True)
    embed.add_field(name=' Created At', value=ctx.guild.created_at.__format__('%a, %d. %b %Y @ %H:%M:%S'), inline=True)
    embed.add_field(name=" Server ID", value=id, inline=True)
    embed.add_field(name=" Region", value=region, inline=True)
    embed.add_field(name=" Member Count", value=memberCount, inline=True)
    embed.add_field(name=" Bot Count", value=len([bot for bot in ctx.guild.members if bot.bot]), inline=True)
    embed.add_field(name=' Verification Level', value=str(ctx.guild.verification_level), inline=False)
    embed.add_field(name=" Text Channels", value=len(ctx.guild.text_channels), inline=True)
    embed.add_field(name=" Voice Channels", value=len(ctx.guild.voice_channels), inline=True)
    embed.add_field(name="Catergories", value=len(ctx.guild.categories), inline=True)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    


    await ctx.send(embed=embed)


@client.command(aliases=['user'],pass_context=True)
async def userinfo(ctx, user: discord.User = None):
    """Displays user information."""
    if user == None: ##if no user is inputted
        user = ctx.author ##defines user as the author of the message
    embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
    embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Roles", value=len(user.roles))
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Created", value=user.created_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
 
    await ctx.send(embed=embed)



@userinfo.error
async def userinfo_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.BadArgument):
        return await ctx.send("Couldn't find that user.")

@client.command(aliases=["shard"], pass_context=True)
async def shardstats(ctx):
    shard_id = ctx.guild.shard_id
    shard = client.get_shard(shard_id)
    shard_ping = f'{round(shard.latency * 1000)}ms'
    shard_servers = len([guild for guild in client.guilds if guild.shard_id == shard_id])

    embed = discord.Embed(title=f'{client.user.name} - Shard Stats')
    embed.add_field(name='Shard:', value=f'{shard_id}/3')
    embed.add_field(name='Shard Ping:', value=shard_ping)
    embed.add_field(name='Shard Servers:', value=shard_servers)

    await ctx.send(embed=embed)






    
#=================ANIMAL=================

@client.command()
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      dogjson = await request.json()
      # This time we'll get the fact request as well!

   embed = discord.Embed(title="KITTY! 😻", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)



@client.command()
async def raccoon(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/racoon')
      dogjson = await request.json()
    

   embed = discord.Embed(title="Raccoon!", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)



@client.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
     

   embed = discord.Embed(title="Doggie!! 🐕", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])

   await ctx.send(embed=embed)

@client.command()
async def whale(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/whale')
      dogjson = await request.json()
     

   embed = discord.Embed(title="Whale! 🐳", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)

@client.command()
async def bird (ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/bird')
      dogjson = await request.json()
      

   embed = discord.Embed(title="Bird! 🐦", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)


@client.command()
async def panda (ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/panda')
      dogjson = await request.json()
    

   embed = discord.Embed(title="Panda! 🐼", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)

@client.command()
async def fox (ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/fox')
      dogjson = await request.json()
     

   embed = discord.Embed(title="Fox! 🦊", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)



#=================HELP=================


client.remove_command("help")
@client.command()
async def help(ctx):

    embed = discord.Embed(title="Space Commands", description="",color=0x176cd5) #,color=Hex code
    embed.add_field(name="`&moderation`", value="Shows moderation commands",inline=False)
    embed.add_field(name="`&fun`" , value="Shows fun commands",inline=False)
    embed.add_field(name="`&utility`" , value="Shows utility commands",inline=False)
    embed.add_field(name="`&animal`" , value="Shows animal commands",inline=False)
    embed.add_field(name="`&action`" , value="Shows action commands",inline=False)
    embed.add_field(name="`&support`" , value="Support commands",inline=False)
    embed.set_author(name="Prefix &")
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    
    await ctx.send(embed=embed)

@client.command()
async def moderation(ctx):
    embed = discord.Embed(title="Space Moderation Commands", description="",color=0x176cd5)
    embed.add_field(name="clear", value="`&clear (amount)`",inline=False)
    embed.add_field(name="lockdown", value="`&lockdown : lockdowns the channel`",inline=False)
    embed.add_field(name="unlock", value="`&unlock : unlocks the channel`",inline=False)
    embed.add_field(name="kick", value="`&kick (member) [reason]`",inline=False)
    embed.add_field(name="ban", value="`&ban (member) [reason]`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    
  
    


    await ctx.send(embed=embed)
    

@client.command()
async def fun (ctx):
    embed = discord.Embed(title="Space Fun Commands", description="",color=0x176cd5) 
    embed.add_field(name="8ball", value="`&8ball (question)`",inline=False)
    embed.add_field(name="coinflip", value="`Flips a coin` ",inline=False)
    embed.add_field(name="poll", value='`&poll <"Question"> <"Answer1"> - <"Answer9"> `',inline=False)
    embed.add_field(name="joke", value='`Tells a random joke`',inline=False)
    embed.add_field(name="rps", value='`Play a game of rock ,paper ,scissors `',inline=False)
    embed.add_field(name="avatar", value='`Sends the user avatar `',inline=False)
    embed.add_field(name="td", value='`Play truth or dare `',inline=False)
    embed.add_field(name="weather", value='`&weather [city] `',inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    

    await ctx.send(embed=embed)


@client.command()
async def utility (ctx):
    embed = discord.Embed(title="Utility Commands", description="",color=0x176cd5) 
    embed.add_field(name="server", value="`Tell information about a server`",inline=False)
    embed.add_field(name="userinfo", value="`&userinfo (member)`",inline=False)
    embed.add_field(name="botinfo", value="`Tell information about the bot`",inline=False)
    embed.add_field(name="status", value="`Gives the status of the bot`",inline=False)
   
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
   
    await ctx.send(embed=embed)

@client.command()
async def animal (ctx):
    embed = discord.Embed(title="Animal Commands", description="",color=0x176cd5) 
    embed.add_field(name="whale", value="`Shows a picture of a whale` ",inline=False)
    embed.add_field(name="dog", value="`Shows a picture of a dog`",inline=False)
    embed.add_field(name="cat ", value="`Shows a picture of a cat`",inline=False)
    embed.add_field(name="bird ", value="`Shows a picture of a bird`",inline=False)
    embed.add_field(name="panda", value="`Shows a picture of a panda`",inline=False)
    embed.add_field(name="fox", value="`Shows a picture of a fox`",inline=False)
    embed.add_field(name="raccoon", value="`Shows a picture of a raccoon`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
   
    await ctx.send(embed=embed)
 
@client.command()
async def action (ctx):
    embed = discord.Embed(title="Action Commands", description="",color=0x176cd5) 
    embed.add_field(name="hug", value="`Hug a user`",inline=False)
    embed.add_field(name="kiss", value="`Kiss a user`",inline=False)
    embed.add_field(name="bonk", value="`Being worked on`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    await ctx.send(embed=embed)


@client.command()
async def support (ctx):
    embed = discord.Embed(title=" Support Commands", description="",color=0x176cd5)
    embed.add_field(name="invite", value="`invite the bot`",inline=False)
    embed.add_field(name="sdiscord", value="`support server`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
    
@client.command()
async def sdiscord (ctx):
    embed = discord.Embed(title="Support server", description="",color=0x176cd5) 
    embed.add_field(name="https://discord.gg/KUybC7tBA2", value="Feel free to join!",inline=False)
    await ctx.send(embed=embed)
 
   



@client.command(pass_context=True)
async def invite(ctx):

        invite_url = f'https://discord.com/oauth2/authorize?client_id=847532364606210099&scope=bot&permissions=3422944343'

 
        inv_title = 'Click here to invite me.'
        sigma_image = 'https://cdn.discordapp.com/avatars/847532364606210099/c63c8d706794b6424cca64f8b950145b.webp?size=1024'
        Embed = discord.Embed(color=0x176cd5 ).set_author(name=inv_title, icon_url=sigma_image, url=invite_url)
        await ctx.send(embed=Embed)










client.run('ODQ3NTMyMzY0NjA2MjEwMDk5.YK_cBg.hp4D_YhgvjCAxLrgiEw_B0W7ejQ')