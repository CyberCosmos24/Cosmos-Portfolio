import discord
from discord.ext import commands
from discord.ext.commands.core import command
import random
import json



from discord.member import Member

intents = discord.Intents.default()  
intents.members = True  


client = commands.Bot (command_prefix = "&", intents=intents)




@client.event
async def on_ready():
    activity = discord.Game(name=f"&help | Watching over {len(client.guilds)} servers ", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    



#Fun commands
@client.command()
@commands.has_permissions(administrator=True)
async def speak(ctx, *, text):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{text}")

@client.command() 
async def ping(ctx):
    await ctx.send(f"Latency is **{round(client.latency * 1000)}ms**!") 

@client.command() 
async def candy(ctx):
    
    await ctx.send("Candy is a litte one. :hearts:  ") 




@client.command()
async def uglybean(ctx):
    await ctx.send("Ugly Bean is poggers!")




    
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ['It is certain.', 
                'Without a doubt',
                'Yes',
                'No',
                'Discord says no',
                'Count on it',
                'Nope',
                'Go think about it']
  await ctx.send(content=f'Question: {question}\n:8ball: says: {random.choice(responses)}')


@client.command()
async def coinflip (ctx):
  responses = ['Heads','Tails']
  await ctx.send(f'{random.choice(responses)}')

@client.command()
async def cat(ctx):
  catpics = ['https://images.all-free-download.com/images/graphiclarge/cat_cats_eyes_curious_215925.jpg',
  'https://images.all-free-download.com/images/graphiclarge/cat_background_201718.jpg','https://images.all-free-download.com/images/graphiclarge/cat_195127.jpg',
  'https://images.all-free-download.com/images/graphiclarge/beautiful_cat_picture_6_168770.jpg',
  'https://images.all-free-download.com/images/graphiclarge/wild_cat_posing_513899.jpg',
  'https://images.all-free-download.com/images/graphiclarge/norwegian_cat_513891.jpg',
  'https://images.all-free-download.com/images/graphiclarge/what_now_human_211370.jpg']
  await ctx.send(f'{random.choice(catpics)}')


@client.command()
async def dog(ctx):
  dogpics = ['https://images.pexels.com/photos/1805164/pexels-photo-1805164.jpeg?cs=srgb&dl=pexels-valeria-boltneva-1805164.jpg&fm=jpg',
  'https://images.pexels.com/photos/97082/weimaraner-puppy-dog-snout-97082.jpeg?cs=srgb&dl=pexels-pixabay-97082.jpg&fm=jpg',
  'https://images.pexels.com/photos/2820134/pexels-photo-2820134.jpeg?cs=srgb&dl=pexels-josh-hild-2820134.jpg&fm=jpg',
  'https://images.pexels.com/photos/3687770/pexels-photo-3687770.jpeg?cs=srgb&dl=pexels-tanika-3687770.jpg&fm=jpg',
  'https://images.pexels.com/photos/2797318/pexels-photo-2797318.jpeg?cs=srgb&dl=pexels-charles-roth-2797318.jpg&fm=jpg',
  'https://images.pexels.com/photos/3009441/pexels-photo-3009441.jpeg?cs=srgb&dl=pexels-josh-hild-3009441.jpg&fm=jpg',
  'https://images.pexels.com/photos/4668425/pexels-photo-4668425.jpeg?cs=srgb&dl=pexels-gillian-harrison-4668425.jpg&fm=jpg']
  await ctx.send(f'{random.choice(dogpics)}')

@client.command()
async def whale(ctx):
  whalepics = ['https://cdn.discordapp.com/attachments/773756807733837868/849102844309405736/0rfzij1_2AVxdB-lr.png',
  'https://images.all-free-download.com/images/graphiclarge/humpback_whale_sea_214286.jpg',
  'https://images.pexels.com/photos/4666751/pexels-photo-4666751.jpeg?cs=srgb&dl=pexels-elianne-dipp-4666751.jpg&fm=jpg',
  'https://images.pexels.com/photos/289324/pexels-photo-289324.jpeg?cs=srgb&dl=pexels-pixabay-289324.jpg&fm=jpg',
  'https://images.pexels.com/photos/3309865/pexels-photo-3309865.jpeg?cs=srgb&dl=pexels-andre-estevez-3309865.jpg&fm=jpg',
  'https://images.pexels.com/photos/4666753/pexels-photo-4666753.jpeg?cs=srgb&dl=pexels-elianne-dipp-4666753.jpg&fm=jpg',
  'https://images.pexels.com/photos/3695720/pexels-photo-3695720.jpeg?cs=srgb&dl=pexels-dianne-maddox-3695720.jpg&fm=jpg']
  await ctx.send(f'{random.choice(whalepics)}')


@client.command()
async def meow (ctx):
    embed = discord.Embed(title="Meow motherfucker :heart:", description="",color=0x0FEBE1)
    await ctx.send(embed=embed)






@client.command()
async def poll(ctx, question, option1=None, option2=None):
  if option1==None and option2==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**")
    await message.add_reaction('✅')
    await message.add_reaction('❎')
   
  elif option1==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = No**")
    await message.add_reaction('✅')
    await message.add_reaction('❎')
    
  elif option2==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = {option2}**")
    await message.add_reaction('✅')
    await message.add_reaction('❎')

  else:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = {option2}**")
    await message.add_reaction('✅')
    await message.add_reaction('❎')
    




# Moderation Commands
 
@client.command()
@commands.has_permissions(manage_channels=True) 
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in lockdown. To unlock this channel do `&unlock`***")
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
async def clear(ctx, amount=5): 
   await ctx.channel.purge(limit=amount)                                     
   await ctx.send(f'Staff have deleted {amount} messages!')                         
    
  
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("```You need the manage_message permission```")
    else: raise(error)









@client.command(description="ban a user with specific reason (only admins)") #kick
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
    await ctx.channel.send(f"{member} is banned")
 except:
    await ctx.send(f"Error banning user {member} ")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member: discord.Member):
    await ctx.guild.unban(member)
@unban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("```You don't have permission to Unban this member```")
    else: raise(error)
 

@client.command(description="kicks a user with specific reason (only admins)") #kick
@commands.has_permissions(kick_members=True)
async def kick (ctx, member:discord.User=None, reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot kick yourself!""") 
    await ctx.guild.kick(member, reason=reason)
    print(member)
    print(reason)
    await ctx.channel.send(f"{member} is kicked!")
 except:
    await ctx.send(f"Error kicking user {member} (cannot kick owner or bot)")


@client.command()
async def botinfo (ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = "Cosmos#0024"
   date = "2021-05-27T17:51:02"

    serverCount = len(client.guilds)

    embed = discord.Embed(title="Space Bot Info", description="",color=0x176cd5)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Servers", value=serverCount, inline=True)
    embed.add_field(name="Ping", value=f"{round(client.latency * 1000)}ms", inline=True)
    embed.add_field(name="Created", value=date, inline=True)
    
    await ctx.send(embed=embed)



@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.red()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)




client.remove_command("help")
@client.command()
async def help(ctx):

    embed = discord.Embed(title="Space Commands", description="",color=0x176cd5) #,color=Hex code
    embed.add_field(name="moderation", value="Shows moderation commands",inline=False)
    embed.add_field(name="fun" , value="Shows fun commands",inline=False)
    embed.add_field(name="info" , value="Shows info commands",inline=False)
    embed.add_field(name="invite" , value="Invites",inline=False)
    embed.set_author(name="Prefix &")
    await ctx.send(embed=embed)

@client.command()
async def moderation(ctx):
    embed = discord.Embed(title="Space Moderation Commands", description="",color=0x176cd5)
    embed.add_field(name="clear", value="&clear (amount)",inline=False)
    embed.add_field(name="lockdown", value="&lockdown : lockdowns the channel",inline=False)
    embed.add_field(name="unlock", value="&unlock : unlocks the channel",inline=False)
    embed.add_field(name="kick", value="&kick (member) [reason]",inline=False)
    embed.add_field(name="ban", value="&ban (member) [reason]",inline=False)
    embed.add_field(name="unban", value="&unban (member)",inline=False)
  
    


    await ctx.send(embed=embed)
    

@client.command()
async def fun (ctx):
    embed = discord.Embed(title="Space Fun Commands", description="",color=0x176cd5) #,color=Hex code
    embed.add_field(name="8ball", value="&8ball (question)",inline=False)
    embed.add_field(name="whale", value="Shows a picture of a whale ",inline=False)
    embed.add_field(name="dog", value="shows a picture of a dog ",inline=False)
    embed.add_field(name="cat ", value="Shows a picture of a dog",inline=False)
    embed.add_field(name="coinflip", value="Flips a coin ",inline=False)
    embed.add_field(name="ping", value="Shows latency  ",inline=False)
    embed.add_field(name="poll", value='&poll "Question" option1 option2',inline=False)
    embed.add_field(name="speak", value="&speak message",inline=False)
    await ctx.send(embed=embed)
@client.command()
async def invite(ctx):
    embed = discord.Embed(title="Invtes", description="") #,color=Hex code
    embed.add_field(name="Bot Invite", value=" https://discord.com/oauth2/authorize?client_id=847532364606210099&scope=bot&permissions=8",inline=False)
    embed.add_field(name="Bot Support Server", value="https://discord.gg/dZEpx4zsjF",inline=False)
  
    
    await ctx.send(embed=embed)


@client.command()
async def info(ctx):
    embed = discord.Embed(title="Information Commands", description="",color=0x176cd5) #,color=Hex code
    embed.add_field(name="server", value="Tell information about a server",inline=False)
    embed.add_field(name="userinfo", value="&userinfo (member)",inline=False)
    embed.add_field(name="botinfo", value="Tell information about the bot",inline=False)


@client.command()
async def userinfo(ctx, user: discord.Member=None):
    """Displays user information."""
    if user == None: ##if no user is inputted
        user = ctx.author ##defines user as the author of the message
    embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
    embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Roles", value=len(user.roles))
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Created", value=user.created_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)






client.run('ODQ3NTMyMzY0NjA2MjEwMDk5.YK_cBg.HiyMU21ANP0-g0msxl4klcE84JI')