"""
That file contains some basic and useful features for the bot.
"""

import discord
from discord.ext import commands
import datetime
import sys
sys.path.append('C:\\Users\\eozdi\\Documents\\ColossusBot\\database')
import DBLib as DB

class Core(object):

    def __init__(self, bot):                #Initializing the bot
        self.bot = bot

    #Some hello function just for checking the bot's main functions
    @commands.command(brief='Basic hello function',pass_context=True)
    async def hello(self, ctx):
        await self.bot.say("Hello! " + ctx.message.author.mention)

    #Basic function for testing the bot's status
    @commands.command(brief="Use it only if you are thinkning bot is going to die")
    async def ping(self):
        await self.bot.say("Pong! " + ':ping_pong:')

    #Help command which creates an custom embed to make it look fancy
    @commands.command(brief="Shows that message")
    async def help(self):
        embed = discord.Embed(title="The available commands", colour=0x53ad80, description="You can use all the commands listed below")                 #Creating the embed

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/450150175290163221/459833983400673280/ColossusFedora.png")                          #Adding thumbnail and other things. I'm not gonna explain everything
        embed.set_author(name="ColossusBot", icon_url="https://cdn.discordapp.com/attachments/450150175290163221/459833983400673280/ColossusFedora.png")

        embed.add_field(name="General Commands", value="**__help__** : Shows that message"+
                                                     "\n**__hello__** : Responds with a warm hello message"+
                                                     "\n**__ping__** : Checks the bot's status",
                                                     inline=True)

        embed.add_field(name="Utility Commands", value="**__timeNow__** : Shows the time based bot's location"+
                                                     "\n**__feedback__** : Anonymously sends a message to #feedback channel"+
                                                     "\n**__venting__** : Anonymously sends a message to #venting channel"+
                                                     "\n**__addRole__** : Use it to get the role you want"+
                                                     "\n**__removeRole__** : Use it to get rid of the role you have",
                                                    inline=True)

        await self.bot.say(embed=embed)                 #Printing the embed


    @commands.command(pass_context=True)            #Sending a invite likn via dm message to whoever types the commands
    async def invite(self, message):
        await self.bot.send_message(message.message.author, "You can invite me via this link https://discordapp.com/oauth2/authorize?client_id=452689243865612304&scope=bot")

    #Trigger which activates when new member comes
    async def on_member_join(self, member):

        embed = discord.Embed(title="**New Member Joined !**", colour=discord.Colour(0x53ad80), timestamp=datetime.datetime.utcfromtimestamp(int(time.time())))

        embed.set_image(url="https://preview.ibb.co/e35VwU/Server_Banner.png")

        await self.bot.send_message(discord.Object(id='437654104827756544'), embed=embed)

        DB.saveEntry(member.display_name, member.discriminator)
    #A trigger which activates when a member leaves
    async def on_member_remove(self, member):
        embed = discord.Embed(colour=0x53ad80, description=(member.display_name + ' #' + member.discriminator + " left the server"))

        embed.set_author(name=(str(member.display_name) + " left the server"))
        embed.set_footer(text=("ID: "+ str(member.id) + ' • ' + str(datetime.datetime.now())))

        await self.bot.send_message(discord.Object(id='437688399755870208'), embed=embed)
        DB.deleteEntry(member.discriminator)

    #Trigger which activates on every message
    async def on_message(self, message):
        msg = message.content   #Geting the message

        exp = len(msg) * 0.3    #Calculating the experience (0.3 exp per character)
        levelUp = DB.addExp(message.author.discriminator, exp)    #Adding the exp to user via DBLib. Also checking if user has leveled up via levelUp variable.
        if levelUp:
            await self.bot.send_message(message.channel ,("%s has leveled up to %d ! 🎉" % (message.author.display_name, levelUp[1])))                                                                                                                    #This might be a horrible solution

        #Foreign invite preventation feature
        if "discord.gg" in msg:         #tests for "discord.gg" in message
            print('Server link detected !')
            print('Message posted by ' + message.author.display_name) #Printing the author of the server message
            print('Message : ' + msg)

            invtest = 1                 #sets up variable that controls if the invite is in the links array
            links = ['gwH4jqW','ypVMXd4']
            for link in links:          #tests user message for every item in array
                if link in msg:
                    invtest = 0         #if the message contains the variable is set to false
            if invtest == 1:
                await self.bot.delete_message(message) #deletes the message if the invite isn't approved
                embed = discord.Embed(title="UNKNOWN SERVER LINK DETECTED !", colour=0x53ad80, description="Please use only our allowed invites for inviting people to here ;\n [Café Tesla](https://discord.gg/gwH4jqW) (https://discord.gg/gwH4jqW) or \n [Café Tesla](https://discord.gg/ypVMXd4) (https://discord.gg/ypVMXd4)", timestamp=datetime.datetime.now())

                embed.set_author(name=message.author.display_name)
                embed.set_footer(text="ColossusBot", icon_url="https://cdn.discordapp.com/attachments/450150175290163221/459833983400673280/ColossusFedora.png")

                await self.bot.send_message(message.channel, embed=embed)



#Setting up the bot for usage
def setup(bot):
    bot.add_cog(Core(bot))
