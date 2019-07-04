#################################################
#Importing Libraries, Variables, Modules, ect...
#################################################

#Import custom variables from custvar.py file
import custvar

#Import commands from Discord library
import discord
from discord.ext import commands

#Import random
import random

#Import logging capabilities.
#import logging

#################################################
#Logging
#
#logging levels: debug, info, warning, error, and critical
#################################################
#logging.basicConfig(level=logging.INFO, filename='/var/log/sagerecovery/logging.debug', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#################################################
#Where the prefix for the bot it set.
#################################################
bot = commands.Bot(command_prefix='sr!')

#################################################
#The main functions of the bot
#################################################
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#@bot.event
#async def on_message(message):
    #print("The message's content was", message.content)


@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cj(ctx):
    await ctx.send(":smiley: Fuck Kaiwolf! :wink:")

@bot.event
async def on_message(message):
     if message.author != bot.user:
         if 'yeet' in message.content:

             yeetop = [
                 'YeYEEEET'
                 'Oh God! :rolling_eyes:',
                 'Not Again!',
                 'You call that a Yeet? This is a YEEEEEET!',
                 'Leroy JENKINS!!'
                 ]
             await message.channel.send(random.choice(yeetop))
     await bot.process_commands(message)

bot.run(custvar.api_token)
