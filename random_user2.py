from bs4 import BeautifulSoup
import requests
data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html'
data_scrapping = requests.get(data_url).text
soup=BeautifulSoup(data_url,'html.parser')

print(soup)