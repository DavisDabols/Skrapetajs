import requests
import time
from bs4 import BeautifulSoup as bs

URL = 'https://www.delfi.lv/archive/latest.php'
LAPAS = 'lapas/'

def saglabat(url, datne):
    rezultats = requests.get(url)
    if rezultats.status_code == 200:
        with open(f"{LAPAS}{datne}", 'w', encoding='UTF-8') as f:
            f.write(rezultats.text)
    else:
        print(f"ERROR: Statusa kods {rezultats.status_code}")

def lejupieladet_lapas():
    saglabat(f"{URL}", f"lapa.html")
    time.sleep(1)

def info(datne):
    with open(datne, 'r', encoding='UTF-8') as f:
        html = f.read()

    zupa = bs(html, "html.parser")

    galvena = zupa.find(id = 'portal-main-content')

    elementi = galvena.find_all("div", class_="row d-flex mx-2 my-2 py-2 border-porcelain border-bottom text-black")

    for elements in elementi:
        raksts = {}

        elementu_teksts = elements.find("a", class_="text-mine-shaft")

        if elementu_teksts.text.strip().__contains__("Covid"):
            raksts["saite"] = elementu_teksts["href"]
            raksts["virsraksts"] = elementu_teksts.text.strip()
        CustomPrint(raksts)

def CustomPrint(raksts):
    if raksts != {}:
        print(raksts["virsraksts"] + "      ->" + raksts["saite"])

info('lapas/lapa.html')