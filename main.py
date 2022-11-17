import os
import discord
import random
import aiohttp

from keep_alive import keep_alive 
intents = discord.Intents.default()
intents.members = True
intents.guilds=True

client = discord.Client(intents=intents)

sad_words=["depressed","sad","lonely","heartbroken","gloomy","hopeless","lost","unhappy","hurt"]

bad_words=["sala"]

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return 
  
  if message.content == ".info":

    myEmbed= discord.Embed(title="Info",description='''Hi! I'm just a bot created by Frank for fun.
Below are the available commands.''',color=0x1ac6ff)
    myEmbed.add_field(name="Scissor_paper_rock_game:",value='''.scissor / .paper / .rock 
(choose one based on which you would like to pick)''')
    myEmbed.add_field(name="Heads_or_Tails",value=".heads or tails" , inline =False)
    myEmbed.add_field(name="Conversation",value='''.hello''',inline=False)
    myEmbed.add_field(name="Server_info",value='''.serverinfo
.members''',inline = False)
    myEmbed.add_field(name="Random Cat Images",value=".meow",inline=False)
    myEmbed.add_field(name="PS:",value = '''If you have certain suggestions or you would like the bot to do certain tasks,
you are free to dm Frankenstein#8315''',inline=False)
    await message.channel.send(embed = myEmbed)

  if message.content.startswith(".hello"):
    await message.channel.send("Hello!")
  
  if "@everyone" in message.content:
    await message.channel.send("Don't ping everyone b-baka!")
  
  if "drink water" in message.content.lower():
    await message.channel.send("Remember to stay hydrated luvvs!")

  if "cry"in message.content:
    await message.channel.send("Lemme wipe 'em tears off your face babygirl<3")

  if".meow"in message.content:
    async with aiohttp.ClientSession() as cs:
      async with cs.get("http://aws.random.cat/meow") as r:
        data=await r.json()

        image = discord.Embed(title="Meow")
        image.set_image(url=data['file'])
        await message.channel.send(embed = image)

  
  if any(word in message.content for word in sad_words):
    await message.channel.send("Cheer up buddy! You are loved.")

  if any(word in message.content for word in bad_words):
    await message.channel.send("Ghar bhitra chada bolne ho huh? Yozo lai bhandim.")
  
  if message.content==".heads or tails":
    choose = random.randint(1,2)
    if choose == 1:
      chance = discord.Embed(description="Heads",color=0xffcc00) 
      await message.channel.send(embed = chance)
    if choose == 2:
      chance = discord.Embed(description = "Tails",color=0xffff00)
      await message.channel.send(embed = chance)
  
  if message.content == ".scissor" or message.content== ".paper" or message.content == ".rock":
    comp = random.randint(1,3)
    if comp == 1:
      comp = "scissor"
    elif comp == 2:
      comp = "paper"
    elif comp == 3:
      comp = "rock"
    
    await message.channel.send(f"My turn : {comp}")
    
    if message.content == ".scissor":
      human = "scissor"
    elif message.content == ".paper":
      human = "paper"
    elif message.content == ".rock":
      human = "rock"
    
    if comp == human:
      result = None

    if comp == "scissor":
      if human == "rock":
        result = True
      elif human == "paper":
        result = False

    if comp == "paper":
      if human == "scissor":
        result = True
      elif human == "rock":
        result = False
    
    if comp == "rock":
      if human == "paper":
        result = True
      elif human == "scissor":
        result = False

    if result == None:
        result= discord.Embed(description="It's a Draw",color=0x1ac6ff)
        await message.channel.send(embed = result)  
    elif result == True:
      result = discord.Embed(description="Congrats!You Won.",color=0x39e600)
      await message.channel.send(embed = result) 
    elif result == False:
      result = discord.Embed(description="Better luck next time",color=0xe62e00)
      await message.channel.send(embed = result) 

  if message.content.startswith(".serverinfo"):
      name = str(message.guild.name)
      owner = str(message.guild.owner)
      member_count = str(message.guild.member_count)
      icon = str(message.guild.icon_url)
      region=str(message.guild.region)

      info = discord.Embed(
        title = name + " server information",
        color = 0x00e600
      )
      info.set_thumbnail(url=icon)
      info.add_field(name="Owner" , value =owner,inline = True)
      info.add_field(name="Member count",value=member_count,inline = True)
      info.add_field(name="Region",value=region,inline=True)

      await message.channel.send(embed = info)

  memberharu=""
  if message.content.startswith(".members"):
    x=message.guild.members
    for member in x:
      memberharu += member.name + "\n"
      
    memberlist = discord.Embed(
      title="Member list",
      description=memberharu,

      color = 0x0073e6
    )

    await message.channel.send(embed=memberlist)

@client.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels , name = "general-general")
  Welembed=discord.Embed(title="Welcome!",color=0x00ff80,description=f"{member.mention} \n Welcome to the server \n Hope you have a great time here!")
  Welembed.set_thumbnail(url=member.avatar_url)
  await channel.send(embed=Welembed)
      
keep_alive()  
client.run(os.getenv('TOKEN'))

