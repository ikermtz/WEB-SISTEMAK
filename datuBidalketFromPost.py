import urllib.parse

import requests


#HELBURUA: NAN zenbakiaren letra kalkulatzeko
#nabigatzaileak egiten duen simulazioa

uria = "http://ws-sendingformdata.appspot.com/processForm"
goiburuak = { 'Host': 'ws-sendingformdata.appspot.com',
            'Content-Type': 'application/x-www-form-urlencoded' }

#datuak hiztegi batean adierazi
edukia = {'nan': '79177920'}

#datuak inprimaki formatua duen kate baten bihurtu
#urllib liburutegiaren bidez
edukia_encoded = urllib.parse.urlencode(edukia)
goiburuak['Content-Length'] = str(len(edukia_encoded))

erantzuna = requests.post(uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)
# metodoa = 'POST'
# erantzuna = requests.requests(metodoa, uria, headers=goiburuak, allow_redirects=False)
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
edukia = erantzuna.content
print(edukia)