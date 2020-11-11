from redbot.core import commands
import sqlite3
from sqlite3 import Error
import os.path


with sqlite3.connect(db_path) as db:


def select_random_quote():
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = None
    try:
        conn = sqlite3.connect("~/redenv/BPPS_Cogs/BPPS_Quotes/bppssqlite.db")
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute("SELECT quote FROM quotes ORDER BY RANDOM() LIMIT 1")

    rows = cur.fetchall()

    return rows

class quotes(commands.Cog):
    """My custom cog"""
    
    @commands.command()
    async def quote(self, ctx):
        """This does stuff!"""
        quote = select_random_quote()
        # Your code will go here
        await ctx.send(quote)
