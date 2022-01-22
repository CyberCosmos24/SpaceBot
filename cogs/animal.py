
import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command
from datetime import datetime
import aiohttp



intents = discord.Intents.default()  
intents.members = True             
class Animal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, help="Shows a random cat picture")
    async def cat(self,ctx):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            hugjson = await request.json()
           
           

         embed = discord.Embed(title="KITTY! 😻", color=discord.Color.blue())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)

    @commands.command(pass_context=True,help="Shows a random raccoon picture")
    async def raccoon(self,ctx):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/raccoon')
            hugjson = await request.json()
        

         embed = discord.Embed(title="Raccoon!", color=discord.Color.blue())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)




    @commands.command(pass_context=True,help="Shows a random dog picture")
    async def dog(self,ctx):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            hugjson = await request.json()

         embed = discord.Embed(title="Doggie!! 🐕", color=discord.Color.blue())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)



    @commands.command(pass_context=True,help="Shows a random whale picture")
    async def whale(self,ctx):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/whale')
            hugjson = await request.json()
     

         embed = discord.Embed(title="Whale! 🐳", color=discord.Color.blue())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)



    @commands.command(pass_context=True,help="Shows a random bird picture")
    async def bird(self,ctx):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/bird')
            hugjson = await request.json()
        
         embed = discord.Embed(title="Bird! 🐦", color=discord.Color.blue())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)

 

    @commands.command(pass_context=True, help="Shows a random panda picture")
    async def panda(self,ctx):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda')
            hugjson = await request.json()
          

         embed = discord.Embed(title="Panda! 🐼", color=discord.Color.blue())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)

    @commands.command(pass_context=True,help="Shows a random fox picuture")
    async def fox(self,ctx):
         async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            hugjson = await request.json()
   

         embed = discord.Embed(title="Fox! 🦊", color=discord.Color.blue())
         embed.set_image(url=hugjson['link'])
         await ctx.send(embed=embed)

         
def setup(bot):
    bot.add_cog(Animal(bot))
