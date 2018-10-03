from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame
url = 'http://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2013-14-legislative-session.html'
# Request content from web page
result = requests.get(url)
c = result.content
# Set as Beautiful Soup Object
soup = BeautifulSoup(c)
# Go to the section of interest
summary = soup.find("div",{'class':'list-land','id':'content'})

# Find the tables in the HTML
tables = summary.find_all('table')
# Set up empty data list
data = []

# Set rows as first indexed object in tables with a row
rows = tables[0].findAll('tr')

# now grab every HTML cell in every row
for tr in rows:
    cols = tr.findAll('td')
    # Check to see if text is in the row
    for td in cols:
        text = td.find(text=True) 
        print text,
        data.append(text)
 data
 # Set up empty lists
reports = []
date = []

# Se tindex counter
index = 0

# Go find the pdf cells
for item in data:
    if 'pdf' in item:
        # Add the date and reports
        date.append(data[index-1])
        
        # Get rid of \xa0
        reports.append(item.replace(u'\xa0', u' '))
                    
    index += 1
 # Set up Dates and Reports as Series
date = Series(date)
reports = Series(reports)
# Concatenate into a DataFrame
legislative_df = pd.concat([date,reports],axis=1)
# Set up the columns
legislative_df.columns = ['Date','Reports']
# Show the finished DataFrame
legislative_df
