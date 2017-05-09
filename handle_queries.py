"""
Mentors table: Id, First_name, Last_name, Nick_name, Phone_number, Email, City, favourite_number
Applicants table: Id, First_name, Last_name, Phone_number, email, Application_code 
"""

from connect import connect_to_sql
import ui
import main


@connect_to_sql
def get_names_from_table(cursor):
    cursor.execute("SELECT first_name, last_name FROM {};".format("mentors"))
    # Fetch and print the result of the last execution
    full_names = cursor.fetchall()
    ui.print_table(full_names)
    pass


@connect_to_sql
def get_nicnames_from_miskolc(cursor):
    cursor.execute("SELECT nick_name FROM mentors WHERE city='Miskolc';")
    nick_names = cursor.fetchall()
    ui.print_table(nick_names)
    pass


@connect_to_sql
def get_name_and_phone_by_firstname(cursor):
    cursor.execute("SELECT CONCAT(first_name, ' ', last_name) As full_name \
                    FROM applicants WHERE first_name='Carol';")
    full_name = cursor.fetchall()
    cursor.execute("SELECT phone_number FROM applicants WHERE first_name='Carol';")
    phone = cursor.fetchall()
    applicant = full_name + phone
    applicant = " ".join("%s" % t for t in applicant)
    ui.print_result(applicant, "applicant first name is Carol: ")
    pass


@connect_to_sql
def get_name_and_phone_by_email(cursor):
    cursor.execute("SELECT CONCAT(first_name, ' ', last_name) As full_name \
                    FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';")
    full_name = cursor.fetchall()
    cursor.execute("SELECT phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';")
    phone = cursor.fetchall()
    applicant = full_name[0] + phone[0]
    applicant = " ".join("%s" % t for t in applicant)
    ui.print_result(applicant, "adipiscingenimmi.edu people's name and phone: ")
    pass


@connect_to_sql
def insert_data(cursor):
    cursor.execute("INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) \
                    VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);")
    pass


@connect_to_sql
def get_applicant_by_code(cursor):
    cursor.execute("SELECT * FROM applicants WHERE application_code='54823';")
    applicant = cursor.fetchall()
    ui.print_table(applicant)
    pass


@connect_to_sql
def update_data(cursor):
    sql_query = "UPDATE applicants SET phone_number= (%s) WHERE first_name='Jemima' AND last_name='Foreman';"
    data = ('003670/223-7459',)
    cursor.execute(sql_query, data)
    pass


@connect_to_sql
def get_applicant_by_name(cursor):
    cursor.execute("SELECT * FROM applicants WHERE first_name='Jemima' AND last_name='Foreman';")
    applicant = cursor.fetchall()
    ui.print_table(applicant)
    pass


@connect_to_sql
def delete_applicant(cursor):
    cursor.execute("DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';")
    pass


@connect_to_sql
def all_applicants(cursor):
    cursor.execute("SELECT * FROM applicants;")
    full_table = cursor.fetchall()
    ui.print_table(full_table)
    pass


@connect_to_sql
def all_mentors(cursor):
    cursor.execute("SELECT * FROM mentors;")
    full_table = cursor.fetchall()
    ui.print_table(full_table)
    pass


def test_queries():
    get_names_from_table()
    get_nicnames_from_miskolc()
    get_name_and_phone_by_firstname()
    get_name_and_phone_by_email()
    #insert_data()
    get_applicant_by_code()
    #update_data()
    get_applicant_by_name()
    all_applicants()
    all_mentors()


if __name__ == '__main__':
    test_queries()