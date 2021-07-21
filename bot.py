import discord
from discord.ext import commands
from json import load

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

client = commands.Bot(command_prefix = '.')

### Part 7: Bot Status
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle,
                              activity=discord.Game("Hello There"))
                              # bot online status
                              # Bot playing "Hello There"
  print('Bot is ready')


client.run(SECRET['token'])