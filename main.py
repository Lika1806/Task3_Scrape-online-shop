from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from scraping_from_page import scrape

base_url = 'https://webscraper.io/test-sites/e-commerce/allinone'
final_df = pd.DataFrame()

def creat_df(source,category):
    '''Creates dataframe from items found in source page, and return it'''
    df = scrape(source)
    category = [s.strip() for s in category.split('/')]
    df['category'] = category[0]
    df['type'] = category[1]
    return df

driver = webdriver.Chrome()
driver.get(base_url)

all_menu_items = driver.find_element(By.ID, 'side-menu').find_elements(By.CLASS_NAME, 'nav-item')

for item in all_menu_items[1:]: #excluding Home page
    item.click()
    new_items = driver.find_element(By.CSS_SELECTOR, '[class*="sidebar"]').find_element(By.CSS_SELECTOR, '[class*="active"]').find_elements(By.CLASS_NAME, 'nav-item')
    for new_item in new_items:
        new_item.click()
        category = driver.find_element(By.CLASS_NAME, 'page-header').text
        new_df = creat_df(driver.page_source, category)
        final_df = pd.concat([final_df, new_df], ignore_index = True)
        driver.back()
    driver.back()

driver.quit()


new_column_order = ['category', 'type'] + list(final_df.columns[:-2]) #changing column order
final_df = final_df[new_column_order]

final_df = final_df.set_index(['category','type']) #reindexing dataframe

final_df.to_csv('complete_item_list.txt') #saving dataframe to csv file