# teletubemp3 - A Telegram Bot
![python](https://img.shields.io/pypi/pyversions/Django.svg)
![size](https://img.shields.io/github/size/ak-wa/teletubemp3/ytgr.py.svg)
![lastcommit](https://img.shields.io/github/last-commit/ak-wa/teletubemp3.svg)
![follow](https://img.shields.io/github/followers/ak-wa.svg?label=Follow&style=social)

**Telegram Bot for downloading Youtube videos as .mp3's & receiving in Telegram chat** 
  
Original Project: https://github.com/thezawad/teletubemp3  
My changes:  
* Now in Python 3 instead of 2  
* Can now parse whitespace search queries  
* Does not crash on Russian or other chars anymore
* Only downloads first video of playlists, not the whole thing
* Saves file as scraped Title + ".mp3", not default youtube_dl settings
* Multiple prefixes: "Yt","yt","Ют","ют"

<img alt="yt despacito" src="https://raw.githubusercontent.com/thezawad/teletubemp3/master/screenshot.png" width="350">

### Usage:
Terminal:
`python ytgr.py`  
  
Telegram:  
* Message to bot: `yt videoname`
* Searches for 'videoname' on Youtube
* Takes the first link from YouTube
* Downloads the video
* Converts it to mp3
* Sends the youtube link + mp3 as response on Telegram

### Installation:
```
git clone https://github.com/Ak-wa/teletubemp3.git
cd teletubemp3
pip install telepot
pip install urllib2
pip install requests
pip install bs4
pip install youtube_dl
brew install youtube-dl
brew install ffmpeg
```
Create `api.txt` and put your Api-Key in there.
