from flask import Flask, jsonify
import requests
import json

from flask.templating import render_template
from werkzeug.wrappers import response

app = Flask(__name__)

@app.route('/')
def index():
    return "Please enter subject code after slash"

@app.route("/<username>")
def papers(username):
    import selenium
    import time
    from selenium import webdriver
    #OPTIONAL PACKAGE, BUY MAYBE NEEDED
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options

    #THIS INITIALIZES THE DRIVER (AKA THE WEB BROWSER)
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install())

    #THIS PRETTY MUCH TELLS THE WEB BROWSER WHICH WEBSITE TO GO TO
    driver.get(f'https://socialblade.com/tiktok/user/{username}')

    followers = driver.find_element_by_xpath('//*[@id="YouTubeUserTopInfoBlock"]/div[3]/span[2]').text
    uploads = driver.find_element_by_xpath('//*[@id="YouTubeUserTopInfoBlock"]/div[2]/span[2]').text
    followers_rank = driver.find_element_by_xpath('//*[@id="socialblade-user-content"]/div[1]/div[2]/div[1]/div[1]/p').text
    details = {
        "Username": username,
        "Live Followers": followers,
        "Upload": uploads,
        "Followers Rank": followers_rank
    }

    return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True)