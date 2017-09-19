# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, url_for
from app import app

@app.route("/user/from", methods=['GET', 'POST'])
def user_from():
    return render_template("user/from.html")


@app.route("/user/alive", methods=['GET', 'POST'])
def user_alive():
    return render_template("user/alive.html")