import discord
import datetime
from redbot.core import commands

__spiced_up_by__ = "Young™#5484"
__author__ = "Neo#1375"

class SecretSanta(commands.Cog):
    """PM People Using The Bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def santaTest(self, ctx):
        """Dm users."""
        names = open('secretsanta.txt', 'r')
        user_id = names.readline()
        user_id = user_id[3:len(user_id)-2]
        print(self.bot.users)
        user = self.bot.get_user(int(user_id))
        await user.send("hello!")
