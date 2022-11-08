import requests
from bs4 import BeautifulSoup
import json
def get_citations_needed_count(cite):
    '''
    function responsible for get the count of paragrah that have citation needed
    input cite:list
    output :int
    '''
    return len(cite)

def get_citations_needed_report():
    '''
    function responsile for give a repoet of paragrah that have citation needed
    otput:list
    '''
    all=soup.find('div',class_="mw-parser-output")
    p=all.find_all("p")
    w=[]
    [w.append(paragraph.text.strip()) for paragraph in p if paragraph.find('a',title="Wikipedia:Citation needed")]
    return w
    

URL="https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
count_of=soup.find_all('sup',class_="noprint Inline-Template Template-Fact") # count








  




# print(get_citations_needed_count(count_of))
all=get_citations_needed_report()
# print(all)
# for a in all :
#     pass


print("The number of Citation needed in the The Big Bang Theory wikipedia is "+str(get_citations_needed_count(count_of)),'\n')
n=1
for p in all:
    print(str(n) +'- Citation needed for '+"\""+ p +"\"",'\n')
    n+=1

