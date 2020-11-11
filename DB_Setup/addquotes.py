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
    database = r"../bppssqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        today = date.today()
        # tasks
        quote1 = ('Cole','YOU CAN\'T RUN FROM BIRDS FUCK MAN!!!!', today.strftime("%d/%m/%y"))
        quote2 = ('Cole','uh oh, UH OH!" *dead*', today.strftime("%d/%m/%y"))
        quote3 = ('Cole','THERE ARE NO BRAKES ON THE SPIRIT BREAKER TRAIN!!! *charges under enemy t1 on entire enemy team*', today.strftime("%d/%m/%y"))
        quote4 = ('Cole','https://gfycat.com/orderlygrippingaplomadofalcon', today.strftime("%d/%m/%y"))
        quote5 = ('Cole','We gave them a thrashing they\'ll not soon forget', today.strftime("%d/%m/%y"))
        quote6 = ('Cole','He is embarrassed as fuck, like super tsundere style', today.strftime("%d/%m/%y"))
        quote7 = ('Cole','FBI more like Fuck Bois Incorporated', today.strftime("%d/%m/%y"))
        quote8 = ('Cole','Rising Tide, Splitting Headache" (Cole\'s ultimate ability)', today.strftime("%d/%m/%y"))
        quote9 = ('Cole','Because I have no friends and no one to talk to', today.strftime("%d/%m/%y"))
        quote10 = ('Cole','They weren’t silver ones, they were half silver twos', today.strftime("%d/%m/%y"))
        quote11 = ('Cole','I will not stop playing dota 2 until I win a game starting now...” Cole, on setting goals', today.strftime("%d/%m/%y"))
        quote12 = ('Cole','Hey lawrence what the fuck was that', today.strftime("%d/%m/%y"))
        quote13 = ('Cole','I will not stop playing dota 2 until I win a game starting now” - Cole, on learning from his mistakes
', today.strftime("%d/%m/%y"))
        quote14 = ('Cole','Default dances on your dead body', today.strftime("%d/%m/%y"))
        quote15 = ('Cole','size comparison owo', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
       # quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        #quote10 = ('Cole','ssssssss', today.strftime("%d/%m/%y"))
        

        # create tasks
        create_quote(conn, quote1)
        create_quote(conn, quote2)
        create_quote(conn, quote3)
        create_quote(conn, quote4)
        create_quote(conn, quote5)
        create_quote(conn, quote6)
        create_quote(conn, quote7)
        create_quote(conn, quote8)
        create_quote(conn, quote9)
        create_quote(conn, quote10)
        create_quote(conn, quote11)
        create_quote(conn, quote12)
        create_quote(conn, quote13)
        create_quote(conn, quote14)
        create_quote(conn, quote15)


if __name__ == '__main__':
    main()
