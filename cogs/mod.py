
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

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True) 
    async def lockdown(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
        await ctx.send( ctx.channel.mention + " ***is now in lockdown. To unlock this channel do `&unlock`***")
    @lockdown.error
    async def lockdown_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You can not use this command`")
        else: raise(error)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + " ***has been unlocked.***")
    @unlock.error
    async def unlock_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You can not use this command`")
        else: raise(error)


    @commands.command(aliases= ['purge','delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=0): 
        await ctx.channel.purge(limit=amount)                                     
        await ctx.send(f'{ctx.message.author} have deleted {amount} messages!')                         
        
    @clear.error 
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You need the manage_message permission`")
        else: raise(error)


    @commands.command(description="ban a user with specific reason (only admins)") #kick
    @commands.has_permissions(ban_members=True)
    async def ban (ctx, member:discord.User=None, reason =None):
        try:
            if (reason == None):
                await ctx.channel.send("You  have to specify a reason!")
                return
            if (member == ctx.message.author or member == None):
                await ctx.send("""You cannot ban yourself!""")
            await ctx.guild.ban(member, reason=reason)
            print(member)
            print(reason)
            await ctx.channel.send(f"{member} has been banned!")
        except:
            await ctx.send(f"Error banning user {member}")


    
        
    @commands.command(description="kicks a user with specific reason ") #kick
    @commands.has_permissions(kick_members=True)
    async def kick (ctx, member:discord.User=None, reason =None):
        try:
            if (reason == None):
                await ctx.channel.send("You  have to specify a reason!")
                return
            if (member == ctx.message.author or member == None):
                await ctx.send("```You cannot kick yourself!```") 
            await ctx.guild.kick(member, reason=reason)
            print(member)
            print(reason)
            await ctx.channel.send(f"{member} is kicked!")
        except:
            await ctx.send(f"{ctx.author} you can not kick user {member}! ")



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(ctx, channel: discord.TextChannel = None):
        if channel == None: 
            await ctx.send("You did not mention a channel!")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            await new_channel.send("https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
            await ctx.send("Nuked the Channel sucessfully!")

        else:
            await ctx.send(f"No channel named {channel.name} was found!")


def setup(bot):
    bot.add_cog(Moderation(bot))