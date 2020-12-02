from redbot.core import commands
import random

def addEntry(name):
    names = open('secretsanta.txt', 'a')
    names.write(name+'\n')
    names.close()
    return "Chess patch note added to the chain!"

def sendDm():
    names = open('secretsanta.txt', 'r')
    user = names.readline()
    user.send("hello, "+user)
    names.close()
    return "DM'ed"


class SecretSanta(commands.Cog):
    """Chess Patch Notes!"""

    @commands.command()
    async def addSanta(self, ctx, user):
        # Your code will go here
        addEntry(user)
        await ctx.send(user+' has been added')

    @commands.command()
    async def santaTest(self, ctx):
        sendDm()
