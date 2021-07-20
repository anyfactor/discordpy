import discord
from discord.ext import commands
from json import load

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

client = commands.Bot(command_prefix = '.')

# the decorator client is referencing the client variable above.
@client.event
async def on_ready():
  print('Bot is ready')

@client.event
async def on_member_join(member):
# member is a object that can do a lots of things; refer docs
# this function runs when a member joins the server
  print(f"{member} has joined the server.")

@client.event
async def on_member_remove(member):
  print(f"{member} has left the server")

client.run(SECRET['token'])