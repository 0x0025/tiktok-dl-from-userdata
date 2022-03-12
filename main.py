import re
from urllib import request
import yt_dlp
import ujson
from datetime import datetime

def dl(url, path):
    opts = {
        'outtmpl': 'downloads/%s /%(extractor)s-%(id)s-%(title)s.%(ext)s'.replace("%s ", path),
        'ignoreerrors': True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

f = open('user_data_fake.json', 'r')

udata = ujson.loads(f.read())

for like in udata['Activity']['Like List']['ItemFavoriteList']:
    link = like['VideoLink']
    path = datetime.strptime(like['Date'], '%Y-%m-%d %H:%M:%S').__format__('%Y-%m-%d')
    
    dl(link, path)
