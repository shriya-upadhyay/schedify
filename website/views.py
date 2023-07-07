import os
import openai
from config import OPENAI_API_KEY
from flask import Blueprint, render_template, redirect, url_for, request
from gpt import ask_gpt 


views = Blueprint('views', __name__)



@views.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        wake_up_time = request.form["wake_up_time"]
        sleep_time = request.form["sleep_time"]
        task1 = request.form['task1']
        task1_time = request.form['time_task1']
        s = ask_gpt("Wake Up time: " + wake_up_time + " Sleep Time: " + sleep_time + " Task 1: " + task1 + " for " + task1_time + " minutes. ") 
        return render_template("sched.html", schedule = s, text = "This is your schedule:")
    return render_template("home.html")

@views.route('/sched/<schedule>')
def sched(schedule):
    return render_template("sched.html", schedule = schedule, text = "This is your schedule:")



