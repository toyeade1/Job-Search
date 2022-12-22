from bs4 import BeautifulSoup
import requests

API = 'https://api.sheety.co/952ea927b5ee42228ec81e7a704646d6/jobAggregation/jobmain'
URL = 'https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites'

response = requests.get(URL)
fortune_list = response.text
soup = BeautifulSoup(fortune_list, 'html.parser')
fortune_name = []
fortune_name2 = []
fn = soup.find_all(name='td')
for name in fn:
    company_name = name.getText()
    fortune_name2.append(company_name)

fortune_name = fortune_name2[4::3]

for company_name in fortune_name:
      sheet_input = {
          'jobmain': {
              'company': company_name
          }
      }
      sheet_response = requests.post(url=API, json=sheet_input)
      print(sheet_response.text)
