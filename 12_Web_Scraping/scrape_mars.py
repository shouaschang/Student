# Import dependencies
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import tweepy

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    nasa_data = {}
    output = marsNews()
    nasa_data["mars_news"] = output[0]
    nasa_data["mars_paragraph"] = output[1]
    nasa_data["mars_image"] = marsImage()
    nasa_data["mars_weather"] = marsWeather()
    nasa_data["mars_facts"] = marsFacts()
    nasa_data["mars_hemisphere"] = marsHemisphere()

    return nasa_data

# Mars News
def marsNews():
    # NASA URL of page to be scraped
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(1)
    # Retrieving NASA page with the requests module
    response = requests.get(news_url)
    # HTML object
    html = browser.html
    # Create BeautifulSoup object; parsing with html.parser
    soup = bs(html, "html.parser")
    # Using Soup to find 'news_title' and 'news_p' tag
    article = soup.find("div", class_="list_text")
    news_title = soup.find("div", class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text
    output = [news_title, news_p]

    return output

# JPL Mars Images
def marsImage():
    # MARS Space image URL 
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    # HTML object
    html = browser.html
    # Creating soup object
    soup = bs(html, "html.parser")
    # Using soup to find .jpg image
    image = soup.find("img", class_="thumb")["src"]
    # Assigning url string
    featured_image_url = "https://www.jpl.nasa.gov" + image

    return featured_image_url

# Mars Weather
def marsWeather():
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)
    time.sleep(1)
    # HTML object
    mars_weather_html = browser.html
    # Soup object
    mars_weather_soup = bs(mars_weather_html, "html.parser")
    tweets = mars_weather_soup.find("ol", class_="stream-items")
    mars_weather = tweets.find("p", class_="tweet-text").text

    return mars_weathers

# Mars Facts
def marsFacts():
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    mars_data = pd.read_html(facts_url)
    mars_data = pd.DataFrame(mars_data[0])
    mars_data.columns = ["Description", "Value"]
    mars_data = mars_data.set_index("Description")
    mars_facts = mars_data.to_html(header = False, index = False)

    return mars_facts

# Mars Hemisphere
def marsHemisphere():
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)
    # HTML object
    html = browser.html
    # Soup object
    soup = bs(html, "html.parser")
    # List
    hemisphere_image_url = []
    products = soup.find("div", class_="result-list")
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        dictionary = {"title": title, "img_url": image_url}
        mars_hemisphere.append(dictionary)

        return mars_hemisphere
