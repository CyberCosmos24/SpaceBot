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


@bot.event
async def on_ready():
    activity = discord.Streaming(name="&help", url="https://www.twitch.tv/chillhopmusic")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    channel = bot.get_channel(870049723535474698)
    total_members = list(bot.get_all_members())
    total_channels = sum(1 for x in bot.get_all_channels())
    print('Guilds: ', len(bot.guilds))
    print('Large Guilds: ', sum(g.large for g in bot.guilds))
    print('Chunked Guilds: ', sum(g.chunked for g in bot.guilds))
    print('Members: ', len(total_members))
    print('Channels: ', total_channels)
    print('Message Cache Size: ', len(bot.cached_messages))
    await channel.send(f'Space has been restarted!')
    print(f"Welcome back Cosmos!")
    print(f"{bot.user}")
    print(f'Client = {round(bot.latency * 1000)}ms')
    print(f'All shards are online')

@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        sname = str(ctx.guild.name)
        uuser = str(ctx.message.author)
        await ctx.send("`Command not found.`")
        print(sname)
        print(uuser)

bot.load_extension('cogs.mod')
bot.load_extension('cogs.fun')
bot.load_extension('cogs.action')
bot.load_extension('cogs.owner')
bot.load_extension('cogs.animal')
bot.load_extension('cogs.utility')
 # this is good but you can make it better

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')



bot.run('ODQ3NTMyMzY0NjA2MjEwMDk5.YK_cBg.hp4D_YhgvjCAxLrgiEw_B0W7ejQ')