import speech_recognition as sr
from datetime import datetime
from time import ctime
from gtts import gTTS
import webbrowser
import playsound
import random
import time
import os


r = sr.Recognizer()

now = datetime.now()
current_time = now.strftime("%H:%M")

def voice_record(ask = False):
    with sr.Microphone() as source:
        if ask:
            friday_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            friday_speak('No vex, I never learn that one')
        except sr.RequestError:
            friday_speak('E be like say you no get data')
        return voice_data


def friday_speak(audio_string):
    tts = gTTS(text = audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    print(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def respond(voice_data):
    if 'how far' in voice_data:
        friday_speak('Nothing much, my Gee')

    if 'Maddow' in voice_data:
        friday_speak('No de shout on top my head')

    if 'wetin be your name' in voice_data:
        friday_speak('my guys de call me Odogwu but I won change my name to friday')

    if 'wetin be time' in voice_data:
        friday_speak('Naa ' + current_time + ' de nack')

    if 'help me find something' in voice_data:
        search = voice_record('Wetin you want make I find for you')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        friday_speak('see am for your screen ' + search )

    if  'where this place de' in voice_data:
        location = voice_record('Which place be that')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        friday_speak('Follow the map wey de your screen now ' + location)
    if 'later things' in voice_data:
        friday_speak('no wahala, my guy')
        exit()


time.sleep(1)
friday_speak("Wetin I go run for you")
while 1:
    voice_data = voice_record()
    print(voice_data)
    respond(voice_data)