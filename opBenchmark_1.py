from bs4 import BeautifulSoup
import requests

page = requests.get("https://browser.geekbench.com/android-benchmarks")
soup = BeautifulSoup(page.content, "lxml")

def get_link():
    
    base_url = "https://browser.geekbench.com"
    no_of_phones = len(soup.find_all("td", class_="name"))
    
    for i in range(no_of_phones):
        try:
            link = soup.find_all("td", class_="name")[i].find("a")["href"]
        except:
            link = None
            
        yield f"{base_url}{link}"

