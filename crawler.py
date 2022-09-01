from get_html import get_html
from bs4 import BeautifulSoup
import re


def check_pub_list():
    response=get_html()
    
    Soup = BeautifulSoup(response.text)
    keywords=Soup.find_all('strong')[:-1]
    

    pub_list=[]
    for i in range(len(keywords)):
        if "Yang" not in str(keywords[i]):
            print(str(keywords[i]))
            to_append=re.search("<strong>(.+?)</strong>",str(keywords[i]))
            pub_list.append(to_append[1])
            
    return pub_list
