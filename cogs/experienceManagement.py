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
        db.getUserData(message.message.author.discriminator)     #Getting the exp of the user









#Setting the bot and the class up
def setup(bot):
    bot.add_cog(experienceManagement(bot))
