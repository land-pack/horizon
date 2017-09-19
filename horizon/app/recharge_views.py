# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, url_for
from app import app

@app.route("/recharge/step", methods=['GET', 'POST'])
def recharge_step():
    return render_template("recharge/step.html")



@app.route("/recharge/range", methods=['GET', 'POST'])
def recharge_range():
    return render_template("recharge/range.html")