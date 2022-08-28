import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

star_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
request = requests.get(star_url)
print(request)

soup = BeautifulSoup(request.text, "html.parser")

star_table = soup.find("table")

temp_list = []
table_rows = star_table[7].find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_name = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp_list)):
    Star_name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

value = pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius)),columns= ['Star_name', 'Distance', 'Mass', 'Radius'])
print(value)

value.to_csv("Brown_dwarf_data.csv")