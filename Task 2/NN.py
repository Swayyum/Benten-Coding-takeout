# Question 2
# Implement a neural network-based text to speech model that can produce speech with a natural-sounding
# tone and intonation. The model should be able to take as input a text string and output an audio waveform
# that corresponds to the spoken version of the text
import torch
import torchaudio
import numpy as np
from IPython.display import Audio
from scipy.io.wavfile import write

# Load pre-trained models from NVIDIA's repository
tacotron2 = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tacotron2', model_math='fp16').to('cuda').eval()
# Load the WaveGlow model
waveglow = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_waveglow', model_math='fp16')

# Remove weight normalization from WaveGlow
waveglow = waveglow.remove_weightnorm(waveglow)

# Move the model to CUDA and set it to evaluation mode
waveglow = waveglow.to('cuda').eval()


# Load utility functions for text preprocessing
utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tts_utils')

def text_to_speech(text):
    # Prepare text input
    sequences, lengths = utils.prepare_input_sequence([text])

    # Generate mel-spectrogram and audio waveform
    with torch.no_grad():
        mel, _, _ = tacotron2.infer(sequences, lengths)
        audio = waveglow.infer(mel)
    audio_numpy = audio[0].data.cpu().numpy()

    # Save the generated speech to a WAV file
    write("output.wav", 22050, audio_numpy)

# Example usage
input_text = "Hello World! I am a text-to-speech modal"
text_to_speech(input_text)

# The output.wav file can be played using an audio player
