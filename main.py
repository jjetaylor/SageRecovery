#################################################
#Importing Libraries, Variables, Modules, ect...
#################################################

#Import custom variables from custvar.py file
import custvar
import os

#Import other Libraries ect..
import random
import time
import asyncio
import datetime
from datetime import timedelta


#Import commands from Discord library
import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions
#from discord.ext.commands import Bot
from discord.utils import get



#################################################
#Cogs
#################################################
initial_extensions = ['cogs.simple',
                      #'cogs.logging',
                      #'cogs.database',
                      'cogs.backup',
                      'cogs.moderation',
                      'cogs.timezone'
                      ]


#################################################
#Bot Prefix
#################################################
bot = commands.Bot(command_prefix=custvar.prefix)


#################################################
#Loading Cogs
#################################################
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


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
          if 'yeet' in message.content.lower():
              yeetop = [
                  'YeYEEEET',
                  'Oh God! :rolling_eyes:',
                  'Not Again!',
                  'You call that a Yeet? This is a YEEEEEET!',
                  'Leroy JENKINS!!'
                  ]
              await message.channel.send(random.choice(yeetop))

      if message.author != bot.user:
          waitphraselist = [
              '1 sec',
              'hold on',
              'give me a second',
              'give me a sec',
              'just a sec',
              'one moment',
              '1 moment',
              'gimme a sec',
              'unsec'
          ]          
          for waitphrase in list(waitphraselist):
              if waitphrase in message.content.lower():
                  await message.channel.send('started timer')
                          
                  async def countdown():
                      await bot.wait_until_ready()
                      counter = 0
                      while counter < 2:
                          counter = counter + 1
                          print(counter)
                          await asyncio.sleep(1)
                      await message.channel.send('{0.author.mention}: Your 1 minute is up!')
                  bot.loop.create_task(countdown())
                        


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
async def shadowkeep(ctx):
    format = "%a %b %d %H:%M:%S %Y"
    skdt = datetime.datetime(2019, 10, 1)
    await ctx.send(f'ShadowKeep Release Date is: {skdt}')
    # This gives timedelta in days
    #dt(year=2011,month=05,day=05) - dt(year=now.year, month=now.month, day=now.day)
    # This gives timedelta in days & seconds
    #dt(year=2019,month=10,day=01) - dt(year=now.year, month=now.month, day=now.day, minute=now.minute))
    
    skcd = (skdt - datetime.datetime.now())
    await ctx.send(f'There are {skcd.strftime("%b-%d, %Y")} days until release')


#----------------------------------------------
#end Bot commands  section.
#----------------------------------------------

#if __name__ == '__main__':
token = os.environ.get("sage_rec_api_token")
#print(token)
bot.run(token)
