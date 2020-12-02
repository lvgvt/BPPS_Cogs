from .SecretSanta import SecretSanta

def setup(bot):
    bot.remove_command('whisper')
    n = SecretSanta(bot)
    bot.add_cog(n)