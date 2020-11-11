from redbot.core import commands

class quotes(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def quote(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")