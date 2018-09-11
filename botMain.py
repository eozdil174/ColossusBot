"""
Bot's main file which loads all the other files.
I put a error throwback and log systems for inspecting the errors
DO NOT PLAY WITH ANYTHING !!!
"""

import discord
from os import listdir
from os.path import isfile , join
from discord.ext import commands
import logging
import traceback
import json


try:
    with open('botConfig.json', 'r') as data:           #Using Json library to load the botConfig file ('r' stands for "read". So the file won't be affected from any kind of write process)
        config = json.load(data)             #Writing the data to config array
except:
    import botSetup                     #We will call the botSetup.py script
    botSetup.showData()

finally:
    with open('botConfig.json', 'r') as data:         #And we will read the data from json again. Whatever happens this will be executed
        config = json.load(data)

bot = commands.Bot(command_prefix='-', description='A bot for all your needs')                       #Defining the bot
bot.remove_command('help')                                                                              #Removing the default help command  to replace my custom one

TOKEN = config["token"]       #Getting the token from the Json file

@bot.event                                                                                              #Setting basic bot things and going to load cogs
async def on_ready():
    await bot.change_presence(game=discord.Game(name=config["game"]))
    print("Version " + discord.__version__)
    print("Alright. Ready for the fly")
    await loadCogs()

async def loadCogs():                                                                                   #Loading the cogs(the other .py files)
    for extension in [f.replace(".py", "") for f in listdir("cogs") if isfile(join("cogs", f))]:
        try:
            if not "__init__" in extension:
                print("loading {} ...".format(extension))
                bot.load_extension("cogs." + extension)
        except exception as e:
            print("Failed to load {}".format(extension))
            traceback.print_exc()

def Main():                                                                                             #Main function to run logging system and starting the bot up
    logging.basicConfig(level=logging.INFO)

    bot.run(TOKEN)

if __name__ == '__main__':                                                                              #Checking if the main file called. Whic is that one
    Main()
