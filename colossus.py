#Colossus' basic functions for anything
import discord
import asyncio
import aiohttp
from random import randint
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import Game

links = ['gwH4jqW','ypVMXd4'] #approved discord invites

TOKEN = 'NDUyNjg5MjQzODY1NjEyMzA0.DfnW3A.AeK5fqu5fl4dM5RlJvk8JTQRtnY'

client = Bot(command_prefix="-")

#A basic hello function
@client.command(name="hello", description="Says hallo",pass_context = True)
async def hello(ctx):
    await client.say("Hello " + ctx.message.author.mention)

#Creates a random number between 0 and 100
@client.command(name='random',category='utility',description=": Gives a random number between 0 and 100",brief="Giving random number",pass_context = True)
async def random(ctx):
    await client.say(format(randint(0,100)) + " " + ctx.message.author.mention)

#Basic function for testing the bot's status
@client.command(name="ping",brief="Use it only if you are thinkning bot is going to die", description="Getting a pulse from bot to see if it's online")
async def ping():
    await client.say("Pong!" + ':ping_pong:')

#Feedback feature which deletes the user message after posting it to a secret channel
@client.command(name="feedback", brief="Leave anonymous feedback.", description="You can leave anonymous feedback. Your message will be removed and will be anonymously sent to mods.", pass_context = True)
async def feedback(message):

    await client.send_message(discord.Object(id='454177239127293982'), message.message.content[9:])

    try:
        await client.delete_message(message.message)
    except:
        print("I can't delete that message!")

#Function for adding the "Event" role to user    
@client.command(name="event_signup", brief="Saves you to event members list", description="Saves you to member list for the coming event", pass_context = True)
async def event_signup(text):
    user = text.message.author      #Getting the user who wants the role
    role = get(user.server.roles, name="Event")     #Getting the "Event" role
    
    #If user already has the role
    if role in user.roles:
        await client.say(user.mention + " You are already on the event list")
        return
    #If user doesn't has the role
    else:
        await client.add_roles(user , role)
        await client.say(user.mention + " Alright added to event list!")

#Removing the "Event" role
@client.command(name="event_quit", brief="Deletes you from event members list", description="Deletes you from member list for the coming event", pass_context = True)
async def event_quit(text):
    user = text.message.author      #Getting the user who doesn't wants the role anymore
    role = get(user.server.roles, name="Event")     #Getting the "Event" role
    
    #If user has the role
    if role in user.roles:
        await client.remove_roles(user, role)   #Remove the role from the user
        await client.say(user.mention + " OK. I removed you from the event list")
        return
    #If user doesn't has the rule
    else:
        await client.say(user.mention + " You are not in the list. You can sign up by typing '-event_signup' .")
        return

#A trigger which activates when a member joins the server
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

#A trigger which activates when a member leaves
@client.event
async def on_member_remove(member):
    await client.send_message(discord.Object(id='437688399755870208'), "User left " + member.display_name + ' #' + member.discriminator + "\nID: " + member.id)

#Discord server advirtesement prevention function    
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

#Basic function which runs on command line
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')
    await client.change_presence(game=Game(name="with people"))


client.run(TOKEN)
