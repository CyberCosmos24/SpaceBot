from discord import shard
import random
import json
import os
import datetime, time
from datetime import datetime
import aiohttp
from discord.ext import commands
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




class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      


    @commands.command(pass_context=True,help="Shows the status of the bot")
    async def status(self,ctx):
        general_text = f'Latency: **{round(self.bot.latency * 1000)}ms**'
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

    @commands.command(pass_context=True,help="Displays bot information" )
    async def botinfo (self,ctx):
        authors = f'Cosmos#2424'
        env_text = f'Language: Python {sys.version.split()[0]}'
        env_text += f'\nLibrary: discord.py {discord.__version__}'
        env_text += f'\nPlatform: {sys.platform.upper()}'
        sas_text = f'Guilds: {len(self.bot.guilds)}'
        sas_text += f'\nMembers: {len(self.bot.users)}'
        sas_text += f'\nCommands: {len(self.bot.commands)}'
        Embed = discord.Embed(title="Space Bot Info",color=0x176cd5)
        Embed.add_field(name='Authors', value=authors) 
        Embed.add_field(name='Environment', value=env_text)
        Embed.add_field(name='Stats', value=sas_text)
        await ctx.send(embed=Embed)




    @commands.command(aliases=['serverinfo'], help="Displays server information")
    @commands.guild_only()
    async def server(self,ctx):   
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon.url)
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=(0x176cd5)
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name=" Owner", value=owner, inline=True)
        embed.add_field(name=' Created At', value=ctx.guild.created_at.__format__('%a, %d. %b %Y'), inline=True)
        embed.add_field(name=" Server ID", value=id, inline=True)
        embed.add_field(name=" Member Count", value=memberCount, inline=True)
        embed.add_field(name=" Bot Count", value=len([bot for bot in ctx.guild.members if bot.bot]), inline=True)
        embed.add_field(name=' Verification Level', value=str(ctx.guild.verification_level), inline=False)
        embed.add_field(name=" Text Channels", value=len(ctx.guild.text_channels), inline=True)
        embed.add_field(name=" Voice Channels", value=len(ctx.guild.voice_channels), inline=True)
        embed.add_field(name="Catergories", value=len(ctx.guild.categories), inline=True)
        embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
        await ctx.send(embed=embed)


    @commands.command(aliases=['user'],pass_context=True,help="Displays user information")
    @commands.guild_only()
    async def userinfo(self,ctx, user: discord.User = None):
     
        if user == None: ##if no user is inputted
            user = ctx.author ##defines user as the author of the message
        embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
        embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Roles", value=len(user.roles))
        embed.add_field(name="Joined", value=user.joined_at.__format__('%a, %d. %b %Y'))
        embed.add_field(name="Created", value=user.created_at.__format__('%a, %d. %b %Y'))
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
        await ctx.send(embed=embed)


    @commands.command(hidden=True,help="Shows the amount of members in the guild")
    @commands.guild_only()
    async def members(self,ctx):
        gname = str(ctx.guild.name)
        await ctx.send(f" {gname} member count is {(ctx.guild.member_count)}")








def setup(bot):
    bot.add_cog(Utility(bot))