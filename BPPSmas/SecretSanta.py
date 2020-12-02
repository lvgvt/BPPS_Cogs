from redbot.core import commands

def addEntry(name):
    names = open('secretsanta.txt', 'a')
    names.write(name+'\n')
    names.close()
    return "Chess patch note added to the chain!"

def sendDm(bot):
    names = open('secretsanta.txt', 'r')
    userID = names.readline()
    userID = userID[2:len(userID)-2]
    bot.get_user(userID).send("hello")
    names.close()
    return userID


class SecretSanta(commands.Cog):
    """Chess Patch Notes!"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def addSanta(self, ctx, user):
        # Your code will go here
        addEntry(user)
        await ctx.send(user+' has been added')

    @commands.command()
    async def santaTest(self, ctx):
        await ctx.send("DM'ed ID: "+sendDm(self.bot))
