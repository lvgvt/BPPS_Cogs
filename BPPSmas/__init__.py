from .SecretSanta import SecretSanta

def setup(bot):
    n = SecretSanta(bot)
    bot.add_cog(n)