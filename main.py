import re
from urllib import request
import yt_dlp
import requests


def dl(url):
    #print('Getting download url...')
    #r = requests.get(url) 
    #print(f'Downloading video: {r.url}')
    ydl_opts = {
        'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'ignoreerrors': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

#dl("https://www.tiktok.com/@wemijs/video/7069031542881848578?")
dl("https://www.tiktokv.com/share/video/7069031542881848578/")