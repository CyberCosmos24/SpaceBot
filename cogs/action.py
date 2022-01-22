import discord
from discord import shard
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command
import random
from datetime import datetime
import aiohttp
from discord.member import Member

import discord

intents = discord.Intents.default()  
intents.members = True             

class Action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,help="Kiss a user")
    async def kiss(self,ctx, member: discord.Member=None):
      async with aiohttp.ClientSession() as session:
         
         request = await session.get('https://api.shinobu.host/api/v1/action/kiss')
         kissjson = await request.json()
         author = ctx.author.mention
         mention = member.mention

      embed = discord.Embed(description=f"{author} gave {mention} a kiss", color=discord.Color.random())
      embed.set_image(url=kissjson['link'])
      await ctx.send(embed=embed)
      if (member == ctx.message.author or member == None):
         ctx.send("`You didn't mention a member!`")

      
    @commands.command(pass_context=True,help="Hug a user")
    async def hug(self,ctx, member: discord.Member=None):
      async with aiohttp.ClientSession() as session:
         request = await session.get('https://some-random-api.ml/animu/hug')
         hugjson = await request.json()
         author = ctx.author.mention
         mention = member.mention

      embed = discord.Embed(description=f"{author} gave {mention} a hug", color=discord.Color.random())
      embed.set_image(url=hugjson['link'])
      await ctx.send(embed=embed)


    @commands.command(pass_context=True,help="Bonk a user")
    async def bonk(self,ctx, member: discord.Member=None):
         
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


   
    @commands.command(pass_context=True, help="Pat a user")
    async def pat(self,ctx, member: discord.Member=None):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/pat')
            hugjson = await request.json()
            author = ctx.author.mention
            mention = member.mention

         embed = discord.Embed(description=f"{author} gave {mention} a head pat ", color=discord.Color.random())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Action(bot))