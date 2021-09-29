from flask import Flask, jsonify
import requests
import json
from bs4 import BeautifulSoup

from flask.templating import render_template
from werkzeug.wrappers import response

app = Flask(__name__)

@app.route('/')
def index():
    return "Please enter subject code after slash"

@app.route("/<username>")
def papers(username):
    url = f'https://tokcount.com/'
    r = requests.get(url)
    html = r.content

    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify)
    print(soup.find_all(class_="odometer-inside"))

    
    details = {
        "Username": username,
        "Live Followers": "",
        "Upload": "",
        "Followers Rank": ""
    }

    return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True)