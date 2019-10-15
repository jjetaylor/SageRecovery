import discord
from discord.ext import commands



class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='greet')
    async def greet(self, ctx):
        await ctx.send(":smiley: :wave: Hello, there!")

    @commands.command(name='ping')
    async def ping(self, ctx):
        '''
        Check bot latency
        '''
        latency = self.bot.latency 
        await ctx.send(latency)

    @commands.command(name='cj')
    async def cj(self, ctx):
        await ctx.send(":smiley: Fuck Kaiwolf! :wink:")


    @commands.command(name='es')
    async def es(self, ctx, user: discord.Member=None):
        '''
        When you need the Recovery Bot to do your dirty work.
        '''
        await ctx.message.delete()
        await ctx.send(f"Eat Shit {user.mention}")




def setup(bot):
      bot.add_cog(Basic(bot))