
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


class CustomCog():
    def __init__(self, bot):
        self.bot = bot 




@commands.command() # Hide custome command 
async def meow (ctx):
    id = str(ctx.author.id)
    if id == '578699592116207629':

        embed = discord.Embed(title="Meow motherfucker :heart:", description="",color=0x0FEBE1)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Only Hide can use that command!")



@commands.command() # Candy custom command
async def candy(ctx):
    id = str(ctx.author.id)
    if id == '424792930461417475':
        await ctx.send("Candy is a little one! :hearts:  ") 
    else:
        
             await ctx.send("Only Candy can use that command!")

@commands.command() 
async def train(ctx):
    await ctx.send("choo choo :train: :rainbow: :sparkling_heart: ")


@commands.command() # Soccer Mom custom command 
async def uglybean(ctx):
    id = str(ctx.author.id)
    if id == '867986155684126750':
        await ctx.send("Thats soccer mom! :soccer: ") 

@commands.command() # Spicyy
async def spieccyy(ctx):
    id = str(ctx.author.id)
    if id == '812528856363696138':
        await ctx.send("He's Spieccyy")

    else:   
         await ctx.send("Only Spiecy can use that command!")

@commands.command() # Dumpy 
async def dork(ctx):
 id = str(ctx.author.id)
 if id == '660609569525071883':
        await ctx.send("❤️ she is a Valorant god and we love her lots! ❤️ ")
 else:   
         await ctx.send("Only Dork can use that command!")


@commands.command() # Snowy COmmand
async def snow(ctx):
 id = str(ctx.author.id)
 if id == '269684770680602624':
        await ctx.send("Snowy is amazing! ❤️ ")
 else:   
         await ctx.send("Only Snowy can use that command!")

@commands.command()
async def racc(ctx):
    id = str(ctx.author.id)
    if id == '290649060002496512':
        await ctx.send(f'Thats a dirty raccoon bitch')
        
    else:
        await ctx.send(f" {ctx.message.author} you can not use that command")






def setup(bot):
    bot.add_cog(CustomCog(bot))