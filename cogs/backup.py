import discord
from discord.ext import commands
import csv
import tempfile
import time



class Backup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    #Section used to get user list from server and
    #export to excel spreedsheet
    @commands.command(name='userlist' , pass_context=True)
    async def userlist(self, ctx):
        """Returns a CSV file of all users on the server."""
        if ctx.guild.large == 'true':
            await bot.request_offline_members(ctx.guild.members)
        before = time.time()
        nicknames = [m.display_name for m in ctx.guild.members]
        user_name = [m.name for m in ctx.guild.members]
        #user: discord.Member=None - gives the whole user and # sine. Might be worth using
        discrim = [m.discriminator for m in ctx.guild.members]
        zip(nicknames, user_name, discrim)

        tf = tempfile.NamedTemporaryFile(suffix='.csv')
        #with open(tf.name, mode='w', encoding='utf-8', newline='') as f:
        with open(tf.name, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            #for v in nicknames:
                #writer.writerow([v])
            writer.writerow(zip(nicknames, user_name, discrim))
        after = time.time()
        await ctx.message.author.send(content=(f'Please see the attached user list for your server: {ctx.guild}'), file=discord.File(tf.name))



def setup(bot):
      bot.add_cog(Backup(bot))


