import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

SITE_URL = os.getenv("SITE_URL") #site you want to scrape
GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")

response=requests.get(SITE_URL).text

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_URL)

beautifulSoup=BeautifulSoup(response,'html.parser')

address=beautifulSoup.find_all(name='address')
address_list=[address_.get_text().strip() for address_ in address]

all_price=beautifulSoup.find_all(name='span',class_='PropertyCardWrapper__StyledPriceLine')
price_list=[price.get_text().split('+')[0].split('/')[0] for price in all_price]

link=beautifulSoup.find_all(name='a',class_='StyledPropertyCardDataArea-anchor')
link_list=[links.get('href') for links in link]

length=len(address)

time.sleep(2)
for i in range(length):
    time.sleep(1.5)
    input_boxes = driver.find_elements(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')
    submit_button=driver.find_element(By.CLASS_NAME,value='Y5sE8d')
    input_boxes[0].send_keys(address_list[i])
    input_boxes[1].send_keys(price_list[i])
    input_boxes[2].send_keys(link_list[i])
    time.sleep(0.5)
    submit_button.click()
    time.sleep(1.5)
    if i==(length-1):
        driver.quit() 
        break

    another_response=driver.find_element(By.LINK_TEXT,value='Submit another response')
    another_response.click()
