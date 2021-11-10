
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
bot = commands.AutoShardedBot (shard_count=3,command_prefix ="&", intents=intents, case_insensitive=True)

class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@commands.command(hidden=True)
@commands.is_owner()
async def speak(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")
@speak.error
async def speak_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} you can not use this command.")
    else: raise(error)

@commands.command(hidden=True)
@commands.is_owner()
async def ping(ctx):
    shard_id = ctx.guild.shard_id
    shard = bot.get_shard(shard_id)
    shard_ping = f'{round(shard.latency * 1000)}ms'

    await ctx.send(f'Client: `{round(bot.latency * 1000)}ms`')
    await ctx.send(f'Shard: `{shard_ping}`')
   

  


@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} you can not use that command.")
    else: raise(error)

@commands.command(hidden=True)
@commands.is_owner()
async def add(ctx, *,  member:discord.User=None):
    message = ctx.message
    await ctx.send(f"{member} has been added to the list")


@commands.command(hidden=True)
@commands.is_owner()
async def spaceadd(ctx, *,  member:discord.User=None):
    await ctx.send(f"{member} has been added to `s6823_Guilds:gamma.bloom.host`")


@commands.command(hidden=True)
@commands.is_owner()
async def cosmos(ctx):
    await ctx.send(f"Our favorite coding guy! <3") 



@commands.command(hidden=True)
@commands.is_owner()
async def peppermint(ctx):
    await ctx.send(f"@ᖴIGᗰEᑎT#6858 is Cosmos bitch") 
@peppermint.error
async def peppermint_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f" {ctx.message.author} you can not use that command")
    else: raise(error)






@commands.command(hidden=True)
@commands.is_owner() # Checks if the bot owner exectued the command
async def restart(ctx):
    await ctx.send("Client is restarting...")
    await bot.logout() # Logging outyyyyyyyyyyyyy
   

@commands.command(hidden=True)
@commands.is_owner()
async def dm(ctx, user: discord.User, *, value):

    await user.send(f"**{value}**")
    await ctx.send(f"Message Sent!")

@commands.command()
async def paro(ctx):
    id = str(ctx.author.id)
    if id == '463932071451164673':
        await ctx.send('paro is the tall and we love him. <3')
        
    else:
        await ctx.send(f" {ctx.message.author} you can not use that command")


@commands.command(hidden=True)
async def pping(ctx):
    id = str(ctx.author.id)
    if id == '463932071451164673':
        await ctx.send(f'Websocket ping {round(bot.latency * 10000)}ms')
        
    else:
        await ctx.send(f" {ctx.message.author} you can not use that command")

@commands.command(hidden=True)
@commands.is_owner() # Checks if the bot owner exectued the command
async def rr(ctx):
    await ctx.send("Testing") 





def setup(bot):
    bot.add_cog(OwnerCog(bot))