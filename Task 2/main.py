# Task 2
# You are building a text-to-speech model for a virtual assistant application that needs to sound natural and
# human-like.
# main.py
import NN
import tts

def main():
    # Testing tts.py
    print("Testing gTTS-based TTS...")
    tts_system = tts.TextToSpeech()
    tts_system.text_to_speech("Hello, world!")
    tts_system.play_speech()



if __name__ == "__main__":
    main()
