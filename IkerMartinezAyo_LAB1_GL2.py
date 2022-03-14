import json
import urllib.parse

import psutil
import time
import signal
import sys
import requests


datuak = []

def cpu_ram():
    while True:
        cpu = psutil.cpu_percent() #erabiltzen ari den cpu %
        ram = psutil.virtual_memory().percent #erabiltzen ari den ram %
        print()
        print("CPU: %" + str(cpu) + "\tRAM: %" + str(ram))
        write_data(cpu,ram)
        time.sleep(15)


def handler(sig_num, frame):
    # Gertaera kudeatu
    ezabatu_channel()
    print('\nSignal handler called with signal ' + str(sig_num))
    print('Check signal number on '
          'https://en.wikipedia.org/wiki/Signal_%28IPC%29#Default_action')
    print('\nExiting gracefully')
    sys.exit(0)


def ezabatu_channel():
    # metodoa = 'DELETE'
    uria = "https://api.thingspeak.com/channels/" + str(datuak[0]) +".json"
    goiburuak = {'Host': 'api.thingspeak.com',
                 'Content-Type': 'application/x-www-form-urlencoded'}
    edukia = {'api_key': 'SI1WONHB9G2MPRVW'}
    edukia_encoded = urllib.parse.urlencode(edukia) #edukia kodetu
    goiburuak['Content-Length'] = str(len(edukia_encoded))

    #channel ezabaketa DELETE metodoaren bidez
    erantzuna = requests.delete(uria, headers=goiburuak,
                                data=edukia_encoded, allow_redirects=False)

    # Erantzunak 4 atal ditu baita: kodea, deskribapena, goiburuak eta edukia
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print("kanala hustu :")
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(edukia)

def sortu_channel():
    # metodoa = 'POST'
    uria = "https://api.thingspeak.com/channels.json"
    goiburuak = {'Host': 'api.thingspeak.com',
                 'Content-Type': 'application/x-www-form-urlencoded'}
    edukia = {'api_key': 'SI1WONHB9G2MPRVW',
              'name': 'Mychannel',
              'field1': '%CPU',
              'field2': '%RAM'}
    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))

    # channel sortu POST metodoaren bidez
    erantzuna = requests.post(uria, headers=goiburuak,
                              data=edukia_encoded, allow_redirects=False)

    # Erantzunak 4 atal ditu baita: kodea, deskribapena, goiburuak eta edukia
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(edukia)
    hiztegia = json.loads(edukia)
    kanala_id = hiztegia['id']
    write_api_key = hiztegia['api_keys'][0]['api_key']

    return kanala_id, write_api_key

def write_data(cpu,ram):
    #metodoa = post
    uria = "https://api.thingspeak.com/update.json"
    goiburuak = {'Host': 'api.thingspeak.com',
                 'Content-Type': 'application/x-www-form-urlencoded'}
    edukia = {'api_key': str(datuak[1]),
              'field1': cpu,
              'field2': ram}

    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))

    # channel sortu POST metodoaren bidez
    erantzuna = requests.post(uria, headers=goiburuak,
                              data=edukia_encoded, allow_redirects=False)

    # Erantzunak 4 atal ditu baita: kodea, deskribapena, goiburuak eta edukia
    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(edukia)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    print('Running. Press CTRL-C to exit.')
    datuak = sortu_channel()
    cpu_ram()
