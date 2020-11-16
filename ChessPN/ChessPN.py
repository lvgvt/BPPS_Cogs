from redbot.core import commands
import random

def chesspn_generator():
    pns = open('input.txt', 'r').read()
    pns = ''.join([i for i in pns if not i.isdigit()]).replace("\n", ", ").replace("  ", " ").split(' ')
    
    index = 1
    chain = {}
    count = 15
    
    for word in pns[index:]:
        key = pns[index-1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    endings = ['can', 'the', 'by', ',', 'no', 'to', 'from', 'a', 'if', 'is', 'has', 'of', 'at']
    for i in range(3):
        if list(filter(message.lower().endswith, endings)) != []:
            message = message.rsplit(' ', 1)[0] 
    return message+"."

def addpatchnote(input):
    pns = open('input.txt', 'w')
    pns.write(input+'\n')
    return "Chess patch note added to the chain!"


class ChessPN(commands.Cog):
    """Chess Patch Notes!"""
    
    @commands.command()
    async def chesspn(self, ctx):
        # Your code will go here
        await ctx.send(chesspn_generator())

    @commands.command()
    async def addpn(self, ctx, input):
        # Your code will go here
        await ctx.send(addpatchnote(input))