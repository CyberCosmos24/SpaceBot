
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
bot = commands.AutoShardedBot (shard_count=3,command_prefix ="&", intents=intents, case_insensitive=True)
api_key = "a66b910bd3c8596a07b90052435da25f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"



class FunCog():
    def __init__(self, bot):
        self.bot = bot 


@commands.command()
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


@commands.command(aliases=['8ball'])
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


@commands.command()
async def coinflip (ctx):
  responses = ['Heads','Tails']
  await ctx.send(f'{random.choice(responses)}')


@commands.command()
async def joke (ctx):
  responses = ['What kind of car runs on leaves? An autumn-mobile!','Why was the math teacher late to work? She took the rhombus.','What do you give to a sick lemon? Lemon aid!','What do you call a fish with no eyes? A fsh.']
  await ctx.send(f'{random.choice(responses)}')












@commands.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await bot.wait_for('message', check=check)).content

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




@commands.command()
async def members(ctx):
    gname = str(ctx.guild.name)
    await ctx.send(f" {gname} member count is {(ctx.guild.member_count)}")
    


@commands.command(aliases=['av'])
async def avatar(ctx, user : discord.Member=None):
    
    await ctx.send(user.avatar_url)
@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} please mention a member!")
    else: raise(error)

@commands.command()
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
    message = await bot.wait_for("message", check=check)
    choice = message.content.lower()
    if choice == "t":
        await ctx.send(f"{random.choice(truth_items)}")
    if choice == "d":
        await ctx.send(f"{random.choice(dare_items)}")







@commands.command()
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





def setup(bot):
    bot.add_cog(FunCog(bot))