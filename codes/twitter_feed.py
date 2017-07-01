from  bs4 import BeautifulSoup
import requests

page = requests.get("https://twitter.com/twitter")
soup = BeautifulSoup(page.content, 'html.parser')
all_items = soup.find_all(class_="content")

for x in range(len(all_items)):
	content = all_items[x]
	tweet_text = content.find(class_="js-tweet-text-container").get_text()
	print(x,tweet_text)
