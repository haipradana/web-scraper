from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = 'https://www.tokopedia.com/gugellaptop/review'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(4)
soup = BeautifulSoup(driver.page_source, 'html.parser')
containers = soup.find_all('article', attrs={'class': 'css-1pr2lii'})

for container in containers:
    review_element = container.find('span', attrs = {'data-testid': 'lblItemUlasan'})
    if review_element:
        review_text = review_element.text
        print(review_text)