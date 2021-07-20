import discord
from discord.ext import commands
from json import load
import random

with open('SECRET', mode='r', encoding='utf-8') as f:
  SECRET = load(f)

with open('8ball.txt', mode='r', encoding='utf-8') as f:
  eightball_responses = f.read().split('\n')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready')

@client.command() # notice the brackets
async def ping(ctx):
  # Name the function whatever you want
  # Unlike previous functions this isn't module function.
  # ctx is the function context
  
  # if you comment ".ping", the bot will say Pong
  await ctx.send('Pong')

  # the following command shows the latency of response
  await ctx.send(f"Pong {round(client.latency * 1000)} ms")

@client.command(aliases=['8ball', "8_ball"])
# aliases means that all the items in the list,
# can invoke the following function
async def eightball(ctx, *, question):
  # * allows you take multiple arguments
  await ctx.send(f"Question: {question}\n Answer: {random.choice(eightball_responses)}")


client.run(SECRET['token'])