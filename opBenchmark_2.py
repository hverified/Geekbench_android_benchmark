from bs4 import BeautifulSoup
import requests
import opBenchmark_1
import pandas as pd

phone_list = []
for i in opBenchmark_1.get_link():
    phone_info = {}
    page = requests.get(i)
    soup = BeautifulSoup(page.content, "lxml")
    ex = soup.find("div",class_="processor-benchmark").find_all("div",class_="benchmark-box-wrapper")

    phone_info = {}
    phone_info["Brand"] = ex[3].find_all("td",class_="value")[0].text.split()[0]
    phone_info["Name"] = ex[3].find_all("td",class_="value")[0].text
    phone_info["Processor"] = ex[3].find_all("td",class_="value")[2].text
    phone_info["Processor_Frequency"] = ex[3].find_all("td",class_="value")[3].text
    phone_info["Processor_Cores"] = ex[3].find_all("td",class_="value")[4].text
    phone_info["Single_core"] = ex[0].find_all("div", class_="score")[0].text
    phone_info["Multi_core"] = ex[0].find_all("div", class_="score")[1].text
    phone_info["OpenCL"] = ex[1].find_all("div", class_="score")[0].text
    phone_info["RenderScript"] = ex[1].find_all("div", class_="score")[1].text
    phone_info["Battery"] = ex[2].find_all("div", class_="score")[0].text

    phone_list.append(phone_info)

df = pd.DataFrame(phone_list)
df.to_csv("Android Benchmark")
