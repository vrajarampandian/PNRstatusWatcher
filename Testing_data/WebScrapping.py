# importing the requests library
import requests
from bs4 import BeautifulSoup
import json
URL = "https://www.trainspnrstatus.com/pnrformcheck.php"
pnr_no = "4448717460"
data = {'lccp_pnrno1': pnr_no}
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'referer': 'https://www.trainspnrstatus.com/'}
r = requests.post(url=URL, data=data, headers=headers)
html_string = r.text
# print(html_string)
soup = BeautifulSoup(html_string, 'lxml')
table = soup.find('table')
print(table)
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    details = " "
    for i in range(0, len(cols)):
        details += cols[i].find(text=True) + "    "
    print(details)

table_data = [[cell.text for cell in row("td")]
                         for row in BeautifulSoup(html_string)("tr")]

print(table_data)
print(json.dumps(table_data))




