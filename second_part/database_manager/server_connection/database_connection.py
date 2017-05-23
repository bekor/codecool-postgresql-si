import psycopg2
from . import config
from . import config_temp


class Database():
    # rename config_temp to config
    settings = config.get_config()
    def __init__(self):
        # use config_temp connection values to establish a connection
        self.connection = psycopg2.connect(host=self.settings["host"],
                                            dbname=self.settings["dbname"],
                                            user=self.settings["user"],
                                            password=self.settings["passwd"])

        self.cursor = self.connection.cursor()
    
    # def __enter__(self):
    #     try:
    #         # use config_temp connection values to establish a connection
    #         self.connection = psycopg2._connect(host=self.settings["host"],
    #                                             dbname=self.settings["dbname"],
    #                                             user=self.settings["user"],
    #                                             password=self.settings["passwd"])

    #         self.cursor = self.connection.cursor()
    #     except psycopg2.DatabaseError as exception:
    #         print(exception)


    def query_handler(self, query):
        cursor = self.cursor
        cursor.execute(query)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':
    db = Database()
    q = "SELECT * FROM applicants"
    print(db.query_handler(q))