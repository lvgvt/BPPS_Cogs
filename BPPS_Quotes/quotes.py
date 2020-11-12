from redbot.core import commands
import sqlite3
from sqlite3 import Error
import os.path

def select_random_quote():
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = None
    try:
        conn = sqlite3.connect("./bppssqlite.db")
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")

    rows = cur.fetchone()
    quote = rows[1].replace('\n', '')
    author = rows[2]
    date = rows[3]
    return quote+" -"+author+" added on "+date

class quotes(commands.Cog):
    """My custom cog"""
    
    @commands.command()
    async def quote(self, ctx):
        """This does stuff!"""
        quote = select_random_quote()
        # Your code will go here
        await ctx.send(quote)
