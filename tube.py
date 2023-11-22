#! /usr/bin/python3
#https://github.com/BG47510/

from urllib.parse import unquote
import requests
import re
import sys

erreur = 'https://raw.githubusercontent.com/BG47510/Zap/main/assets/error.m3u8'

def snif(url):
    lien = s.get(url, timeout=15).text
    retour = re.findall(r'\"hlsManifestUrl\":\"(.*?)\"\}', lien)
    tri = unquote(''.join(retour))
    flux = requests.get(tri).text
    if '#EXTM3U' not in tri:
        print(erreur)
    else:
        print(flux)

s = requests.Session()
result = snif(str(sys.argv[1]))
print(result)
