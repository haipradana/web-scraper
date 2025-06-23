from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = 'https://www.tokopedia.com/gugellaptop/review'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

reviews_data = []
for i in range(0, 10):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    containers = soup.find_all('article', attrs={'class': 'css-1pr2lii'})

    for container in containers:
        try:
            product_element = container.find('p', attrs={
                'data-unify': 'Typography',
                'class': 'css-akhxpb-unf-heading e1qvo2ff8'
            })
            review_element = container.find('span', attrs={'data-testid': 'lblItemUlasan'})
                
            if review_element:
                product_name = product_element.get_text(strip=True) if product_element else None
                review_text = review_element.get_text(strip=True)

            reviews_data.append({
                'product_name': product_name,
                'review': review_text
            })

        except AttributeError:
            continue

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Laman berikutnya']").click()
    time.sleep(3)

# print(product_names)
# print(review_data)
df = pd.DataFrame(reviews_data)

df.to_csv('tokopedia-seller-review/data/review_gugellaptop.csv', index=False)