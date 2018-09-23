# importing the requests library
import requests
from bs4 import BeautifulSoup
URL = "https://www.trainspnrstatus.com/pnrformcheck.php"
pnr_no = "4448717460"
data = {'lccp_pnrno1': pnr_no}
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'referer': 'https://www.trainspnrstatus.com/'}
r = requests.post(url=URL, data=data, headers=headers)
html_string =r.text
print(html_string)
soup = BeautifulSoup(html_string, 'lxml')
table = soup.find_all('table')
print(table)


