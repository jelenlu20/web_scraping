from time import sleep
import requests
from bs4 import BeatifulSoup

#pip3 install requests bs4



base_url = "https://zvirata.bazos.cz/"

r = requests.get(base_url)
content = r.text
soup = beatifulSoup(content, "html.parser")

content = soup.find(boddy)
content = soup.find("div", {"class": "sirka"})
content = soup.find("div", {"class": "flexmain"})
content = soup.find("div", {"class": "maincontent"})

inzeraty = soup.finf.contenz(class, madpis

fro i in Inzeraty (
    b = i.find {ase_ur,
)

print ()
