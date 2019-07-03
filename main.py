#################################################
#Importing Libraries, Variables, Modules, ect...
#################################################

#Import custom variables from custvar.py file
import custvar

#Import commands from Discord library
import discord
from discord.ext import commands

#Import logging capabilities.
import logging


#################################################
#Logging
#
#logging levels: debug, info, warning, error, and critical
#################################################
#logging.basicConfig(level=logging.INFO, filename='/var/log/sagerecovery/logging.debug', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#################################################
#Where the prefix for the bot it set.
#################################################
bot = commands.Bot(command_prefix=custvar.prefix)

#################################################
#The main functions of the bot
#################################################
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    print("The message's content was", message.content)


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cj(ctx):
    await ctx.send(":smiley: Fuck Kaiwolf! :wink:")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

bot.run(custvar.api_token)
