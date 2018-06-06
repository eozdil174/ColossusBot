#Colossus' basic functions
import discord
import asyncio
import aiohttp
import random
from random import randint
from discord.ext.commands import Bot
from discord import Game
links = ['gwH4jqW','ypVMXd4'] #approved discord invites

TOKEN = ''

client = Bot(command_prefix="-")


@client.command(name="hello", description="Says hallo",pass_context = True)
async def hello(ctx):
    await client.say("Hello " + ctx.message.author.mention)

@client.command(name='random',category='utility',
                description=": Gives a random number between 0 and 100",
                brief="Giving random number",pass_context = True)
async def random(ctx):
    await client.say(format(randint(0,100)) + ctx.message.author.mention)

@client.command(name="ping",brief="Use it only if you are thinkning bot is going to die", description="Getting a pulse from bot to see if it's online")
async def ping():
    await client.say("Pong!" + ':ping_pong:')
    
@client.event
async def on_member_join(member):
    
    welcomeMessage = (member.mention + " Welcome to Café Tesla. Please have a seat. Your coffee will be served in a minute. \n"+

                                        "\nWe have MBTI type tags available for everyone. If you want to put your type's tag on to your profile: go to #bot_interactions and type\n"+
                                        "```.iam type```\n"+

                                        '\nFor example ".iam INTP"\n' +

                                        "\nAlso we now have country tags. You can find the whole list of available countries by typing '.lsar 2' in #bot_interactions . If you can't see your country. Write it down in #feedback and it will be added as soon as possible\n" +

                                        "\nIf you want to get notified when a VC event starts you can get the VC Squad role by simply typing \n"+
                                        "```.iam VC Squad\n```"


                                        "\nIf you need any help or questions you can ask them in #feedback channel. Have fun !\n")
    
    await client.send_message(discord.Object(id='437654104827756544'), welcomeMessage)


@client.event
async def on_member_remove(member):
    await client.send_message(discord.Object(id='437688399755870208'), "User left " + member.display_name + ' #' + member.discriminator + "\nID: " + member.id)
    
@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content #makes user message a variable   
    if "discord.gg" in msg: #tests for "discord.gg" in message
        print('Server link detected !')
        print('Message posted by ' + message.author.display_name) #Printing the author of the server message
        print('Message : ' + msg)
        invtest = 1 #sets up variable that controls if the invite is in the links array
        for link in links: #tests user message for every item in array
            if link in msg:  
                invtest = 0 #if the message contains the variable is set to false
        if invtest == 1: 
            await client.delete_message(message) #deletes the message if the invite isn't approved
           # await client.say(message.get_room, message.author.mention + " Unknown server invite discovered ! \n Please use following links for inviting people;\n \n discord.gg/gwH4jqW \n discord.gg/ypVMXd4")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=Game(name="with people"))


client.run(TOKEN)