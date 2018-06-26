"""
This file contains role management functions for everyone.
The special roles (admin and staff roles (also bot roles)) has to be added to seriousRoles (that will be automated in the future)
"""

import discord
import asyncio
from discord.ext import commands
from discord.utils import get

roles = []                                                                  #Saving all the available roles to that list
seriousRoles = {'Admin', 'Intern','Event Creator','Bot','@everyone'}        #The special roles

def get_roles(message):                                                 #Function for getting the available roles
    roles.clear()                                                       #Cleaning the list to prevent duplicate roles
    for role in message.message.author.server.roles:                    #For every role in the current server
        if str(role) not in seriousRoles:                               #If the role is not in seriousRoles
            roles.append(str(role))                                     #Put it to role list
    roles.sort()                                                        #Sort the roles list to make it look organized

class roleManagement(object):

    def __init__(self, bot):            #Initialize bot
        self.bot = bot

    #Function for showing every available role
    @commands.command(brief="Shows a list for the available roles",pass_context = True)
    async def roles(self,message):
        get_roles(message)          #Trigger the get_role function

        embed = discord.Embed(title=("The role list for  " + str(message.message.author.server.name)), color=0x53ad80)      #Create the custom embed
        embed.add_field(name="Available roles", value= ("• "+'\n• '.join(roles)) , inline=True)

        await self.bot.send_message(message.message.channel, embed=embed)            #Post the embed

    #Function for adding role to yourself
    @commands.command(brief="Adds role to user", pass_context=True)
    async def addRole(self, message):

        user = message.message.author               #Getting the user who wants to add role
        role = get(user.server.roles, name=message.message.content[9:])         #Getting the role which user wants to add

        if not roles:                   #If the roles list is empty...
            get_roles(message)          #... get the roles by going back to that function

        if (str(role) not in seriousRoles) and (str(role) in roles) and (role not in user.roles):           #Check if the role is safe to assign and user doesn't already have it
            await self.bot.add_roles(user , role)       #Add the role
            await self.bot.say("Done! You have " + str(role) + " now. You can use '-removeRole' command to remove an unwanted role")        #Output the process
        elif role in user.roles:                                    #If user has the role
            await self.bot.say("You already have that role")        #output again
        else:
            await self.bot.say("Sorry that role is not available")

    #Function for removing the role from the user
    @commands.command(brief="Removes role from the user", pass_context=True)
    async def removeRole(self, message):

        user = message.message.author                                           #Get the user
        role = get(user.server.roles, name=message.message.content[12:])        #Get the role

        if role in user.roles:                          #If user has the role...
            await self.bot .remove_roles(user, role)    #... remove the role
            await self.bot.say("Done! Removed the " + str(role) + "role. You can use '-addRole' command to add another role")

        elif role not in user.roles:            #If user doesn't has the role just kindly say it
            await self.bot.say("You don't have that role !")

#Setting the bot and the class
def setup(bot):
    bot.add_cog(roleManagement(bot))
