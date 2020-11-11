from .quotes import quotes


def setup(bot):
    bot.add_cog(quotes())