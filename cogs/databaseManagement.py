import discord
from discord.ext import commands
import sys
sys.path.append('/usr/ColossusBot/database/')
import DBLib as DB

class DatabaseManagement(object):
    """docstring for DatabaseManagement."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def check(self, ctx):
        await self.bot.say(DB.getEntries())

    @commands.command(pass_context=True)
    async def getPeople(self, ctx):
        if DB.ifAdmin(ctx.message.author.discriminator) or ctx.message.author.discriminator == '9600':
            server = ctx.message.server

            for user in server.members:
                DB.saveEntry(user.display_name, user.discriminator)
            await self.bot.say("Done!")


    @commands.command(pass_context=True)
    async def cookieJar(self, message):
        user = message.message.author

        await self.bot.say("You have " + str(DB.getCookies(user.discriminator)) + ':cookie:')

    @commands.command(pass_context=True)
    async def giveCookies(self, message):
        donatorUser = message.message.author.discriminator
        donatorCurrency = DB.getCookies(donatorUser)
        i = message.message.content.split('@', 1)
        i = str(i[0])
        cookieVal = i[13:(len(i) - 2)]

        if int(cookieVal) < 0 or int(cookieVal) > int(donatorCurrency):
            await self.bot.say("You can't send your debts to another person ! You have to pay them !")

        else:
            targetUser = message.message.mentions[0].discriminator
            DB.giveCookies(donatorUser, cookieVal, targetUser)

            await self.bot.say("Done! "+ cookieVal + " Cookies sent to " + message.message.mentions[0].mention)


def setup(bot):
    bot.add_cog(DatabaseManagement(bot))
