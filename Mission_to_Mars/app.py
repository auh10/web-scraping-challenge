#libraries
from flask import Flask, render_template, redirect
from flask_pymongo import flask_pymongo
import scrape_mars

#create an instance of Flask app
app = Flask(__name__)
#use pymongo to establish mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
#create a route rendering index.html template using data from Mongo
@app.route("/")
def home():
    #find record of data from mongo database
    mars_data = mongo.db.collection.find_one()
    #return template and data
    return render_template("index.html", mars=mars_data)

#create route that will scrape
@app.route("/scrape")
def scrape():
    #run scrape function
    mars = 

if __name__ == "__main__":
    app.run()
