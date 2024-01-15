from gtts import gTTS
import os

class TextToSpeech:
    def __init__(self):
        pass

    def text_to_speech(self, text, lang='en'): #convert text to speech using Google's Text-to-Speech API.
        tts = gTTS(text=text, lang=lang)   # create a gTTS object with the given text and language
        tts.save('output.mp3') # save the converted audio to a file
    def play_speech(self): #play the converted text-to-speech audio.
        os.system("start output.mp3")





#Test
if __name__ == "__main__":
    tts = TextToSpeech() # create an instance of the TextToSpeech class
    tts.text_to_speech("Hello, I am your virtual assistant.") # convert text to speech and save as mp3 file
    tts.play_speech()  # Play the generated speech audio
