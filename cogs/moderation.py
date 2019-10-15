import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions



class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear')
    @has_permissions(administrator=True)
    async def clear(self, ctx, amount=100):
        #if ctx.message.author.server_permissions.administrator:
        await ctx.channel.purge(limit=int(amount+1))

    #Section used to add new users to the temp role
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="temp")
        await member.add_roles(role)



def setup(bot):
      bot.add_cog(Moderation(bot))





