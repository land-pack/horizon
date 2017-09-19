# -*- coding:utf-8 -*-
from datetime import datetime
from datetime import timedelta
from datetime import date
from flask import render_template, request, redirect, url_for
from app import app

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
