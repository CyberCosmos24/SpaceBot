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
        source = f'https://github.com/CyberCosmos24/SpaceBot'
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
        Embed.add_field(name='Source', value=source)
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
    async def userinfo(self,ctx, user: discord.Member = None):
     
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

    @commands.command()
    async def moderation(self,ctx):
        embed = discord.Embed(title="Space Moderation Commands", description="",color=0x176cd5)
        embed.add_field(name="clear", value="`&clear (amount)`",inline=False)
        embed.add_field(name="lockdown", value="`&lockdown : lockdowns the channel`",inline=False)
        embed.add_field(name="unlock", value="`&unlock : unlocks the channel`",inline=False)
        embed.add_field(name="kick", value="`&kick (member) [reason]`",inline=False)
        embed.add_field(name="ban", value="`&ban (member) [reason]`",inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
    

    @commands.command()
    async def fun (self,ctx):
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


    @commands.command()
    async def utility (self,ctx):
        embed = discord.Embed(title="Utility Commands", description="",color=0x176cd5) 
        embed.add_field(name="server", value="`Tell information about a server`",inline=False)
        embed.add_field(name="userinfo", value="`&userinfo (member)`",inline=False)
        embed.add_field(name="botinfo", value="`Tell information about the bot`",inline=False)
        embed.add_field(name="status", value="`Gives the status of the bot`",inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}") 
        await ctx.send(embed=embed)

    @commands.command()
    async def animal (self,ctx):
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
    
    @commands.command()
    async def action (self,ctx):
        embed = discord.Embed(title="Action Commands", description="",color=0x176cd5) 
        embed.add_field(name="hug", value="`Disabled`",inline=False)
        embed.add_field(name="kiss", value="`Kiss a user`",inline=False)
        embed.add_field(name="bonk", value="`Bonk a user`",inline=False)
        embed.add_field(name="pat", value="`Pat a user`",inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avatar.url}", text = f"Requested by {ctx.author}")
        await ctx.send(embed=embed)


    @commands.command()
    async def support (self,ctx):
        embed = discord.Embed(title=" Support Commands", description="",color=0x176cd5)
        embed.add_field(name="invite", value="`invite the bot`",inline=False)
        embed.add_field(name="sdiscord", value="`support server`",inline=False)
        embed.set_footer(icon_url = f"{ctx.author.avata.url}", text = f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def sdiscord (self,ctx):
        embed = discord.Embed(title="Support server", description="",color=0x176cd5) 
        embed.add_field(name="https://discord.gg/KUybC7tBA2", value="Feel free to join!",inline=False)
        await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(Utility(bot))