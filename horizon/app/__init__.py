from flask import Flask, render_template, request, redirect, url_for
from flask.ext.wtf import Form
from wtforms import SubmitField, SelectField, DateField
from flask.ext.admin.form.widgets import DatePickerWidget
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

"""
If you are wondering why the import statement is at the end and not at 
the beginning of the script as it is always done, the reason is to avoid 
circular references, because you are going to see that the views module 
needs to import the app variable defined in this script. Putting the 
import at the end avoids the circular import error.
"""
# fcc_ as finance project
from app import main_views, user_views

# pcc_ as product project

# icc_ as inside project
