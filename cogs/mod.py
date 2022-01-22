
import discord
from discord import shard
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command
from datetime import datetime
from discord.member import Member

import discord

intents = discord.Intents.default()  
intents.members = True             

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="lockdown a channel")
    @commands.has_permissions(manage_channels=True) 
    async def lockdown(self,ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
        await ctx.send( ctx.channel.mention + " ***is now in lockdown. To unlock this channel do `&unlock`***")
    @lockdown.error
    async def lockdown_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You need the manage_channels permission to use this command`")
        else: raise(error)

    @commands.command(help="Unlock a channel")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self,ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + " ***has been unlocked.***")
    @unlock.error
    async def unlock_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You need the manage_channels permission to use this command`")
        else: raise(error)


    @commands.command(aliases= ['purge','delete'],help="Clears desire amount of messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=0): 
        await ctx.channel.purge(limit=amount)                                     
        await ctx.send(f'{ctx.message.author} have deleted {amount} messages!')                         
        
    @clear.error 
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You need the manage_message permission to use this command`")
        else: raise(error)


    @commands.command(help="Bans a user from the guild") #kick
    @commands.has_permissions(ban_members=True)
    async def ban (self, ctx, member:discord.User=None, reason =None):
        try:
            if (reason == None):
                await ctx.channel.send("`You have to specify a reason!`")
                return
            if (member == ctx.message.author or member == None):
                await ctx.send("`You cannot ban yourself!`")
            await ctx.guild.ban(member, reason=reason)
            print(member)
            print(reason)
            await ctx.channel.send(f"{member} has been banned! for {reason}")
        except:
            await ctx.send(f"Error banning user {member}")


    @ban.error 
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You need the ban_members permission to use this command`")
        else: raise(error)
        
    @commands.command(help="Kicks a user from the guild") #kick
    @commands.has_permissions(kick_members=True)
    async def kick (self,ctx, member:discord.User=None, reason =None):
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
    @kick.error 
    async def kick_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("`You need the kick_members permission to use this command`")
        else: raise(error)


    
def setup(bot):
    bot.add_cog(Moderation(bot))