import discord
from discord.ext import commands
import sys
sys.path.append('C:\\Users\\eozdi\\Documents\\ColossusBot\\database')
import DBLib as db

class experienceManagement(object):
    def __init__(self, bot, exp = 0):
        self.bot = bot
        self.exp = exp

    @commands.command(pass_context=True)
    async def showExp(self, message):
        userData = db.getUserData(message.message.author.discriminator)     #Getting the exp of the user

        userExp = float(userData[0])       #Assigning experience
        userLevel = float(userData[1])     #and level from the tuple which returned from DBLib

        targetExp = userLevel * 1000  #Target exp is target level multiplied by 1000 (target exp for level 6 is 6000)

        remainingExp = targetExp - userExp

        line = ""  #An empty string to store line

        lineDrawExp = int((userExp - ((userLevel - 1) * 1000)) / 100)     #It basically does this ; userExp = 5865.6
                                                                                                # (userLevel(It's 6) - 1) * 1000 = 5000
                                                                                                # lineDrawExp = 5865.6 - 5000 = 865.6 # int(865.6 / 100) = 8 . We will use that 8
        for i in range(10):
            if i == lineDrawExp:
                line += 'o'
            elif i < lineDrawExp:
                line += '='
            elif i > lineDrawExp:
                line += '-'


        embed = discord.Embed(colour=discord.Colour(0x53ad80))

        embed.set_author(name=message.message.author)
        embed.set_footer(text="ColossusBot")

        embed.add_field(name="➡️", value=("Your current experience is : **" + str(int(userExp)) + "**"), inline=True)
        embed.add_field(name="🔢", value=("You are level **" + str(int(userLevel - 1)) + "**"), inline=True)
        embed.add_field(name="☑️", value=(("You will level up after aproximately **__" + str(int(remainingExp / 12)) + "__** messages")), inline=True)
        embed.add_field(name="🆙", value=(("Next level is : **" + str(int(userLevel))) + "**"), inline=True)
        embed.add_field(name="↗️", value=("Your current state : **" + line +"**"), inline=True)

        await self.bot.say(embed=embed)






#Setting the bot and the class up
def setup(bot):
    bot.add_cog(experienceManagement(bot))
