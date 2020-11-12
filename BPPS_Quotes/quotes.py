from redbot.core import commands
import sqlite3
from sqlite3 import Error
from datetime import date

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
    today = date.today().strftime("%m/%d/%y")
    record = (author, quote, today)
    sql = ''' INSERT INTO quotes(author,quote,date_added)
                VALUES(?,?,?) '''
    cur.execute(sql, record)

class quotes(commands.Cog):
    """My custom cog"""
    
    @commands.command()
    async def quote(self, ctx):
        """This does stuff!"""
        quote = select_random_quote()
        # Your code will go here
        await ctx.send(quote)

    @commands.command()
    async def addquote(self, ctx, quote, author):
        """Adds a quote to the list"""
        ""
        # Your code will go here
        await ctx.send("Added: \""+quote+"\" by "+author)
