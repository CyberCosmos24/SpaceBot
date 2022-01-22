
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
bot = commands.AutoShardedBot (shard_count=1,command_prefix ="&", intents=intents, case_insensitive=True)

class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(hidden=True)
    @commands.is_owner()
    async def speak(self,ctx, *, text):
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")
   

    @commands.command(hidden=True)
    @commands.is_owner()
    async def ping(self,ctx):
        await ctx.send(f'Pong!')
        print(f"{round(self.bot.latency * 1000)}ms")
        
    @ping.error
    async def ping_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f" {ctx.message.author} you can not use that command.")
        else: raise(error)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def add(self,ctx, *,  member:discord.User=None):
        await ctx.send(f"{member} has been added to the list")
        print(f"{member} has been added to the blacklist")


    @commands.command(hidden=True)
    @commands.is_owner()
    async def spaceadd(self,ctx, *,  member:discord.User=None):
        await ctx.send(f"{member} has been added to `s6823_Guilds:gamma.bloom.host`")


    @commands.command(hidden=True)
    @commands.is_owner()
    async def cosmos(self,ctx):
        await ctx.send(f"Our favorite coding guy! <3") 



    @commands.command(hidden=True)
    @commands.is_owner()
    async def peppermint(self,ctx):
        await ctx.send(f"@ᖴIGᗰEᑎT#6858 is Cosmos bitch") 
    @peppermint.error
    async def peppermint_error(ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f" {ctx.message.author} you can not use that command")
        else: raise(error)






    @commands.command(hidden=True)
    @commands.is_owner() # Checks if the bot owner exectued the command
    async def restart(self,ctx):
        await ctx.send("Client is restarting...")
        await bot.logout() # Logging outyyyyyyyyyyyyy
    

    @commands.command(hidden=True)
    @commands.is_owner()
    async def dm(self,ctx, user: discord.User, *, value):

        await user.send(f"**{value}**")
        await ctx.send(f"Message Sent!")

    @dm.error
    async def dm_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f"`400 Bad Request (error code: 50007): Cannot send messages to this user`")
        else: raise(error)




    @commands.command(hidden=True)
    async def pping(self,ctx): 
        id = str(ctx.author.id)
        if id == '463932071451164673':
            await ctx.send(f'Websocket ping {round(self.bot.latency * 10000)}ms')
            
        else:
            await ctx.send(f" {ctx.message.author} you can not use that command")

    @commands.command(hidden=True)
    @commands.is_owner() # Checks if the bot owner exectued the command
    async def rr(self,ctx):
        await ctx.send("Yeah the fucking bot works") 





def setup(bot):
    bot.add_cog(OwnerCog(bot))