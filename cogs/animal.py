

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
class AnimalCog():
    def __init__(self, bot):
        self.bot = bot







@commands.command()
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      dogjson = await request.json()
      # This time we'll get the fact request as well!

   embed = discord.Embed(title="KITTY! 😻", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)



@commands.command()
async def raccoon(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/racoon')
      dogjson = await request.json()
    

   embed = discord.Embed(title="Raccoon!", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)



@commands.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
     

   embed = discord.Embed(title="Doggie!! 🐕", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])

   await ctx.send(embed=embed)

@commands.command()
async def whale(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/whale')
      dogjson = await request.json()
     

   embed = discord.Embed(title="Whale! 🐳", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)

@commands.command()
async def bird (ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/bird')
      dogjson = await request.json()
      

   embed = discord.Embed(title="Bird! 🐦", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)


@commands.command()
async def panda (ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/panda')
      dogjson = await request.json()
    

   embed = discord.Embed(title="Panda! 🐼", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)

@commands.command()
async def fox (ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/fox')
      dogjson = await request.json()
     

   embed = discord.Embed(title="Fox! 🦊", color=discord.Color.blue())
   embed.set_image(url=dogjson['link'])
   await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(AnimalCog(bot))
