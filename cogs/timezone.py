import discord
from discord.ext import commands
import datetime
import pytz


class Time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ctz')
    async def ctz(self, ctx, dt, tz1, tz2):
        tz1 = pytz.timezone(tz1)
        tz2 = pytz.timezone(tz2)

        dt = datetime.datetime.strptime(dt,"%H:%M")
        dt = tz1.localize(dt)
        dt = dt.astimezone(tz2)
        dt = dt.strftime("%H:%M")
        await ctx.send(dt)



def setup(bot):
     bot.add_cog(Time(bot))