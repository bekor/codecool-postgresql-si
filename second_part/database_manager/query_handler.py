from database_manager.server_connection.database_connection import Database


def sql_mentors_schools():
    db = Database()
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
            FROM mentors
            LEFT OUTER JOIN schools
            ON mentors.city = schools.city
            ORDER BY mentors.id
            """
    return db.query_handler(query)


def sql_all_school():
    db = Database()
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
            FROM mentors
            RIGHT OUTER JOIN schools
            ON mentors.city = schools.city
            ORDER BY mentors.id
            """
    return db.query_handler(query)


def sql_mentors_by_country():
    db = Database()
    query = """SELECT schools.country, COUNT(mentors.id)
            FROM mentors
            INNER JOIN schools
            ON mentors.city = schools.city
            GROUP BY schools.country
            """
    return db.query_handler(query)
        

def test():
    db = Database()
    q = "SELECT * FROM mentors"
    return db.query_handler(q)

if __name__ == '__main__':
    test()