#-*- coding: UTF-8 -*-
import urllib.parse

import requests
from bs4 import BeautifulSoup
import sys

# HTML kodea nola aztertu:
# Boton derecho --> Ver codigo fuente de la pagina

# "bilatu" zerbitzuko inprimakiaren HTML kodean "<form" elementua bilatu
# "method" atributuan datuak bidaltzeko erabili behar den metodoa adierazten da
metodoa = 'POST'
# "action" atributuan datuak jasoko dituen zerbitzariaren URI-a adierazten da
uri = 'https://www.ehu.eus/bilatu/buscar/sbilatu.php?lang=es1'
goiburuak = {'Host': 'www.ehu.eus',
             'Content-Type': 'application/x-www-form-urlencoded'}

# bidaliko den balioaren parametroaren izena
# dagokion "<input" elementuaren "name" atributuan adierazten da
edukia = {'abi_ize': sys.argv[1]}
#datuak inprimaki formatuan kodifikatu
edukia_encoded = urllib.parse.urlencode(edukia)

# "buscar" botoia sakatzea simulatzen dugu
erantzuna = requests.request(metodoa, uri, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
html = erantzuna.content

#
soup = BeautifulSoup(html, 'html_parser')
errenkada = soup.find_all('td', {'class': 'fondo_listado'})

for idx, each in enumerate(errenkada):
    izen_abizena = errenkada.a.text
    esteka = "https//:www.ehu.eus" + errenkada.a['href']
    print(str(idx) + " "+ izen_abizena + ": " + esteka)