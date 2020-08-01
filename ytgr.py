#!/usr/bin/python3
# -*- coding: utf-8 -*-
API_TOKEN='1235042476:AAHraJCdLUwXPl-o_qcrjxwCslCwVsPE4zE'
import time
import subprocess
import telepot
import os
import urllib.request, urllib.error, urllib.parse
import sys
import urllib.request, urllib.parse, urllib.error
import re
import json
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import youtube_dl
import codecs


def handle(msg):
    def request_data():
        url = "https://www.youtube.com/results?search_query={}".format(urllib.parse.quote(command[3:]))
        print("Pesquisando vídeos em: {}".format(url))
        response = urlopen(url)
        data = response.read()
        response.close()
        return data

    def get_video_info(data):
        soup = BeautifulSoup(data, "html.parser")
        vid = soup.find(attrs={'class': 'yt-uix-tile-link'})

        link = "https://www.youtube.com" + vid['href']
        watchid = vid['href'].replace('/watch?v=', '')
        title = vid['title']

        return watchid, title, link

    chat_id, command = msg['chat']['id'], msg['text']
    print("Client {} requested command: '{}'".format(chat_id, command))
    if command.startswith('!down') or command.startswith('/down') or comman.startswith('#down') or command.startswith('down'):
        data = request_data()
        watchid, title, link = get_video_info(data)
        print("WatchID: {:15} Title: {:30}\t{}".format(watchid, title, link))

        bot.sendMessage(chat_id, title + "\n" + link)  # send Title & Link to Client

        options = {
            'outtmpl': title+".mp3",
            'playlist-end': "2",
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }]
        }
        filename = title+".mp3"
        bot.sendMessage(chat_id,"Transferências...")
        print(("[DEBUG] File Name: " + filename))
        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                print(ydl.download([link]))
        except:
            bot.sendMessage(chat_id,"Download Error")
        filename = filename.encode().decode("utf-8")
        bot.sendAudio(chat_id, audio=open(filename, "rb"))
        print("Sent!")
        os.remove(filename)

try:
    bot = telepot.Bot(API_TOKEN, threaded=False)
    bot.message_loop(handle)
    print('[+] Server is Listening')
    print('[=] Type Command from Telegram')
except:
    pass

while 1:
    time.sleep(2)
