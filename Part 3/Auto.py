import requests
import sys
import json
from time import sleep
from bs4 import BeautifulSoup
from oauth2client import client
from googleapiclient import sample_tools


def posting(argv, artikel):
    service, flags = sample_tools.init(
      argv, 'blogger', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/blogger')
    try:
      posts = service.posts()
      posts.insert(blogId="xxxxxxxxxxxxxxx", body=artikel, isDraft=False).execute()

    except client.AccessTokenRefreshError:
        print ('Credensial Belum Benar')



c = requests.session()
for i in range(370):
  r = c.get('https://rexdl.com/android/game/page/'+str(i+1)+'/')
  soup = BeautifulSoup(r.text,"html.parser")
  for apk in soup.findAll("span", class_="readmore a"):
     link_halaman = apk.find('a').get('href')
     r1 = c.get(link_halaman)
     soup1 = BeautifulSoup(r1.text,'html.parser')
     judul = soup1.find('title').text
     artikel_post = soup1.find('div', class_="entry themeform").find('div', class_="entry-inner").findAll('p')
     hasil_artikel = ''
     for artikel in artikel_post:
        hasil_artikel = hasil_artikel + str(artikel)
     body = {
        "kind": "blogger#post",
        "title": judul,
        "content": str(hasil_artikel),
        "labels": [
           "android",
           "Game",
           "sport"
        ]

     }
     try:
       posting(sys.argv, body)
       print ("Berhasil Memposting Artikel "+judul)
       sleep(60)
     except:
       sleep(15)
       print ('gagal Memposting Artikel')
