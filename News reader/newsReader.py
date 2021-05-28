from win32com.client.makepy import main
import requests
import time
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today are")
    api = "https://newsapi.org/v2/top-headlines?country=in&apiKey=4ee7891de5684d9c9dc4846d4024cda8"
    news = requests.get(api).text
    news_json = json.loads(news)
    arts = news_json['articles']

    for artical in arts:
        speak(artical['title'])
        time.sleep(.5)
        speak("Next news for you ...")

    