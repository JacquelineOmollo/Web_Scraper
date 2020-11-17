from bs4 import BeautifulSoup
import requests

# This header tricks the website to seem like I am personally on the website searching
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

# The website page that's being scraped
web_data = "https://www.bulkcheapammo.com/handgun-ammo/9mm-luger"

site = requests.get(web_data, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')


round_title = soup.find("span", {"class": "round"}).get_text()


caliber = soup.findAll("div", {"class": "caliber-name"})


print(round_title, caliber)
# print(soup.prettify())

