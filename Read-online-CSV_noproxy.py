from cgitb import text
import pandas as pd
import os
import io
import requests


## Data Input
url = 'http://www.edb.gov.hk/attachment/en/student-parents/sch-info/sch-search/sch-location-info/SCH_LOC_EDB.csv'
r = requests.get(url)
r.encoding = 'utf-16'  #encode for traditional chinese
df = pd.read_csv(io.StringIO(r.text))

## Data Manipulation
#Filter to get only "Central" data under column "District"
filteredarea = df[df["DISTRICT"].str.contains("CENTRAL")]  


## Final Result
#Print it out
print(filteredarea)

