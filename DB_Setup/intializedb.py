import sqlite3
from sqlite3 import Error
from datetime import date



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_quote(conn, quote):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO quotes(author,quote,date_added)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, quote)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"./bppssqlite.db"

    # create a database connection
    conn = create_connection(database)

    sql_create_quotes_table = """ CREATE TABLE IF NOT EXISTS quotes (
                                        id integer PRIMARY KEY,
                                        author text NOT NULL,
                                        quote text,
                                        date_added text
                                    ); """

    with conn:
        try:
            c = conn.cursor()
            c.execute(sql_create_quotes_table)
        except Error as e:
            print(e)
        today = date.today()
        f = open("quotes.txt", "r")
        for l in f:
            line = l.split('*')
            quote = (line[0],line[1], today.strftime("%d/%m/%y"))
            create_quote(conn, quote)
        f.close()


if __name__ == '__main__':
    main()
