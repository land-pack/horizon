# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, url_for
from app import app

@app.route("/user/from", methods=['GET', 'POST'])
def user_from():
    return render_template("user/from.html")


@app.route("/user/alive", methods=['GET', 'POST'])
def user_alive():
    return render_template("user/alive.html")


@app.route("/user/info", methods=['GET', 'POST'])
def user_info():
    return render_template("user/info.html")


@app.route("/user/week", methods=['GET', 'POST'])
def user_week():
    return render_template("user/week.html")


@app.route("/user/lost", methods=['GET', 'POST'])
def user_lost():
	# no login aleast 30 days
    return render_template("user/lost.html")


# ===dark
@app.route("/dark/sumary", methods=['GET', 'POST'])
def user_sumary():
	# no login aleast 30 days
    return render_template("dark/sumary.html")