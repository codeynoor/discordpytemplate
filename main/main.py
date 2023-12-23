import discord
from discord.ext import commands
import asyncio

prefix = 'YOUR_PREFIX' # Enter a prefix
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

# Remove the built-in help and ping commands
client.remove_command('help') 
client.remove_command('ping')

@client.event
async def on_ready():
  print(f'\nLogged in as {client.user}\nJoined servers: {len(client.guilds)}')

# Error handler
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CommandNotFound):
    await ctx.send("The specified command doesn't exist")
  else:
    await ctx.send("An error occured")
    print(error)

# Example command
@client.command(name="ping", description="Ping command")
async def ping(ctx):
  await ctx.send(f'{round(client.latency * 1000)} ms')

# Start your bot 
client.run('YOUR_TOKEN') 
