import discord
from redbot.core import commands
import random

class SecretSanta(commands.Cog):
    """PM People Using The Bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def sendSantas(self, ctx):
        """Dm users."""
        #determine secret santa order
        allUsers = []
        f = open('secretsanta.txt', 'r')
        for line in f:
            user_id = int(line[3:len(line)-2])
            user = self.bot.get_user(user_id)
            allUsers.append(user)
        random.shuffle(allUsers)
        allUsers.append(allUsers[0])
        f.close()

        #record results just in case
        f = open('secretsanta.txt', 'a')
        for user in allUsers:
            f.append(str(user.name)+" | ")
        f.close()

        #dm users
        for i in range(len(allUsers)-1):
            userToSend = allUsers[i]
            userToRecieve = allUsers[i+1]
            await user.send("Hello <@"+str(userToSend.id)+">, you are the secret santa for **"+userToRecieve.name+"** to send them a gift!")
            await user.send("Consider sending by mail, or if you live closeby you can drop it off")
            await user.send("If you need an address or need to inform someone a package has been delivered, feel free to ask Inabiaf or PointAndGlick to ask on your behalf so you can maintain anonymity.")
            await user.send("When you recieve your gift, *DON'T OPEN IT!* We will be holding a discord call w/ facecam sometime after Christmas where we will open all ours up.")
            await user.send("Merry Christmas, Happy Holidays! :christmas_tree:")

    @commands.command()
    async def addSanta(self, ctx, user):
        # Your code will go here
        names = open('secretsanta.txt', 'a')
        names.write(user+'\n')
        names.close()
        await ctx.send(user+' has been added')
