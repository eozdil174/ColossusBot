"""
This file includes some utility functions to do some stuff.
Even I don't know some of them
"""

import discord
from discord.utils import get
from discord.ext import commands
from datetime import datetime

class Utility(object):

    def __init__(self, bot):        #Initialize the bot
        self.bot = bot

    #Stares at the clock and says the time
    @commands.command(brief="Tells the time",pass_context=True)
    async def timeNow (self):
        time = datetime.now().strftime ('%H:%M:%S')         #Get the time...
        await self.bot.say("The time is " + time)           #... and print it

    #Anonymous feedback feature
    @commands.command(brief="Sends an anonymous message to #feedback channel", pass_context = True)
    async def feedback(self, message):

        await self.bot.send_message(discord.Object(id='454173550434058240'), message.message.content[9:])     #Post the message to #feedback channel

        try:                                                    #Try to delete the message (it can't if the message sent via DMs)
            await self.bot.delete_message(message.message)
        except:
            print("I can't delete that message!")

    #Anonymous venting feature
    @commands.command(brief="Send an anoymous message to #venting channel", pass_context=True)
    async def venting(self, message):
        await self.bot.send_message(discord.Object(id='454969449590685696'), message.message.content[8:])     #Post the message to #venting channel
        await self.bot.say("Alright posted to #venting !")

    #Some fun command to post a special message
    @commands.command(brief="Some funny thing to play with. ADMINS ONLY !", pass_context=True)
    async def sendMsg(self, message):
        print(message.message.author)
        if message.message.author.discriminator == '9600':
            await self.bot.send_message(discord.Object(id='450150175290163221'), message.message.content[8:])

        elif message.message.author.id == '231815469848461314':         #That's you Foun !
            await self.bot.send_message(discord.Object(id='450150175290163221'), "I'm not taking orders from you")

        else:       #For every other user
            await self.bot.send_message(discord.Object(id='450150175290163221'), "I don't think so")

    

#Setting the bot up
def setup(bot):
    bot.add_cog(Utility(bot))
