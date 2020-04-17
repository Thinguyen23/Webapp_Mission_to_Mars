# :full_moon: Mission to Mars :full_moon:
In this project, I built a Python Flask app that automatically collects data from online webpages and store the data scraped in a non-relational database for further use and analysis. The data is then display on a dynamic website. Users interact with page by pressing button to update data. 
As the title of this project, I collect data on Mars from [NASA website](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) 
## Getting Started
Web scraping bot is a time-saver. But there will be several tools you need to install in order to get the app up and running.

### Prerequisites

These are the list of tools you need
1. **Splinter**<br>
Splinter automates web browser. To install, run the command `pip install splinter` 
2. **ChromeDriver**<br> 
Visit the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) webpage to install ChromeDriver. Make sure the version matches your Chrome version.
3. **BeautifulSoup**<br>
BeautifulSoup is a Python library for pull data out of HTML and XML. To install, run the command `pip install bs4`
4. **MongoDB**<br>
MongoDB is a NoSQL database that stores unstructured data in the form of Binary JavaScript Object Notation (JSON), or BSON. It is a fast and efficient way to store tables, documents or images...<br>
First, install PyMongo by running `pip install pymongo`. PyMongo is a tool that allows developers to use Python with Mongo<br>
Second, install Mongo to your computer, follow the instructions on [MongoDB official documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) for Windows users.<br>
For macOS computers, follow instructions in [MongoDB official documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/).
* Add a data directory to root by first navigating to root directory. Then make a directory with command `mkdir -p data/db`. This is the default location for Mongo's databases.
* Add MongoDb's Path to PATH environment variables so that you can run and launch MongoDB from the Bash command line. Path will look like this `C:\\Program Files\\MongoDB\\Server\\\\bin`

#### Test MongoDB

To test if you have sucessfully installed MongoDB, reopen a Git Bash window and run `mongod`. If Mongo continues to run in the terminal, it’s been successfully installed—great job!

If `mongod` didn’t run and instead, your Bash threw a `command not found` error, make sure you added MongoDB’s bin directory to your PATH variable.

If mongod starts but closes after a series of prompts, make sure you created the /data/db directory in your root. MongoDB cannot run without this directory.

## Web Inspector
Inspect the Nasa webpage structure to get an idea what data needed to be collected. Open the page inspector and identify the piece of information needed to be collected. In this case, I chose to collect the article headlines.
<p align="center">
   <img scr="https://github.com/Thinguyen23/Thi_Mission_to_Mars/blob/master/apps/images/rawpage.png" width=35%>
</p>
 
## Automate Web Browser and Perform Web Scrape
```
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup

# Set the executable path and initialize the chrome browser in splinter
executable_path = {‘executable_path’: ‘chromedriver’}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional: tell browser to wait for a second before searching for components
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Set up HTML parser
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
```
Visit [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and start web scraping!
For this project, I scrape an update image of Mission to Mars project, recent news article summary and an HTML table on Mars facts. 
## Store the data
As mentioned, MongoDB is a non-relational database. A Mongo Database contains collections. These collections contain documents, and each document contains fields where the data is stored. Mongo and SQL handle documents differently in terms of storage and how user interact with the database.
1. To get started, open a new terminal window and activate the proper working environment
2. To start an instance, type `mongod` into the first line of the terminal and press enter. This tab need to stay open and activate so that the Mongo instance continues to run.
3. Open another terimnal window and type `mongo`. A Mongo instance has been created.
4. Create a database by typing `use mars_app` to creates a new database named "mars_app"
## Web app
The app is hosted in [app.py file](https://github.com/Thinguyen23/Thi_Mission_to_Mars/blob/master/apps/app.py).<br>
Flask is a web microframework that allows developers to build a web application using python. 
1. First, import tools and set tup Flask
```
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping # scraping.py which hosts the scraping process

app = Flask(__name__)
```
2. Second, set up database connection
```
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
```
3. Third, set up App routes
```
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"
```
4. Final code: tell Flask to run
```
if __name__ == "__main__":
  app.run()
 ```
## Customize Apearance with HTML and CSS
 
A shot of final Scraping Website:<br><br>
<p align="center">
   <img scr="https://github.com/Thinguyen23/Thi_Mission_to_Mars/blob/master/apps/images/rawpage.png" width=75%>
</p>
                                                                                                           
## Tools used
- Chrome Developer Tools to identify HTML components
- BeautifulSoup, Splinter and ChromeDriver to automate the scrape
- MongoDB to store data
- Flask to display
## Authors
* **Thi Nguyen** - [Thinguyen23](https://github.com/Thinguyen23)
## Copyright
© 2019 Trilogy Education Services. All Rights Reserved.

