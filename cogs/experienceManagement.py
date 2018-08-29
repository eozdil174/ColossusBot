import discord
from discord.ext import commands
import sys
sys.path.append('C:\\Users\\eozdi\\Documents\\ColossusBot\\database')
import DBLib as db

class experienceManagement():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def addExp(self, message):
        user = message.message.author

        if db.ifAdmin(user.discriminator):
            amount = message.message.content[7:]
            db.addExp(user.discriminator, amount)
            await self.bot.say("%s exp added to %s" % (amount , user.display_name))
        else:
            await self.bot.say("You don't have permission to do that !")

    @commands.command(pass_context=True)
    async def removeExp(self, message):
        user = message.message.author

        if db.ifAdmin(user.discriminator):
            amount = message.message.content[10:]
            db.removeExp(user.discriminator, amount)
            await self.bot.say("%s exp removed from %s" % (amount, user.display_name))
        else:
            await self.bot.say("You don't have permission to do that !")

    @commands.command(pass_context=True)
    async def showExp(self, message):
        pictures = {
            '0'  : 'https://preview.ibb.co/bXyjv9/0.png' ,
            '10' : 'https://preview.ibb.co/fHuMsp/10.png',
            '20' : 'https://preview.ibb.co/cfBedU/20.png',
            '30' : 'https://preview.ibb.co/kpEhyU/30.png',
            '40' : 'https://preview.ibb.co/igOsyU/40.png',
            '50' : 'https://preview.ibb.co/jYwyNp/50.png',
            '60' : 'https://preview.ibb.co/mttjv9/60.png',
            '70' : 'https://preview.ibb.co/dtdv2p/70.png',
            '80' : 'https://preview.ibb.co/mi1b8U/80.png',
            '90' : 'https://preview.ibb.co/ciaga9/90.png'
        }

        userData = db.getUserExp(message.message.author.discriminator)     #Getting the exp of the user

        userExp = float(userData[0])       #Assigning experience
        userLevel = float(userData[1])     #and level from the tuple which returned from DBLib

        targetExp = userLevel * 1000  #Target exp is target level multiplied by 1000 (target exp for level 6 is 6000)

        remainingExp = targetExp - userExp

        line = ""  #An empty string to store line

        lineDrawExp = int((userExp - ((userLevel - 1) * 1000)) / 100)     #It basically does this ; userExp = 5865.6
                                                                                                # (userLevel(It's 6) - 1) * 1000 = 5000
                                                                                                # lineDrawExp = 5865.6 - 5000 = 865.6
        image =  pictures[str(lineDrawExp * 10)]                                                                                       # int(865.6 / 100) = 8 . We will use that 8

        embed = discord.Embed(colour=discord.Colour(0x53ad80))              #Creating the experience embed

        embed.set_author(name=message.message.author)
        embed.set_footer(text="ColossusBot")
        embed.set_image(url = image)
        embed.add_field(name="➡️", value=("Your current experience is : **%d**" % int(userExp)))
        embed.add_field(name="🔢", value=("You are level **%d**" % (int(userLevel) - 1)))
        embed.add_field(name="☑️", value=("You will level up after aproximately **__%d__** messages" % int(remainingExp / 12)), inline=True)

        embed.add_field(name="↗️", value=("Your current state"))

        await self.bot.say(embed=embed)

    @commands.command
    async def newLevelNotif(self, userName ,userLevel):

        await self.bot.say("User %s is now level %d !" % (userName, userLevel))


#Setting the bot and the class up
def setup(bot):
    bot.add_cog(experienceManagement(bot))
