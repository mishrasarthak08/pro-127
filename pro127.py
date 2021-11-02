from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)
soup = BeautifulSoup(page.text,"html.parser")
startable = soup.find("table")
temp_list = []
tablerows = startable.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
distance = []
mass = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df = pd.DataFrame(list(zip(star_name,distance,mass,radius,lum)),columns = ["star_name","distance","mass","radius","lum"])
df.to_csv("brightstars.csv")