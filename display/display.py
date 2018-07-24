from flask import Flask
import requests
import os

app = Flask("display")

@app.route("/")
def display():
    if os.path.exists('messages/messages.txt'):
        return open('messages/messages.txt').read()
    else:
        return "No Messages Yet"


app.run("0.0.0.0", port=5010)
