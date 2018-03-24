from twython import Twython
import re
from re import *
import sys
import time
from datetime import date

today = date.today()
asu = today.strftime("%d-%m-%Y")

regex = re.compile(r"<td>(\d)</td>\s*<.*>(.*)\s*</td>\s*<.*>(.*)</td>\s*</tr>\s*<!--Posting-->")
with open("E:/an8/garismiring-an8.github.io/index.html", "r+") as notepad:
    baca = notepad.read()
    notepad.seek(0)
    tabel = re.search(regex,baca)
    no = tabel.group(1)
    rilisan = tabel.group(2)
    ukuran = tabel.group(3)+'MB'
    string = '''
['''+asu+'''][Miuna_BOT]
http://garismiring-an8.github.io
-----------RELEASED------------
No : '''+no+'''
Nama berkas : '''+rilisan+'''
Ukuran berkas : '''+ukuran+'''

#garismiringan8 #fastsub #kartun 
'''

APP_KEY = ''  # Customer Key here
APP_SECRET = ''  # Customer secret here
OAUTH_TOKEN = ''  # Access Token here
OAUTH_TOKEN_SECRET = ''  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.update_status(status=string)


