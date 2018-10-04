"""
This file includes event functions such as:
- Creating the event
- Posting the event
- And giving Event roles based on certain reactions
"""

import discord
import asyncio
from discord.ext import commands
from discord.utils import get
import datetime, time

class eventManagement(object):

    def __init__(self, bot, event_message = "Not Assigned",title = "Not Assigned", desc = "Not Assigned", clock = "Not Assigned", desTime = "Not Assigned"):
        self.bot = bot
        self.title = title                  #Assigning every setting to bot for making things easy
        self.desc = desc
        self.clock = clock
        self.desTime = desTime
        self.event_message = event_message

    #Creating the custom embed for the event
    @commands.command(brief="Create the event embed",pass_context=True)
    async def event_create(self, message):
        user = message.message.author
        event_creator_role = get(user.server.roles, name="Event Creator")
        if event_creator_role in message.message.author.roles:
            if message.message.content.startswith("-event_create eTitle"):      #Set the title
                if self.title == "Not Assigned":
                    self.title = message.message.content[21:]
                    await self.bot.say("Title set as : " + str(self.title))


            if message.message.content.startswith("-event_create eDesc"):       #Set the description
                 if self.desc == "Not Assigned":
                    self.desc = message.message.content[20:]
                    await self.bot.say("Description set as : " + self.desc)


            if message.message.content.startswith("-event_create eClock"):      #Set the clockURL
                if self.clock == "Not Assigned":
                    self.clock = message.message.content[21:]
                    await self.bot.say("ClockURL set as : " + self.clock)


            if message.message.content.startswith("-event_create eDesTime"):    #Set the designated time
                if self.desTime == "Not Assigned":
                    self.desTime = message.message.content[23:]
                    await self.bot.say("Designated Time set as : " + self.desTime)
        else:
            await self.bot.say("Sorry you don't have the permission to do that.")

    @commands.command(pass_context = True)
    async def event_reset(self, message):
        user = message.message.author   #Getting the message author
        event_creator_role = get(user.server.roles, name="Event Creator")   #Getting the Event Creator role

        if event_creator_role in user.roles:        #Checking the author's roles for being sure it has the rights to do that
            self.title = "Not Assigned"
            self.desc =  "Not Assigned"         #Resetting the settings
            self.clock = "Not Assigned"
            self.desTime = "Not Assigned"

            await self.bot.say("Event message reseted !")
        else:
            await self.bot.say("You don't have the permission to do that !")


    @commands.command(pass_context = True)
    async def event_end(self, message):
        end_embed = discord.Embed(title=(self.title + " - Finished !"), colour=discord.Colour(0x53ad80), description="**__This event has finished !__**", timestamp=datetime.datetime.utcfromtimestamp(int(time.time())))
        #The preset end embed for making things easy
        end_embed.set_footer(text="ColossusBot |" + str(message.message.author))

        user = message.message.author
        event_creator_role = get(user.server.roles, name="Event Creator")

        if event_creator_role in user.roles:            #Resetting the event settings
            self.title = "Not Assigned"
            self.desc =  "Not Assigned"
            self.clock = "Not Assigned"
            self.desTime = "Not Assigned"

            await self.bot.edit_message(self.event_message, embed = end_embed)  #Editing the existing event message and posting the end message
            await self.bot.clear_reactions(self.event_message)                  #Clearing the reactions from that message

            user = text.message.author                                        #Getting the user who wrote the command
            event_creator_role = get(user.server.roles, name="Event Creator") #Getting the "Event Creator" role for the permission system

                            #If user has the Event Creator role
            role = get(user.server.roles, name="Event")     #Getting the "Event" role !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Change according to the server you are goint to use!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            members = text.message.server.members           #Getting all the members in the server
            for member in members:                          #For every member in the server this will remove the role who has it
                #If user has the role
                if role in member.roles:
                    await self.bot.remove_roles(member, role)   #Remove the role from the user
                    print("\nRemoved the 'Event' role from " + str(member))
                    continue
                #If user doesn't has the role
                else:
                    continue

        else:
            await self.bot.say("You don't have the permission to do that !")


    @commands.command(pass_context = True)
    async def event_post(self, message):
        user = message.message.author      #Getting the user who wants the role
        event_creator_role = get(user.server.roles, name="Event Creator")#Getting the "Event Creator" role for the permission system
        event_room = self.bot.get_channel('453209726717657100')             #('437658178579333130') => Cafe Tesla Id !!! Replace it !!!    #The id of the room which will be used for posting event messages

        if event_creator_role in user.roles:      #Checking the Event Creator for the user who tried to create event

            timeStamp = int(time.time())         #Getting timestamp

            event_embed = discord.Embed(title=self.title, colour=0x53ad80, url=self.clock, description=self.desc, timestamp=datetime.datetime.utcfromtimestamp(timeStamp))
                                                                                                                    #  ^^ Converting timestamp to utc format ^^
            event_embed.set_footer(text="ColossusBot | " + str(message.message.author))    #Setting the author text

            event_embed.add_field(name="React with :white_check_mark: for joining the event", value="\u200b")             #Creating the description message
            event_embed.add_field(name="React with :negative_squared_cross_mark: for leaving the event", value="\u200b")
            event_embed.add_field(name="Extra Information", value="The event will start at "+ self.desTime +". You can check the time by clicking : "+str(self.clock), inline=True)
                                                                                        # ^ The choosen time while setting up the event ......... and the clock url ^

            self.event_message = await self.bot.send_message(event_room, embed=event_embed)
            await asyncio.sleep(0.26)
            await self.bot.add_reaction(self.event_message, '✅')    #Adding the reaction
            await asyncio.sleep(0.26)
            await self.bot.add_reaction(self.event_message, '❎')    #Adding the reaction
        else:
            await self.bot.send_message(event_room, user.mention + " Sorry. You don't have permission for doing that. Please contact with a moderator for creating that event")


        #The trigger for assigning the "Event" role by reactions
        @self.bot.event
        async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
            role = get(user.server.roles, name="Event")     #Getting the "Event" role   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Change according to the server you are goint to use!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            roleChannel = self.bot.get_channel('453209726717657100')             #('437658178579333130') => Cafe Tesla Id !!! Replace it !!!

            if reaction.message.channel != roleChannel :
                return #So it only happens in the specified channel

            if reaction.emoji == "✅":      #If user chooses that reaction give the role
                await self.bot.add_roles(user, role)

            elif reaction.emoji == '❎':    #If user chooses that reaction remove the role
                await self.bot.remove_roles(user, role)

            else:
                print("I don't know that")


#Setting the bot and the class up
def setup(bot):
    bot.add_cog(eventManagement(bot))
