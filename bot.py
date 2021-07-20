import discord
from discord.ext import commands
from json import load
import random

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready')

@client.command()
async def clear(ctx, amount=5):
  # this commands cleans up the chat room by removing the number of chat messages
  # default value of 5
  # it purges the "amount" number of messages from the channel chat with the command ".clear"
  # to clear 2 messages do send the command ".clear 2" (inclusive)
  await ctx.channel.purge(limit=amount)

client.run(SECRET['token'])