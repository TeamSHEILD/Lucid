import discord
import random
import os
import json
import logging
import nekos
import requests
import asyncio
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

with open("prefixes.json") as f:
    prefixes = json.load(f)
default_prefix = "]["

joinlink = 'https://bit.ly/Betr4yz'

client = commands.Bot(command_prefix=commands.when_mentioned_or("[]"))
client.remove_command('help')
logging.basicConfig(level=logging.INFO)
status = cycle(["[] | Sub 2 Chaseyy on yt!", "[] | OwO whats this?", "[]invite", "[]help"])

@client.event
async def on_ready():
    change_status.start()
    print(f'Successfully logged in as {client.user.name}!')
    print(f"ID = {client.user.id}")

@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, exception):
    error = getattr(exception, "original", exception)
    if isinstance(error, discord.NotFound):
        return
    elif isinstance(error, discord.Forbidden):
        return
    elif isinstance(exception, commands.BadArgument):
        return
    elif isinstance(exception, commands.CommandNotFound):
        await ctx.send(f'We couldn\'t find that command :(\n\nPlease try again or use []help')
    elif isinstance(exception, commands.MissingRequireArgument):
        await ctx.send(f'Command is missing required argument :(')
    return

@client.command
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}') 

#@load.error
#async def clear_error(ctx, error):
#    if isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send('Command Unavaliable')


#@client.event
#async def on_member_join(ctx, member):
#    print(f'{member} Has joined {ctx.guild}')
    #role = discord.utils.get(ctx.guild.roles, name = "member")
    #await ctx.add_roles(role)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Adding to update file for token :)

client.run('TOKEN')
