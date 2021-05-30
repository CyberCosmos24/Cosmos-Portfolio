import discord
from discord.ext import commands
from discord.ext.commands.core import command
import random

from discord.member import Member

client = commands.Bot (command_prefix = '$')


@client.event
async def on_ready():
    print('HALLO')

@client.command() 
async def ping(ctx):
     await ctx.send(f"Ping!\nLatency is **{round(client.latency * 1000)}ms**!")
    
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ['It is certain.', 
                'Without a doubt',
                'Yes',
                'No',
                'Discord says no',
                'Count on it']
  await ctx.send(content=f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_channels=True) 
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in lockdown.***")
@lockdown.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("`You can not use this command`")
    else: raise(error)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")
@unlock.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("```You can not use this command```")
    else: raise(error)


@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount :int = -1):
   if amount == -1:
       await ctx.channel.purge(limit=1000000)
   else:
       await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("```You can not use this command```")
    else: raise(error)









@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("```You don't have permission to ban this member```")
    else: raise(error)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member: discord.Member):
    await ctx.guild.unban(member)
@unban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("```You don't have permission to Unban this member```")
    else: raise(error)
 

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("```You don't have permission to kick this member```")
    else: raise(error)


    
client.remove_command("help")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Space Commands", description="") #,color=Hex code
    embed.add_field(name="8ball", value="$8ball (question)",inline=False)
    embed.add_field(name="ping", value="$ping",inline=False)
    embed.add_field(name="clear", value="$clear (amount)",inline=False)
    embed.add_field(name="lockdown", value="$lockdown : lockdowns the channel",inline=False)
    embed.add_field(name="unlock", value="$unlock : unlocks the channel",inline=False)
    embed.add_field(name="kick", value="$kick (member) [reason]",inline=False)
    embed.add_field(name="ban", value="$ban (member) [reason]",inline=False)
    embed.add_field(name="unban", value="$unban (member)",inline=False)
  
    
    await ctx.send(embed=embed)






client.run('ODQ3NTMyMzY0NjA2MjEwMDk5.YK_cBg._1GFqThFuyl9MG03tQrrJ7VBRGc')