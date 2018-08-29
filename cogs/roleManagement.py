"""
This file contains role management functions for everyone.
The special roles (admin and staff roles (also bot roles)) has to be added to seriousRoles (that will be automated in the future)
"""

import discord
import asyncio
from discord.ext import commands
from discord.utils import get
import sys
sys.path.append("C://Users//eozdi//Documents//ColossusBot//database")
import DBLib as db


class roleManagement(object):

    def __init__(self, bot, roles = []):            #Initialize bot
        self.bot = bot
        self.roles = db.getRoles()

    #Function for showing every available role
    @commands.command(brief="Shows a list for the available roles", pass_context = True)
    async def showRoles(self, message):
        roles = []
        for role in self.roles:
            roles.append("".join(role))
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

    @commands.command(brief="Getting all the roles", pass_context=True)
    async def getRoles(self, message):
        if db.ifAdmin(message.message.author.discriminator):
            self.roles = db.getRoles()

            specialRoles = ["Admin", "Bot", "@everyone", "Intern", "Event Creator"]

            if not self.roles or message.message.content.endswith(" +update"):
                db.clearRoles()
                roles = {}
                for role in message.message.server.roles:
                    if str(role) not in specialRoles:
                        roles[role] = True
                    else:
                        roles[role] = False
                db.saveRoles(roles)
                self.roles = db.getRoles()
                await self.bot.say("Roles saved !")

            else:
                await self.bot.say("There is already " + str(len(self.roles)) +" self assignable role saved to database ! If you want to update roles, you know the command. Right ?")

        else:
            await self.bot.say("Sorry, you don't have the permission to do that.")


#Setting the bot and the class
def setup(bot):
    bot.add_cog(roleManagement(bot))
