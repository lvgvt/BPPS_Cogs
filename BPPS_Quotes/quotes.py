from redbot.core import commands
import sqlite3
from sqlite3 import Error
import os.path

def select_random_quote():
    conn = None
    try:
        conn = sqlite3.connect("./bppssqlite.db")
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")

    rows = cur.fetchone()
    quote = rows[2].replace('\n', '')
    author = rows[1]
    date = rows[3]
    return "\""+quote+"\" -"+author+", added on "+date+"."

def add_quote(quote, author):
    conn = None
    try:
        conn = sqlite3.connect("./bppssqlite.db")
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute("INSERT INTO ")

class quotes(commands.Cog):
    """My custom cog"""
    
    @commands.command()
    async def quote(self, ctx):
        """This does stuff!"""
        quote = select_random_quote()
        # Your code will go here
        await ctx.send(quote)

    @commands.command()
    async def addquote(self, ctx, quote):
        """This does stuff!"""
        ""
        # Your code will go here
        await ctx.send("Added: "+quote)
