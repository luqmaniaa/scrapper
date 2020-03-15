import urllib.request
import requests
from bs4 import BeautifulSoup
import json
from time import sleep 

def parse_article_page(page_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(page_url,headers={'User-Agent': user_agent})
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html,'html.parser')
    main_post = soup.find('div',attrs={'class':'wrapperDetailArtikel'})
    title = main_post.find('h1',attrs={'class':'width-65 xs-width-auto'}).text
    articles = main_post.find('article',attrs={'class':'textArticle'}).text
    extracted_records = []
    record = {
        'title':title,
        'articles':articles,
    }
    extracted_records.append(record)
    return record

def scrape():
    extracted_data = []
    for page in range(0, 100, 10):
        base_url = 'https://katadata.co.id/search/cse/harga%20mesin/-/-/-/-/-/-' + str(page)
        page = requests.get(base_url)
        #request = urllib.request.Request(base_url,headers=headers)
        #html = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(page.text, 'html.parser')
        main_table = soup.find("div",class_="col-md-9 listing2")
        links = main_table.find_all("h4")
    
        for link in links:
            url = link.find('a').get('href','')
            if not url.startswith('http'):
                url = "https://katadata.co.id"+url
    
            extracted_data.append(parse_article_page(url))
    return extracted_data

if __name__ == "__main__":
    print(scrape())

