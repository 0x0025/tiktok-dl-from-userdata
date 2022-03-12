import yt_dlp

def dl(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'ignoreerrors': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

dl("https://www.tiktok.com/@wemijs/video/7069031542881848578?")
#https://www.tiktokv.com/share/video/7069031542881848578/