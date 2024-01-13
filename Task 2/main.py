# main.py
import NN
import tts


def main():
    # Testing NN.py
    print("Testing NN-based TTS...")
    NN.generate_speech_nn("Hello, world from NN!")

    # Testing tts.py
    print("Testing gTTS-based TTS...")
    tts_system = tts.TextToSpeech()
    tts_system.text_to_speech("Hello, world!")
    tts_system.play_speech()


if __name__ == "__main__":
    main()
