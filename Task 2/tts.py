from gtts import gTTS
import os


class TextToSpeech:
    def __init__(self):
        pass

    def text_to_speech(self, text, lang='en'):
        tts = gTTS(text=text, lang=lang)
        tts.save('output.mp3')

    def play_speech(self):
        os.system("start output.mp3")


# Example usage
tts = TextToSpeech()
tts.text_to_speech("Hello, I am your virtual assistant.")
tts.play_speech()
