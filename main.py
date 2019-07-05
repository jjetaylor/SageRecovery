#################################################
#Importing Libraries, Variables, Modules, ect...
#################################################

#Import custom variables from custvar.py file
import custvar

#Import other Libraries ect..
import csv
import time
import random
import logging
import tempfile

#Import commands from Discord library
import discord
from discord.ext import commands
from discord.ext.commands import Bot
#from discord.ext.commands import Bot



#################################################
#Logging
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



#################################################
#On Message section. All on_message statements 
# must fall under this one section.
#################################################
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

#This portion of the on_message is to provide users with helpful information
#about the bot. If you @ this bot, it will respond with its prefix. 
     if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'help' in message.content.lower():
             await message.channel.send(f'My prefix is "{custvar.prefix}". Please try "{custvar.prefix}help" for more information.')



     await bot.process_commands(message)
#----------------------------------------------
#end On message section. Do not put any 
#on_message code below await bot.process 
#command. 
#----------------------------------------------



###############################################
#Begin Bot commands section.
###############################################
@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cj(ctx):
    await ctx.send(":smiley: Fuck Kaiwolf! :wink:")

#Section used to get user list from server and
#export to excel spreedsheet
@bot.command(pass_context=True)
async def userlist(ctx):
    """Returns a CSV file of all users on the server."""
    if ctx.guild.large == 'true':
        await bot.request_offline_members(ctx.guild.members)
    before = time.time()
    nicknames = [m.display_name for m in ctx.guild.members]
    tf = tempfile.NamedTemporaryFile(suffix='.csv')
    with open(tf.name, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        for v in nicknames:
            writer.writerow([v])
    after = time.time()
    await ctx.message.author.send(content=(f'Please see the attached user list for your server: {ctx.guild}'), file=discord.File(tf.name))



#----------------------------------------------
#end Bot commands  section.
#----------------------------------------------




if __name__ == '__main__':
     bot.run(custvar.api_token)
