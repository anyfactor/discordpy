import discord
from discord.ext import commands

class Example(commands.Cog):
  def __init__(self, client):
    self.client = client

# This will show up in the terminal
  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot is ready")

# standard ping funcion with ".ping"
  @commands.command()
  async def ping(self, ctx):
    await ctx.send('Pong!')

# when you load the Cog from the bot file
# it comes here
# it triggers the setup file
# then uses it's client function to add the cog
# then it loads the Example Class which is the cog extension
# it passes the client function to it
def setup(client):
  client.add_cog(Example(client))
