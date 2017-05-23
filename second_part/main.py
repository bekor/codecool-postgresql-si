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


@app.route("/applicants")
def applicants_properties():
    datas = query_handler.sql_applicants_dates()
    return render_template('index.html', datas=datas)


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    datas = query_handler.sql_applicants_and_mentors()
    return render_template('index.html', datas=datas)


if __name__ == '__main__':
    app.run(debug=True)