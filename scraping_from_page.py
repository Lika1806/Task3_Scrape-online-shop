from bs4 import BeautifulSoup
from my_requests import get_text
import pandas as pd


def scrape(text):
	soup = BeautifulSoup(text, 'lxml')
	items = soup.find_all('div', class_="card-body")
	all_info = [None]*len(items)
	for i,item in enumerate(items):
		name = item.find('a').text
		price = item.find('h4', class_='float-end price card-title pull-right').text
		pars = item.find_all('p')
		description = pars[0].text
		review_count = pars[1].text.split()[0]
		rating = pars[2]['data-rating']
		all_info[i] = [name, price, description, review_count, rating]

	new_df = pd.DataFrame(all_info, columns = ['title', 'price', 'description', 'raview_count', 'rating'])
	return new_df
	
	
if __name__ == '__main__':
	url  = 'https://webscraper.io/test-sites/e-commerce/allinone'
	new_df = scrape(get_text(url))
	new_df.to_csv('top_item_list.txt',index=False)
