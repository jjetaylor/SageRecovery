import discord
from discord.ext import commands



class Announcement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='dates')
    async def dates(self, ctx):
        with open('season-dates.txt', 'r') as reader:
            await ctx.send(reader.read())




def setup(bot):
      bot.add_cog(Announcement(bot))
