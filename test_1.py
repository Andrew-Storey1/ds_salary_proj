"""
@author: Andrew
"""

import pandas as pd
import soup_scraper as ss

df = pd.DataFrame({'Title': title, 'Salary': salary, 'Location': location })

df.to_csv('indeed_jobs.csv', index = False)

