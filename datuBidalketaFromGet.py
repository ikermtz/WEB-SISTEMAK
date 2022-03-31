import urllib.parse

import requests


#HELBURUA: NAN zenbakiaren letra kalkulatzeko
#nabigatzaileak egiten duen simulazioa

base_uria = "http://ws-sendingformdata.appspot.com/processForm"
goiburuak = { 'Host': 'ws-sendingformdata.appspot.com'}
edukia = {'nan': '79177920'}
edukia_encoded = urllib.parse.urlencode(edukia)
uria = base_uria + '?' + edukia_encoded

erantzuna = requests.get(uria, headers=goiburuak, allow_redirects=False)
# metodoa = 'GET'
# erantzuna = requests.requests(metodoa, uria, headers=goiburuak, allow_redirects=False)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
edukia = erantzuna.content
print(edukia)