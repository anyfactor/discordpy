import discord
from discord.ext import commands
from json import load

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready')

# this is a general error handler function
# this will trigger for all error
# but the caveat is that now your terminal error messages are suppressed
# you won't see errors such as command not found
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please pass all required arguments.')
  elif isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid Command.')

@client.command()
async def clear(ctx, amount:int):
  await ctx.channel.purge(limit=amount)

# this function is specific to the error function
# this function will only get triggered when there is an error with clear function
@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify an amount of messages to delete.')


client.run(SECRET['token'])