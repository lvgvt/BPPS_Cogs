from redbot.core import commands
import random

def addEntry(name):
    names = open('secretsanta.txt', 'a')
    names.write(name+'\n')
    names.close()
    return "Chess patch note added to the chain!"


class SecretSanta(commands.Cog):
    """Chess Patch Notes!"""

    @commands.command()
    async def addSanta(self, ctx, name):
        # Your code will go here
        addEntry(name)
        await ctx.send(name+' has been added')
