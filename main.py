import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
from time import sleep



url_head = "https://www.kijiji.ca"
urls = []
numbers = []
total=0
kijiji_head = "https://www.kijiji.ca/b-achat-et-vente/ville-de-montreal/wholesale/page-"
kijiji_tail = "/k0c10l1700281?radius=20.0&address=Chinatown%2C+Ville-Marie%2C+Montreal%2C+QC&ll=45.507693,-73.560141&rb=true"

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def find_hitpoints(hitpoint):
    while urls==[]:
        global total
        response = requests.get(hitpoint, headers=HEADER)
        pprint(response)
        soup = BeautifulSoup(response.text, "html.parser")
        info = soup.find_all(class_="info-container")
        for data in info:
            urls.append(url_head + str(data.find(name="a")).split('href="')[1].strip().split('">')[0])
        total=len(urls)
        if urls==[]:
            sleep(60)




def extractNum(string):
    num = ''
    finalOpt = ""
    emailRegEx = re.compile("\D*([2-9]\d{2})(\D*)([2-9]\d{2})(\D*)(\d{4})\D*")
    m = emailRegEx.search(string)
    if m:
        num = m.group(0)
    for ch in num:
        if ch.isnumeric():
            finalOpt += ch
    return finalOpt


def getNumber(url):
    text="none"
    response = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        text = (str(soup.text).split('Description')[1].strip())
    except TypeError:
        text = str(soup.find(id="MainContainer"))
    except IndexError:
        pass
    return (extractNum(text))


def start_collecting(page_num):
    hitpoint = kijiji_head+str(page_num)+kijiji_tail
    find_hitpoints(hitpoint)
    pprint(urls)
    at = 0
    for url in urls:
        print(f"Im at {at}/{total}")
        num = getNumber(url)
        at+=1
        if len(num) > 9:
            data={
                "num":num,
                "url":url
            }
            numbers.append(data)


while len(numbers)<30:
    page_number=0
    start_collecting(page_number)
    page_number+=1
    pprint(numbers)
