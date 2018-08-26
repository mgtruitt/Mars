
# coding: utf-8

# In[1]:


#!pip install chromedriver


# In[2]:



import pandas as pd
import os
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser

#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)

# Declare the database
#db = client.Mars_Mission

# Declare the collection
#collection = db.Mars_Mission

# In[3]
def init_browser():
        executable_path = {"executable_path": "/Users/G/Anaconda3/Chromedriver-Windows"}
        return Browser("chrome", **executable_path, headless=False)

# In[4]:
def scrape():
    mars_scrape_data = {}

    response = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")


# In[5]:


    soup = bs(response.text, 'html.parser')
   

# In[6]:


    newstitles = soup.find(class_="content_title")
    news_titles = newstitles.text.strip()
    #news_titles


# In[7]:


    newsp = soup.find(class_="rollover_description_inner")
    news_p = newsp.text.strip()
    #news_p


# In[8]:

    browser = init_browser()
  
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    htmll = browser.html
    imsoup = bs(htmll, "html.parser")

   # In[10]:


    image = imsoup.find('img', class_= 'data-fancybox-href')   
    imagee = imsoup.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
    #imagee 


# In[11]:


    featured_image_url = "https://www.jpl.nasa.gov"+imagee
    featured_image_url


# In[12]:



    twitter = requests.get("https://twitter.com/marswxreport?lang=en")
    s_twitter = bs(twitter.text, 'html.parser')
   


# In[14]:


    marsweather = s_twitter.find('p', class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather = marsweather.text.strip()
    #mars_weather


# In[15]:


   # browser = init_browser()
    browser.visit("https://space-facts.com/mars/")
    facts = browser.html
    marsfacts = bs(html, 'html.parser')


# In[16]:


    facts_url = "https://space-facts.com/mars/"
    facts_pd = pd.read_html(facts_url)
    facts_df = pd.DataFrame(facts_pd[0])
    facts_df.columns = ["Fact Description", "Fact Data"]
    facts_df.set_index(["Fact Description", "Fact Data"])


# In[17]:


    df_variable = facts_df.set_index(["Fact Description", "Fact Data"])
    df_html = "".join(df_variable.to_html().split())

    #df_html


# In[18]:


    #browser = init_browser()
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    cerberus_html = browser.html
    cer_soup = bs(cerberus_html, "html.parser")
    #print(cer_soup.prettify())
#

    


# In[23]:


    cer_img = cer_soup.find('div', 'downloads').a['href']
    cer_title = cer_soup.find('h2', class_= 'title')
    title_cer = cer_title.text.strip()
    #print(cer_img)
    #print(title_cer)


# In[32]:


    #browser = init_browser()
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced")
    schiaparelli_html = browser.html
    sch_soup = bs(schiaparelli_html, "html.parser")


# In[26]:


    sch_img = sch_soup.find('div', 'downloads').a['href']
    sch_title = sch_soup.find('h2', class_= 'title')
    title_sch = sch_title.text.strip()
    #print(sch_img)
    #print(title_sch)


# In[28]:


    #browser = init_browser()
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced")
    syrtis_html = browser.html
    syr_soup = bs(syrtis_html, "html.parser")


# In[29]:


    syr_img = syr_soup.find('div', 'downloads').a['href']
    syr_title = syr_soup.find('h2', class_= 'title')
    title_syr = syr_title.text.strip()
    #print(syr_img)
    #print(title_syr)


# In[30]:


    #browser = init_browser()
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced")
    valles_html = browser.html
    val_soup = bs(valles_html, "html.parser")


# In[31]:


    val_img = val_soup.find('div', 'downloads').a['href']
    val_title = val_soup.find('h2', class_= 'title')
    title_val = val_title.text.strip()
    #print(val_img)
    #print(title_val)


# In[34]:


    Hemisphere_Dictionary = []
    Cerberus_Hemisphere = {"img_url": cer_img, "title": title_cer} 
    Schiaparelli_Hemisphere = {"img_url": sch_img, "title": title_sch}
    Syrtis_Hemisphere = {"img_url": syr_img, "title": title_syr} 
    Valles_Hemisphere = {"img_url": val_img, "title": title_val} 
    Hemisphere_Dictionary.append(Cerberus_Hemisphere)
    Hemisphere_Dictionary.append(Schiaparelli_Hemisphere) 
    Hemisphere_Dictionary.append(Syrtis_Hemisphere) 
    Hemisphere_Dictionary.append(Valles_Hemisphere)
    
# In[35]:
    mars_scrape_data["Hemisphere_Dictionary"] = Hemisphere_Dictionary
    mars_scrape_data["news_titles"] = news_titles
    mars_scrape_data["news_p"] = news_p
    mars_scrape_data["featured_image_url"] = featured_image_url
    mars_scrape_data["mars_weather"] = mars_weather
    mars_scrape_data["df_html"] = df_html

    #mars_scrape_data =[]
    #mars_scrape_data.append(Hemisphere_Dictionary)
    #mars_scrape_data.append(news_titles)
    #mars_scrape_data.append(news_p)
    #mars_scrape_data.append(featured_image_url)
    #mars_scrape_data.append(mars_weather)
    #mars_scrape_data
    return mars_scrape_data

#scrape()
