"""Angelo Barcelona SDEV 300, lab6"""
import datetime as dt
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    """returns home page login screen"""
    return render_template("login.html")


@app.route('/', methods=["POST"])
def check_login():
    """checks login"""
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def new_user():
    """returns registration template"""


@app.route('/index')
def hello_world():
    """returns the template for the initial home page index"""
    return render_template("index.html", systems=get_systems_fought(), date_time=dt.datetime.now())


@app.route('/members')
def get_members():
    """returns the template HTML page for RnK Membership"""
    return render_template("rnkmembers.html", members=get_member_list(), table_data=get_table_data())


@app.route('/image')
def get_image():
    """returns the HTML page for the RnK Image"""
    return render_template("rnkimage.html")


def get_member_list():
    """defines the member list that is passed in to the HTML page - rnkmembers.html"""
    members = ["Skrubs", "Lord Maldoror", "Agent Xer0", "Mesh",
               "Elderath", "Trident", "Princess Arcia"]
    members.sort()
    return members


def get_systems_fought():
    """defines the list of regions rooks and kings have conquered in EVE"""
    systems = ["PROVIDENCE", "FOUNTAIN", "GREAT WILDLANDS", "COBALT'S EDGE", "CLOUD RING", "FADE",
               "STAIN", "SCALDING PASS"]
    return systems


def get_table_data():
    """produces data for our members table"""
    table_d = [['Name', 'Position', 'Ship'],
               ['Lord Maldoror', 'CEO', 'Navy Apoc'],
               ['Skrubs', 'Core Member', 'Archon'],
               ['Agent Xer0', 'Core Member', 'Archon'],
               ['Mesh', 'Director', 'Navy Apoc'],
               ['Elderath', 'Core Member', 'Navy Apoc'],
               ['Trident', 'Core Member', 'Navy Apoc'],
               ['Princess Arcia', 'Core Member', 'Navy Apoc']]
    return table_d


get_member_list()
get_systems_fought()
get_table_data()

if __name__ == '__main__':
    app.run(debug=True)
