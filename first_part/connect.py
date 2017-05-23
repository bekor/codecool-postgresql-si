import psycopg2


def connect_to_sql(func):
    def with_connection():
        try:
            # setup connection string
            connect_str = my_connection()
            # use our connection values to establish a connection
            conn = psycopg2.connect(host=connect_str["host"],
                                    user=connect_str["user"],
                                    password=connect_str["passwd"],
                                    dbname=connect_str["dbname"])
            # set autocommit option, to do every query when we call it
            conn.autocommit = True
            # create a psycopg2 cursor that can execute queries
            cursor = conn.cursor()
            rv = func(cursor)
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)
            conn.rollback()
            raise
        else:
            conn.commit()
        finally:
            conn.close()
        return rv
    return with_connection


def my_connection():
    connect = {"host": 'localhost',
               "user": 'bekor',
               "passwd": 'Almafa666',
               "dbname": 'bekor'}
    return connect
