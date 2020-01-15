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
      posts.insert(blogId="xxxxxxxxxxxxxxxx", body=artikel, isDraft=False).execute()

    except client.AccessTokenRefreshError:
        print ('Credensial Belum Benar')


body = {
	"kind": "blogger#post",
	"title": "Paercobaan Auto Post Blogger",
	"labels": [
		"Android",
		"Termux",
		"Hacking"
	],
	"content": "Percobaan Auto Posting Blogger Menggunakan Bahasa Pemrograman Python"
}
posting(sys.argv, body)