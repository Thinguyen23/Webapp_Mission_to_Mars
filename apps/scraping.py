from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape_all():
    import datetime as dt
    # Initiate headless driver for deployment
    
    #Windows Code:
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        'ceberus': hemispheres(browser)[0],
        'schiaparelli': hemispheres(browser)[1],
        'syrtis_major': hemispheres(browser)[2],
        'valles_marineris': hemispheres(browser)[3]
    }
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')

    # Find the relative image url
    try:
        # find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    return img_url

def mars_facts():

    import pandas as pd  
    try:
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    return df.to_html()

def hemispheres(browser):
    # Create function to scrape hemispheres titles and images
    def scrape_img(url):
        browser.visit(url)
        html = browser.html
        img_soup = BeautifulSoup(html, 'html.parser')
        #hemisphere_data ={}
        try:
        #   title = img_soup.select('h2')[0].get_text()
            img_url_rel = img_soup.select('div div div img')[2].get('src')  
        except AttributeError:
            return None
        img_url = f'https://astrogeology.usgs.gov/{img_url_rel}'
        #hemisphere_data = {img_url:title}
        return img_url
    # Hemisphere url:
    url1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    url2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    url3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    url4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    # Create list  to hold hemispheres' dictionaries
    hemis =[]
    hemis.append(scrape_img(url1))
    hemis.append(scrape_img(url2))
    hemis.append(scrape_img(url3))
    hemis.append(scrape_img(url4))
    return hemis

#data= scrape_all()
#print(data['ceberus'])
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())