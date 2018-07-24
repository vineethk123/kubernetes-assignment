from flask import Flask, request, render_template
import os

app = Flask("read_message")

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/", methods=["POST"])
def post_form():
    text = request.form["text"]
    path = 'messages/messages.txt'
    if os.path.exists(path):
        f = open(path, 'a')
    else:
        f = open(path, 'w')

    f.write(text + '.' + '\n')
    f.close()
    return "Thanks for submitting!"

@app.route("/display")
def displayMessages1():
    if os.path.exists('messages/messages.txt'):
        return open('messages/messages.txt').read()
    else:
        return "No Messages Yet"

app.run('0.0.0.0', port=5000)
