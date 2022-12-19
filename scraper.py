import requests 
from bs4 import BeautifulSoup
r = requests.get("https://www.songkick.com/artists/5686164-waterparks/calendar")
 
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_="component events-summary upcoming")

lines = s.find_all('strong')
# lines = s.find_all('strong class="primary-detail"')
for line in lines:
    print(line.text)