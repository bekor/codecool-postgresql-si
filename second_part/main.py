from flask import Flask, render_template, request, redirect
import os
from database_manager import query_handler
# from importlib.machinery import SourceFileLoader
# current_file_path = os.path.dirname(os.path.abspath(__file__))
# # query_handler
# query_handler = SourceFileLoader("query_handler", current_file_path + "/database_manager/query_handler.py").load_module()

# serving as multiplexer

app = Flask(__name__)


@app.route("/")
def index():
    """ Show index page with function buttons
    """
    return render_template("index.html")


@app.route("/mentors")
def mentors_and_schools():
    datas = query_handler.sql_mentors_schools()
    return render_template('index.html', datas=datas)


@app.route("/all-school")
def all_school():
    datas = query_handler.sql_all_school()
    return render_template('index.html', datas=datas)


@app.route("/mentors-by-country")
def mentors_by_country():
    datas = query_handler.sql_mentors_by_country()
    return render_template('index.html', datas=datas)


@app.route("/contacts")
def contacts():
    datas = query_handler.sql_contacts()
    return render_template('index.html', datas=datas)

# On this page you should show the result of a query that
#  returns the name of the school 
# plus the name of contact person at the school 
# (from the mentors table) ordered by the 
# name of the school
# columns: schools.name, mentors.first_name, mentors.last_name

# Applicants page [/applicants]
# On this page you should show the result of a query that returns the first name and the 
# code of the applicants plus the creation_date of the application (joining with the 
# applicants_mentors table) ordered by the creation_date in descending order
# BUT only for applications later than 2016-01-01
# columns: applicants.first_name, applicants.application_code, 
# applicants_mentors.creation_date

# Applicants and mentors page [/applicants-and-mentors]
# On this page you should show the result of a query that returns the first name and 
# the code of the applicants plus the name of the assigned mentor (joining through the 
# applicants_mentors table) ordered by the applicants id column
# Show all the applicants, even if they have no assigned mentor in the database!
# In this case use the string 'None' instead of the mentor name
# columns: applicants.first_name, applicants.application_code, mentor_first_name, 
# mentor_last_name

if __name__ == '__main__':
    app.run(debug=True)