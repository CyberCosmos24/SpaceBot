import discord
import logging
from discord import shard
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.bot import Bot
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



bot = commands.AutoShardedBot (shard_count = 1, command_prefix ="&", intents=intents, case_insensitive=True)

api_key = "a66b910bd3c8596a07b90052435da25f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@bot.event
async def on_ready(ctx):
    shard_id = ctx.guild.shard_id
    activity = discord.Streaming(name=f"&help | Shard:{shard_id}/1", url="https://www.twitch.tv/chillhopmusic")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    total_members = list(bot.get_all_members())
    total_channels = sum(1 for x in bot.get_all_channels())
    print('Guilds: ', len(bot.guilds))
    print('Large Guilds: ', sum(g.large for g in bot.guilds))
    print('Members: ', len(total_members))
    print('Channels: ', total_channels)
    print('Message Cache Size: ', len(bot.cached_messages))
    print(f"Welcome back Cosmos!")
    print(f"{bot.user}")
    print(f'Client = {round(bot.latency * 1000)}ms')
    print(f'All shards are online')
    channel = bot.get_channel(908770867440386068)
    await channel.send(f'Space has been restarted!')

 # this is good but you can make it better



for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        sname = str(ctx.guild.name)
        uuser = str(ctx.message.author)
        await ctx.send("`Command not found.`")
        print(sname)
        print(uuser)




@bot.command(aliases = ['l'],hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'{extension}')
    await ctx.send(f'Successfully loaded `{extension}`')
# Unload:
@bot.command(aliases = ['ul'],hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'{extension}')
    await ctx.send(f'Successfully unloaded `{extension}`')



@bot.event
async def on_guild_join(guild,ctx):
    guild = ctx.guild.name
    print(f"Space has joined {guild}")

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot.remove_command("help")

@bot.command()
async def help(ctx):

    embed = discord.Embed(title="Space Commands", description="",color=0x176cd5) #,color=Hex code
    embed.add_field(name="`&moderation`", value="Shows moderation commands",inline=False)
    embed.add_field(name="`&fun`" , value="Shows fun commands",inline=False)
    embed.add_field(name="`&utility`" , value="Shows utility commands",inline=False)
    embed.add_field(name="`&animal`" , value="Shows animal commands",inline=False)
    embed.add_field(name="`&action`" , value="Shows action commands",inline=False)
    embed.add_field(name="`&support`" , value="Support commands",inline=False)
    embed.set_author(name="Prefix &")
    embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
    
    await ctx.send(embed=embed)

@bot.command()
async def moderation(ctx):
    embed = discord.Embed(title="Space Moderation Commands", description="",color=0x176cd5)
    embed.add_field(name="clear", value="`&clear (amount)`",inline=False)
    embed.add_field(name="lockdown", value="`&lockdown : lockdowns the channel`",inline=False)
    embed.add_field(name="unlock", value="`&unlock : unlocks the channel`",inline=False)
    embed.add_field(name="kick", value="`&kick (member) [reason]`",inline=False)
    embed.add_field(name="ban", value="`&ban (member) [reason]`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
    

@bot.command()
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
    embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
    await ctx.send(embed=embed)


@bot.command()
async def utility (ctx):
    embed = discord.Embed(title="Utility Commands", description="",color=0x176cd5) 
    embed.add_field(name="server", value="`Tell information about a server`",inline=False)
    embed.add_field(name="userinfo", value="`&userinfo (member)`",inline=False)
    embed.add_field(name="botinfo", value="`Tell information about the bot`",inline=False)
    embed.add_field(name="status", value="`Gives the status of the bot`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}") 
    await ctx.send(embed=embed)

@bot.command()
async def animal (ctx):
    embed = discord.Embed(title="Animal Commands", description="",color=0x176cd5) 
    embed.add_field(name="whale", value="`Shows a picture of a whale` ",inline=False)
    embed.add_field(name="dog", value="`Shows a picture of a dog`",inline=False)
    embed.add_field(name="cat ", value="`Shows a picture of a cat`",inline=False)
    embed.add_field(name="bird ", value="`Shows a picture of a bird`",inline=False)
    embed.add_field(name="panda", value="`Shows a picture of a panda`",inline=False)
    embed.add_field(name="fox", value="`Shows a picture of a fox`",inline=False)
    embed.add_field(name="raccoon", value="`Shows a picture of a raccoon`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")  
    await ctx.send(embed=embed)
 
@bot.command()
async def action (ctx):
    embed = discord.Embed(title="Action Commands", description="",color=0x176cd5) 
    embed.add_field(name="hug", value="`Disabled`",inline=False)
    embed.add_field(name="kiss", value="`Kiss a user`",inline=False)
    embed.add_field(name="bonk", value="`Bonk a user`",inline=False)
    embed.add_field(name="pat", value="`Pat a user`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
    await ctx.send(embed=embed)


@bot.command()
async def support (ctx):
    embed = discord.Embed(title=" Support Commands", description="",color=0x176cd5)
    embed.add_field(name="invite", value="`invite the bot`",inline=False)
    embed.add_field(name="sdiscord", value="`support server`",inline=False)
    embed.set_footer(icon_url = f"{ctx.author.avata.url}", text = f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
    
@bot.command()
async def sdiscord (ctx):
    embed = discord.Embed(title="Support server", description="",color=0x176cd5) 
    embed.add_field(name="https://discord.gg/KUybC7tBA2", value="Feel free to join!",inline=False)
    await ctx.send(embed=embed)
 
@bot.command(aliases=["shard"], pass_context=True)
async def shardstats(ctx):
    shard_id = ctx.guild.shard_id
    shard = bot.get_shard(shard_id)
    shard_ping = f'{round(shard.latency * 1000)}ms'
    shard_servers = len([guild for guild in bot.guilds if guild.shard_id == shard_id])
    embed = discord.Embed(title=f'{bot.user.name} - Shard Stats')
    embed.add_field(name='Shard:', value=f'{shard_id}/1')
    embed.add_field(name='Shard Ping:', value=shard_ping)
    embed.add_field(name='Shard Servers:', value=shard_servers)
    await ctx.send(embed=embed)

bot.run('')
