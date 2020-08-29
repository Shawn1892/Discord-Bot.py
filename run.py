import discord
from discord.ext import commands

shawn = commands.Bot(command_prefix = '!')

@shawn.event
async def on_ready():
  print('Ok bot is running, note you are a loser (just kidding) using my tutorials as lessons or whatever :p')

shawn.run('[BOT TOKEN HERE]')

// (REMOVE THIS) Note: You can get a bot token by creating an application (https://discord.com/developers/applications), creating the bot, and then copy the token thats given inside the bot's profile. //
