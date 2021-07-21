import discord
from discord.ext import commands
from discord.ext import tasks # importing task
from itertools import cycle # using infinite cycle
from json import load

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

client = commands.Bot(command_prefix = '.')
# status to be cycled
status = cycle(['Status 1', 'Status 2'])

@client.event
async def on_ready():
  change_status.start()
  print('Bot is ready')

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))


client.run(SECRET['token'])