# Question 2
# Implement a neural network-based text to speech model that can produce speech with a natural-sounding
# tone and intonation. The model should be able to take as input a text string and output an audio waveform
# that corresponds to the spoken version of the text
import torch
import torchaudio
import numpy as np
from IPython.display import Audio
from scipy.io.wavfile import write

tacotron2 = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tacotron2', model_math='fp16').to('cuda').eval() # load pre-trained models from NVIDIA's repository
waveglow = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_waveglow', model_math='fp16') # load the WaveGlow model

waveglow = waveglow.remove_weightnorm(waveglow) # removed weight normalization from WaveGlow
waveglow = waveglow.to('cuda').eval() # moved the model to CUDA and set it to evaluation mode

utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_tts_utils') # loaded utility functions for text preprocessing

def text_to_speech(text):
    sequences, lengths = utils.prepare_input_sequence([text]) # prepare text input
    with torch.no_grad(): # generate mel-spectrogram and audio waveform
        mel, _, _ = tacotron2.infer(sequences, lengths)
        audio = waveglow.infer(mel)
    audio_numpy = audio[0].data.cpu().numpy()

    write("output.mp3", 22050, audio_numpy) # Save the generated speech to a mp3 file

# tests
input_text = "Hello World! I am a text-to-speech model   "
text_to_speech(input_text)

