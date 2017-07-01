from bs4 import BeautifulSoup
import requests
url = "http://see.ntc.net.np/score.php"

symbolnum = 99999
for all in range(10) : #Upto 10 consecutives.
	form_data = {
		'symbol' : "0"+str(symbolnum),
		'Submit' : 'Submit'
	}
	post = requests.post(url,data=form_data)
	soup = BeautifulSoup(post.content, 'html.parser')
	result = soup.find(id="show-result").find("h3").get_text()+"\n"
	result += soup.find(id="show-result").find("h2").get_text()
	print(result)
	symbolnum = symbolnum + 1
