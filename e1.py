import requests
page = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General")
from bs4 import BeautifulSoup as bs
#Creating the list for election id and year through web scrapping

soup=bs(page.content,'html.parser')
f_tag=soup.find_all('tr','election_item')
election_id = [x.get("id").split("-")[2] for x in f_tag]
year_id=soup.find_all('td', attrs={'class':'year first'})
year = [pt.get_text() for pt in year_id]

#Creating a new list that contains information on election id and year
id_and_year=[]
for i in range (0,23):
    new=year[i], election_id[i]
    id_and_year.append(new)

with open ('ELECTION_ID', 'w') as file:
    for i in id_and_year:
        file.write("{}\n".format(i[0]+' '+i[1]+ ' '))
        print(i[0],i[1])
