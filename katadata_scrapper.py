#! C:/ProgramData/Anaconda3/python.exe
import requests
from bs4 import BeautifulSoup

print("Content-Type: text/html")
print()


def scrape():
    l = []
    for page in range(0, 100, 10):
        base_url = 'https://katadata.co.id/search/cse/industri%20mesin/-/-/-/-/-/-/' + str(page)
        
        page = requests.get(base_url)
        soup = BeautifulSoup(page.text, 'html.parser')

        main_table = soup.find("div",class_="col-md-9 listing2")
        links = main_table.find_all("h4")
        
        for item in links:
            d = { }

            #title and url
            title = item.find('a').text
            url = item.find('a').get('href','')
            if not url.startswith('http'):
                url = "https://katadata.co.id"+url
            d['title'] = title
            d['url'] = url

            l.append(d)
    
    return l


if __name__ == "__main__":
    print(scrape())
