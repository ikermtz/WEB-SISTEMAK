import requests

# HELBURUA: web bezero honek irudi bat deskargatuko du

# HTTP eskaerak 4 eremu ditu:
metodoa = "GET"
uria = "http://www.httpwatch.com/httpgallery/chunked/chunkedtext.aspx"
goiburuak = { 'Host': 'www.httpwatch.com' }
edukia = ""

# eskaera bidali eta erantzuna jasoko dugu
erantzuna = requests.request(metodoa, uria, headers=goiburuak, data=edukia)

# HTTP erantzunak 4 atal ditu:
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(" ---- Kodea eta Deskribapena ----")
print(str(kodea) + " " + deskribapena)
print(" ")
print(" ---- Goiburuak ----")
for goiburua in erantzuna.headers: # erantzuna.headers hiztegi bat da
    print(goiburua + ": " + erantzuna.headers[goiburua])
print(" ")
print(" ---- Irudia ----")
edukia = erantzuna.content
print(edukia)

#Irudia fitxategi batean gorde
fitxategia = open("irudia.jpg", "wb")
fitxategia.write(edukia)
fitxategia.close