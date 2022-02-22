import sys
import youtube_dl


def download_youtube(url):
    with youtube_dl.YoutubeDL() as ydl:
        try:
            retcode = ydl.download([url])
        except youtube_dl.MaxDownloadsReached:
            ydl.to_screen('--max-download limit reached, aborting.')
            retcode = 101

    return retcode

url = 'https://www.youtube.com/watch?v=FvB-cB3-Z3o'
code = download_youtube(url)
sys.exit(code)
