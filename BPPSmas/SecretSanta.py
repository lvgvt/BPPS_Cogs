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
            await user.send("Hello <@"+str(userToSend.id)+">, you are the secret santa for **"+userToRecieve.name+"** to send them a gift!")
            await user.sent("Consider dropping off their present at their house while social distancing, or send my mail.")
            await user.send("Merry Christmas, Happy Holidays!")

    @commands.command()
    async def addSanta(self, ctx, user):
        # Your code will go here
        names = open('secretsanta.txt', 'a')
        names.write(user+'\n')
        names.close()
        await ctx.send(user+' has been added')