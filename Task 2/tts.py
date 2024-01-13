# tts.py
from gtts import gTTS
import os

class TextToSpeech:
    def __init__(self):
        pass

    def text_to_speech(self, text, lang='en'):
        tts = gTTS(text=text, lang=lang)
        tts.save('output_tts.mp3')

    def play_speech(self):
        os.system("start output_tts.mp3")
