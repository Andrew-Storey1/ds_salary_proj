# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 06:45:13 2020

@author: Andre
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

url = 'https://www.glassdoor.co.uk/Salaries/london-data-scientist-salary-SRCH_IL.0,6_IM1035_KO7,21.htm'


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

soup_level2 = BeautifulSoup(driver.page_source, 'lxml')

datalist = []
x = 0 

table = soup_level2.find_all('table')[0]

df = pd.read_html(str(table),header=0)

datalist.append(df[0])

driver.quit()

result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)
