
"""
@author: Andrew
"""


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.indeed.co.uk/data-scientist-jobs-in-London,-Greater-London'
#url = 'https://https://www.indeed.co.uk/jobs?q=data+scientist&l=United+Kingdom'

html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
type(soup)


jobs = []

titles = soup.find_all('h2', {"class" : "title"})

locations = soup.find_all('span', {"class" : "location accessible-contrast-color-location"})

salaries = soup.find_all('span', {"class" : "salaryText"})


title = [span.get_text() for span in titles]
salary = [span.get_text() for span in salaries]
location = [span.get_text() for span in locations]

salary = pd.Series(salary)

title = pd.Series(title)

location = pd.Series(location) 
jobs = pd.DataFrame({'Title': title, 'Salary': salary, 'Location': location })

jobs.to_csv('DataFrame', index=False)