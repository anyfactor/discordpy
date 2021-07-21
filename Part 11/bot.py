import discord
from discord.ext import commands
from json import load

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("Bot is ready")

@client.command()
@commands.has_permissions(manage_messages=True)
# Restricts access to the people who can delete and manage messages in a channel
async def clear(ctx, amount=10):
  await ctx.channel.purge(limit=amount)

def is_it_me(ctx):
  return ctx.author.id ==  12351254312344123 # get ID from account

@client.command()
@commands.check(is_it_me) # custom check function
# if this is True then the function runs
async def example(ctx):
  await ctx.send(f'Hi I am {ctx.author}')

client.run(SECRET['token'])