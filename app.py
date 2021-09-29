from flask import Flask, jsonify
import requests
import json

from flask.templating import render_template
from werkzeug.wrappers import response

app = Flask(__name__)

@app.route('/')
def index():
    return "Please enter username after slash"

@app.route("/<username>")
def papers(username):
    import selenium
    import time
    from selenium import webdriver
    #OPTIONAL PACKAGE, BUY MAYBE NEEDED
    from webdriver_manager.chrome import ChromeDriverManager

    #THIS INITIALIZES THE DRIVER (AKA THE WEB BROWSER)
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    #THIS PRETTY MUCH TELLS THE WEB BROWSER WHICH WEBSITE TO GO TO
    driver.get(f'https://tokcounter.com/?user={username}')

    #THIS IS THE IMPORTANT PART SO I'LL BREAK IT DOWN IN A COUPLE DIFFERENT PARTS LOL

    #THIS 'TEXT' PORTION         |       THIS PORTION WILL TAKE THE ELEMENT THAT
    #PRETTY MUCH STORES THE      |       WE WANT FROM THE WEBSITE, THE .TEXT WILL
    #WEBSITE DATA THAT WE WANT   |       SAVE THE INFORMATION AS A TEXT DOCUMENT
    #IN THIS VARIABLE
    # time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/button').click()
    time.sleep(10)
    FOLLOWERS = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[4]/div[1]/div').text

    #PRINTS OUT THE DATA PULLED FROM ABOVE
    a=FOLLOWERS.split('\n')
    followers="".join(a)
    
    details = {
        "Username": username,
        "Live Followers": followers,
        # "Upload": uploads,
        # "Followers Rank": followers_rank
    }

    return jsonify(details)

if __name__ == '__main__':
    app.run(debug=True)