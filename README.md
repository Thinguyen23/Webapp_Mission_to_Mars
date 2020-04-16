# :full_moon: Mission to Mars :full_moon:
In this project, I built a Python Flask app that automatically collects data from online webpages and store the data scraped in a non-relational database for further use and analysis. The data is then display on a dynamic website. Users interact with page by pressing button to update data. 
As the title of this project, I scraped data from [NASA news on Mars website](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) 
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
MongoDB is a NoSQL database that stores unstructured data in the form of JSON. It is a fast and efficient way to store tables, documents or images...<br>
First, install PyMongo by running `pip install pymongo`. PyMongo is a tool that allows developers to use Python with Mongo<br>
Second, install Mongo to your computer, follow the instructions on [MongoDB official documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) for Windows users.<br>
For macOS computers, follow instructions in [MongoDB official documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/).
* Add a data directory to root by first navigating to root directory. Then make a directory with command `mkdir -p data/db`. This is the default location for Mongo's databases.
* Add MongoDb's Path to PATH environment variables so that you can run and launch MongoDB from the Bash command line. Path will look like this `C:\\Program Files\\MongoDB\\Server\\\\bin`

### Running the tests

To test if you have sucessfully installed MongoDB, reopen a Git Bash window and run `mongod`. If Mongo continues to run in the terminal, it’s been successfully installed—great job!

If `mongod` didn’t run and instead, your Bash threw a “command not found” error, make sure you added MongoDB’s bin directory to your PATH variable.

If mongod starts but closes after a series of prompts, make sure you created the /data/db directory in your root. MongoDB cannot run without this directory.

## Web Inspector
Inspect the website to get an idea what piece of data needed to be collected. In this case, I chose to collect the article headlines.
## Automate Web Browser and Perform Web Scrape



```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Data extraction
The web scraping process is automated using programming script. By using automated web scraping, companies can gather information from different sources in seconds.
Define web page structure
Writing Python script with Splinter and BeautifulSoup
Store data using MongoDB (noSQL database, messy data, data that does not have any relationship to any data, using json data structure, fast and efficient, relate to task we are using, 
build a web app using flask (button to execute scraping code and update the data on the home page)
### MongoDB



Final Scraping Website:


![webpage](https://github.com/Thinguyen23/Thi_Mission_to_Mars/blob/master/apps/images/webpage.png)
## Tools used
- Use Chrome Developer Tools to identify HTML components
- Use BeautifulSoup, Splinter and ChromeDriver to automate the scrape
```
To install Splinter, run `pip install splinter`
To install BeautifulSoup, run `pip install bs4`
```
- Use Mongo to store data
- Use flask to display


## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Authors

* **Thi Nguyen** - [ThiNguyen23](https://github.com/Thinguyen23)

