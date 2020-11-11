from redbot.core import commands
import sqlite3
from sqlite3 import Error

class quotes(commands.Cog):
    """My custom cog"""
    database = r"../bppssqlite.db"

    # create a database connection
    conn = create_connection(database)

    @commands.command()
    async def quote(self, ctx):
        """This does stuff!"""
        quote = select_random_quote(conn)
        # Your code will go here
        await ctx.send(quote)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_random_quote(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT quote FROM table ORDER BY RANDOM() LIMIT 1")

    rows = cur.fetchall()

    return rows