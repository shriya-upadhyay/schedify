import os
import openai
from config import OPENAI_API_KEY
from flask import Blueprint, render_template, redirect, url_for, request
from gpt import ask_gpt 


views = Blueprint('views', __name__)

tasks = {}

@views.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':

        if 'taskName' in request.form and 'allottedTime' in request.form:
            task_name = request.form['taskName']
            allotted_time = request.form['allottedTime']
            tasks[task_name] = allotted_time

        else:
            wake_up_time = request.form["wake_up_time"]
            sleep_time = request.form["sleep_time"]
            s = ask_gpt("Wake Up time: " + wake_up_time + " Sleep Time: " + sleep_time + " Tasks: " + str(tasks.keys()) + " for " + str(tasks.values()) + " minutes. ") 
            print(s)
            tasks.clear()
            return render_template("sched.html", schedule = s, text = "This is your schedule:")


        
        print (tasks.items())
    return render_template("home.html")

@views.route('/sched/<schedule>')
def sched(schedule):
    return render_template("sched.html", schedule = schedule, text = "This is your schedule:")



