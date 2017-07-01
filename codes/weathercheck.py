from  bs4 import BeautifulSoup
import requests

page = requests.get("http://www.accuweather.com/en/np/kathmandu/241809/current-weather/241809")
soup = BeautifulSoup(page.content, 'html.parser')
now_section = soup.find(id="detail-now")
now = now_section.find(class_="forecast")
temperature = now.find(class_="large-temp").get_text()
info = now.find(class_="cond").get_text()
print("Temperature :")
print(temperature)
print("\nCondition : ")
print(info)
