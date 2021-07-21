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

#### Clear Function: Part 4
@client.command()
async def clear(ctx, amount=5):
  # this commands cleans up the chat room by removing the number of chat messages
  # default value of 5
  # it purges the "amount" number of messages from the channel chat with the command ".clear"
  # to clear 2 messages do send the command ".clear 2" (inclusive)
  await ctx.channel.purge(limit=amount)

#### Kick/Ban: Part 5
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  # The asterisk says all of the param added after member and reason will be added reason
  await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)

# Command to send
# .kick @account
# .ban @account Spam Account

#### Unban: Part 6

# We get access to the Member object with discord.Member
# But the member must be part of the channel to give us that object
# After banning the member is out of the channel
# So we can't get that object normally
@client.command()
async def bank(ctx, *, member):
  # the asterisk is here because account names can contain spaces
  banned_users = await ctx.guild.bans()
  # this function returns all the banned users on the server
  # returns a named tuple
  member_name, member_discriminator = member.split("#")
  # account: anyfactor#8591

  for ban_entry in banned_users:
    user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      # await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
      # this is essentially the same as this but this string mentions
      await ctx.send(f"Unbanned {user.mention}")
      return




client.run(SECRET['token'])