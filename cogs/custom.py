
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



class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True) # Hide custome command 
    async def meow (self,ctx):
            id = str(ctx.author.id)
            if id == '578699592116207629':

                embed = discord.Embed(title="Meow motherfucker :heart:", description="",color=0x0FEBE1)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Only Hide can use that command!")


    @commands.command(hidden=True) # Candy custom command
    async def candy(self,ctx):
            id = str(ctx.author.id)
            if id == '424792930461417475':
                await ctx.send("Candy is a little one! :hearts:  ") 
            else:
                
                    await ctx.send("Only Candy can use that command!")

    @commands.command(hidden=True) # Pongo custom command
    async def pongo(self,ctx):
            id = str(ctx.author.id)
            if id == '376027321154404353':
                await ctx.send("Nano Swarm Love <3 ") 
            else:
                
                    await ctx.send("Only Pongo can use that command!")


    @commands.command(hidden=True) 
    async def train(self,ctx):
            await ctx.send("choo choo :train: :rainbow: :sparkling_heart: ")


    @commands.command(hidden=True) # My love custom command 
    async def gaytorade(self,ctx):
            id = str(ctx.author.id)
            if id == '867986155684126750':
                await ctx.send(":sparkling_heart: Maya :sparkling_heart: ") 

    @commands.command(hidden=True) # Spicyy
    async def spieccyy(self,ctx):
            id = str(ctx.author.id)
            if id == '812528856363696138':
                await ctx.send("He's Spieccyy")
            else:   
                await ctx.send("Only Spiecy can use that command!")

    @commands.command(hidden=True) # Dumpy 
    async def dork(self,ctx):
            id = str(ctx.author.id)
            if id == '660609569525071883':
                    await ctx.send("❤️ she is a Valorant god and she's hot af! ❤️ ")
            else:   
                await ctx.send("Only Dork can use that command!")


    @commands.command(hidden=True) # Snowy COmmand
    async def snow(self,ctx):
            id = str(ctx.author.id)
            if id == '269684770680602624':
                    await ctx.send("Snowy is amazing! ❤️ ")
            else:   
                await ctx.send("Only Snowy can use that command!")
    @commands.command()
    async def paro(self,ctx):
        id = str(ctx.author.id)
        if id == '463932071451164673':
            await ctx.send('paro is the tall and we love him. <3')
            
        else:
            await ctx.send(f" {ctx.message.author} you can not use that command")



def setup(bot):
    bot.add_cog(Custom(bot))