import yt_dlp
import ujson
from datetime import datetime

print("Options:\n1-Download liked videos\n2-Download favorite videos\n3-Download this users videos\n4-Download all")

choice = int(input("Choice:"))

def dl(url, path):
    opts = {
        'outtmpl': '%s /%(extractor)s-%(id)s-%(title)s.%(ext)s'.replace("%s ", path),
        'ignoreerrors': True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

f = open('user_data.json', 'r')

udata = ujson.loads(f.read())

def dlLiked():
    for like in udata['Activity']['Like List']['ItemFavoriteList']:
        link = like['VideoLink']
        path = 'liked/' + datetime.strptime(like['Date'], '%Y-%m-%d %H:%M:%S').__format__('%Y-%m-%d')
        
        dl(link, path)

def dlFav():
    for fav in udata['Activity']['Favorite Videos']['FavoriteVideoList']:
        link = fav['VideoLink']
        path = 'favorite/' + datetime.strptime(fav['Date'], '%Y-%m-%d %H:%M:%S').__format__('%Y-%m-%d')
        
        dl(link, path)

def dlUser():
    for vid in udata['Video']['Videos']['VideoList']:
        link = vid['VideoLink']
        path = 'user/' + datetime.strptime(vid['Date'], '%Y-%m-%d %H:%M:%S').__format__('%Y-%m-%d')
        
        opts = {
            'outtmpl': '%s /%(title)s.%(ext)s'.replace("%s ", path),
            'ignoreerrors': True,
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([link])

if choice == 1:
    dlLiked()
    print('Done')
elif choice == 2:
    dlFav()
    print('Done')
elif choice == 3:
    dlUser()
    print('Done')
elif choice == 4:
    dlLiked()
    dlFav()
    dlUser()
    print('Done')
else:
    print('bad choice')

