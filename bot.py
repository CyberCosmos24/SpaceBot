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




@bot.event
async def on_ready(ctx):
    shard_id = ctx.guild.shard_id
    activity = discord.Streaming(name=f"&help", url="https://www.twitch.tv/chillhopmusic")
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
        guild = str(ctx.guild.name)

        uuser = str(ctx.message.author)
        await ctx.send("`Command not found.`")
        print(guild)
        print(uuser)

@bot.command(hidden=True)
@commands.is_owner() # Checks if the bot owner exectued the command
async def restart(ctx):
    await ctx.send("Client is restarting...")
    await bot.logout() # Logging outyyyyyyyyyyyyy

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

@bot.event
async def on_guild_leave(guild,ctx):
    guild = ctx.guild.name
    print(f"Space has left {guild}")

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

bot.run('ODQ3NTMyMzY0NjA2MjEwMDk5.YK_cBg.hp4D_YhgvjCAxLrgiEw_B0W7ejQ')