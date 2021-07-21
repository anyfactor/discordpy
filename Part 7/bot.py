import discord
from discord.ext import commands
from json import load

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

client = commands.Bot(command_prefix = '.')

# Part 7: Cogs

# Cog extension is like class module that you can use like an extension
# this function loads the COG extension
# can be triggered with the message ".load"
@client.command()
async def load(ctx, extension):
  await ctx.send(f'{extension} loaded')
  client.load_extension(f'cogs.{extension}')

# this function unloads the function
# can be triggered with ".unload"
# When you unload a function you can't use that extension anymore
@client.command()
async def unload(ctx, extension):
  await ctx.send(f'{extension} unloaded')
  client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
  await ctx.send(f'{extension} reloaded')
  client.load_extension(f'cogs.{extension}')
  client.unload_extension(f'cogs.{extension}')

import os
# Going to the examples directory and loading all the python files as Cogs
for filename in os.listdir("./cogs"):
  if filename.endswith('.py'):
    # just inputting the name of the python file
    client.load_extension(f'cogs.{filename[:-3]}') # cuts the .py part


client.run(SECRET['token'])