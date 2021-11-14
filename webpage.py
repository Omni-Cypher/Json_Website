import os.path
import urllib.request
import json
import cgi

import jinja2

import templates as templates
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template, redirect, url_for, request

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as url:
    users = json.loads(url.read().decode())

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as url:
    userPosts = json.loads(url.read().decode())


app = Flask(__name__)
app.config['Debug'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


@app.route('/')
@app.route('/home')
def home():
    return render_template('source.html', title="Json", users=users)


@app.route('/', methods=['POST'])
def posts():
    userId = request.form['userId']
    userName = request.form['userName']
    return render_template('source.html', title="Json", users=users, userPosts=userPosts, userId=userId,
                           userName=userName)


if __name__ == '__main__':
    app.run(debug=True)
