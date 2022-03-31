import requests
import sys
import zlib

# argv--> parametroak atzitzeko balio du
metodoa = 'GET'
uria = "https://www.google.es/"
goiburuak = {'Host': 'www.google.es'}

compressed = False
if len(sys.argv) == 1:
    goiburuak['Accept-Encoding']= 'identity'
elif sys.argv[1] == 'compress':
    compressed = True
    goiburuak['Accept-Encoding'] = 'gzip'
else:
    print("Errorea! Erabilera: python compression.py compress")
    exit(0)

erantzuna = requests.get(uria, headers=goiburuak, allow_redirects=False, stream=True)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

#erantzunetik edukia modu gordinean atera:
print("RESPONSE CONTENT LENGTH: " + str(len(erantzuna.raw.data)) + " byte")

# python compression.py --> 15946 byte
# python compression.py compress --> 6935 byte

for goiburua in erantzuna.headers:
    print(goiburua + ": " + erantzuna.headers[goiburua])

print("RESPONSE CONTENT LENGTH: " + str(len(erantzuna.raw.data)) + " byte")
if compressed:
    edukia_compressed = erantzuna.raw.data
    print(edukia_compressed)
    edukia_uncompressed = zlib.decompress(edukia_compressed, 16+zlib.MAX_WBITS)
    print("UNCOMPRESSED RESPONSE CONTENT LENGTH: " + str(len(edukia_uncompressed)) + " byte")


