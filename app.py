from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_scrape_data = mongo.db.mars_scrape_data.find_one()
    return render_template("index.html", mars_scrape_data=mars_scrape_data)


@app.route("/scrape")
def scrape():
    mars_scrape_data = mongo.db.mars_scrape_data
    mars_scrape = scrape_mars.scrape()
    mars_scrape_data.update({}, mars_scrape, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)