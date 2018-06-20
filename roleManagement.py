import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

roles = {}
seriousRoles = {'Admin', 'Intern','Event Creator','Bot','@everyone'}

def get_roles(user):
    for role in user.server.roles:
        if str(role) not in seriousRoles:
            roles[str(role)] = role.id

    print (roles)

def add_role(user, role):
    get_roles(user)
    print (role)

    if str(role) in roles:
        print("It's there and available")
    else:
        print("Wut ?")
