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
    database = r"../bppsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        today = date.today()
        # tasks
        quote1 = ('Cole','IM NOT SMART ENOUGH!!!!', today.strftime("%d/%m/%y"))

        # create tasks
        create_quote(conn, task_1)



if __name__ == '__main__':
    main()