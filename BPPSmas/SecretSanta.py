import discord
from redbot.core import commands
import random

__spiced_up_by__ = "Young™#5484"
__author__ = "Neo#1375"

class SecretSanta(commands.Cog):
    """PM People Using The Bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def sendSantas(self, ctx):
        """Dm users."""
        allUsers = []
        f = open('secretsanta.txt', 'r')
        for line in f:
            user_id = int(line[3:len(line)-2])
            user = self.bot.get_user(user_id)
            allUsers.append(user)
        random.shuffle(allUsers)
        allUsers.append(allUsers[0])

        for i in range(len(allUsers)-1):
            userToSend = allUsers[i]
            userToRecieve = allUsers[i+1]
            await user.send("Hello "+userToSend.name+", you are the secret santa for "+userToRecieve+" to send them a gift! Consider dropping off their present while social distancing at their house, or send my mail. Merry Christmas, Happy Holidays!")
